import base64
import hashlib

from cryptography.fernet import Fernet


class SecretManager:
    def __init__(self, secret_key: str):
        if not secret_key:
            raise ValueError("SECRET_KEY is required for encrypted provider secrets")
        self.cipher = self._build_cipher(secret_key)

    def _build_cipher(self, secret_key: str) -> Fernet:
        digest = hashlib.sha256(secret_key.encode("utf-8")).digest()
        key = base64.urlsafe_b64encode(digest[:32].ljust(32, b"0"))
        return Fernet(key)

    def encrypt(self, value: str) -> str:
        if not value:
            return value
        return self.cipher.encrypt(value.encode("utf-8")).decode("utf-8")

    def decrypt(self, value: str) -> str:
        if not value:
            return value
        if value.startswith("enc:"):
            value = value.replace("enc:", "", 1)
            return self.cipher.decrypt(value.encode("utf-8")).decode("utf-8")
        return value
