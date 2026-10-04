from datetime import datetime
from typing import Optional


class Scheduler:
    """Simple job scheduler for background tasks."""

    def __init__(self):
        """Initialize scheduler."""
        self.jobs: dict = {}
        self.running = False

    def add_job(self, name: str, func, interval_seconds: int) -> None:
        """Add scheduled job."""
        self.jobs[name] = {
            "func": func,
            "interval_seconds": interval_seconds,
            "last_run": None,
        }

    def start(self) -> None:
        """Start scheduler."""
        self.running = True

    def stop(self) -> None:
        """Stop scheduler."""
        self.running = False

    async def tick(self) -> None:
        """Run scheduled jobs."""
        now = datetime.utcnow()
        for name, job in self.jobs.items():
            last_run = job.get("last_run")
            if last_run is None or (
                now - last_run
            ).total_seconds() >= job["interval_seconds"]:
                try:
                    if callable(job["func"]):
                        await job["func"]()
                    job["last_run"] = now
                except Exception as e:
                    print(f"[scheduler] Job {name} failed: {e}")
