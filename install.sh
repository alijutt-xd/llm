#!/usr/bin/env bash
# LLM Gateway - Universal Installation Script
# Works on: Linux, macOS, Windows (Git Bash), Termux, Docker
# ================================================================================

set -e  # Exit on error

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "\n${BLUE}=== $1 ===${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if grep -qi termux /proc/version 2>/dev/null || [[ -f /system/build.prop ]]; then
            echo "termux"
        elif [[ -f /etc/os-release ]]; then
            . /etc/os-release
            echo "$ID"
        else
            echo "linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "windows"
    else
        echo "unknown"
    fi
}

# Check Python version
check_python() {
    print_header "Checking Python Installation"
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 not found!"
        echo "Please install Python 3.10+ first"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    print_success "Python $PYTHON_VERSION found"
    
    # Check if version is 3.10 or higher
    if [[ $(echo "$PYTHON_VERSION < 3.10" | bc) -eq 1 ]]; then
        print_warning "Python 3.10+ is recommended, but continuing with $PYTHON_VERSION"
    fi
}

# Install system dependencies based on OS
install_system_deps() {
    OS=$(detect_os)
    print_header "Detecting OS: $OS"
    
    case $OS in
        termux)
            print_header "Installing Termux Dependencies"
            pkg update -y
            pkg install -y python python-pip python-dev git clang libffi libffi-dev openssl openssl-dev curl wget make pkg-config
            print_success "Termux dependencies installed"
            ;;
        ubuntu|debian)
            print_header "Installing Ubuntu/Debian Dependencies"
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-dev python3-venv git build-essential libffi-dev libssl-dev curl wget
            print_success "Ubuntu/Debian dependencies installed"
            ;;
        fedora|rhel|centos)
            print_header "Installing Fedora/RHEL Dependencies"
            sudo dnf install -y python3 python3-pip python3-devel git gcc libffi-devel openssl-devel curl wget
            print_success "Fedora/RHEL dependencies installed"
            ;;
        arch)
            print_header "Installing Arch Linux Dependencies"
            sudo pacman -Syu --noconfirm
            sudo pacman -S --noconfirm python python-pip base-devel libffi openssl git curl wget
            print_success "Arch Linux dependencies installed"
            ;;
        macos)
            print_header "Installing macOS Dependencies"
            if ! command -v brew &> /dev/null; then
                print_warning "Homebrew not found. Installing..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install python3 git libffi openssl
            print_success "macOS dependencies installed"
            ;;
        windows)
            print_warning "Windows detected. Please ensure Python 3.10+ and Git are installed"
            print_warning "Download from: https://www.python.org/downloads/"
            ;;
        *)
            print_warning "Unknown OS. Assuming dependencies are installed"
            ;;
    esac
}

# Create virtual environment
create_venv() {
    print_header "Setting Up Virtual Environment"
    
    if [[ -d "venv" ]]; then
        print_warning "Virtual environment already exists"
        read -p "Remove and recreate? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf venv
        else
            return
        fi
    fi
    
    python3 -m venv venv
    print_success "Virtual environment created"
    
    # Activate venv
    if [[ "$OS" == "windows" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    print_success "Virtual environment activated"
}

# Upgrade pip
upgrade_pip() {
    print_header "Upgrading pip, setuptools, and wheel"
    
    pip install --upgrade pip setuptools wheel
    print_success "pip, setuptools, and wheel upgraded"
}

# Install dependencies
install_deps() {
    print_header "Installing Python Dependencies"
    
    print_warning "Installing core packages first (for Termux compatibility)..."
    pip install Flask Werkzeug Flask-CORS requests python-dotenv cryptography SQLAlchemy Flask-SQLAlchemy pydantic
    
    print_warning "Installing additional packages..."
    if ! pip install -r requirements.txt 2>/dev/null; then
        print_warning "Full installation failed, but core packages are installed"
        print_warning "Try installing remaining packages manually:"
        echo "  pip install --no-cache-dir APScheduler"
        echo "  pip install --no-cache-dir gunicorn"
        echo "  pip install --no-cache-dir Pillow"
    fi
    
    print_success "Dependencies installed"
}

# Configure environment
configure_env() {
    print_header "Configuring Environment"
    
    if [[ -f ".env" ]]; then
        print_warning ".env file already exists"
        read -p "Reconfigure? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm .env
        else
            return
        fi
    fi
    
    cp .env.example .env
    print_success ".env file created"
    
    # Generate random SECRET_KEY
    SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    sed -i.bak "s/dev-secret-key-change-in-production/$SECRET_KEY/g" .env
    
    print_warning "Please edit .env with your settings:"
    echo "  nano .env (or your preferred editor)"
}

# Test installation
test_installation() {
    print_header "Testing Installation"
    
    python3 -c "import flask; print(f'Flask version: {flask.__version__}')"
    print_success "Flask working"
    
    python3 -c "import sqlalchemy; print(f'SQLAlchemy version: {sqlalchemy.__version__}')"
    print_success "SQLAlchemy working"
    
    python3 -c "import cryptography; print('Cryptography working')"
    print_success "Cryptography working"
    
    print_success "All core modules working!"
}

# Main installation flow
main() {
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════════════════════════════════╗"
    echo "║                  LLM Gateway - Universal Installer                 ║"
    echo "║            Compatible with Linux, macOS, Windows, Termux           ║"
    echo "╚════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    check_python
    install_system_deps
    create_venv
    upgrade_pip
    install_deps
    configure_env
    test_installation
    
    echo -e "\n${GREEN}"
    echo "╔════════════════════════════════════════════════════════════════════╗"
    echo "║                 Installation Complete! 🎉                          ║"
    echo "╚════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "\n${BLUE}Next steps:${NC}"
    echo "1. Activate virtual environment:"
    
    if [[ "$OS" == "windows" ]]; then
        echo "   venv\\Scripts\\activate"
    else
        echo "   source venv/bin/activate"
    fi
    
    echo ""
    echo "2. Configure environment:"
    echo "   nano .env"
    echo ""
    echo "3. Run the application:"
    echo "   python app.py"
    echo ""
    echo "4. Access dashboard:"
    echo "   http://localhost:5000"
    echo ""
    echo -e "${GREEN}For help: https://github.com/alijutt-xd/llm${NC}\n"
}

# Run main function
main "$@"
