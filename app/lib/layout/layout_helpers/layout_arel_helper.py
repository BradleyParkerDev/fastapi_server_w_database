from arel import HotReload, Path
from starlette.routing import WebSocketRoute
from contextlib import asynccontextmanager
from fastapi import FastAPI
import os

# Import here to avoid circular imports
from app.lib import CronJobUtility

class LayoutArelHelper():

    def __init__(self):
        # Initialize hot reload watching resources and public directories
        self.hotreload = HotReload(
            paths=[
                Path("resources", on_reload=[self.reload_data]),
                Path("public")
            ]
        )

        self.cron = None  # We’ll use this to manage the cron job

    # Define the lifespan context manager
    @asynccontextmanager
    async def lifespan(self, app:FastAPI):
        await self.hotreload.startup()

        # ✅ Start cron job on app startup (if enabled)
        if os.getenv("RUN_SCHEDULER", "false").lower() == "true":
            self.cron = CronJobUtility()
            self.cron.session.start_cron()

        yield
        await self.hotreload.shutdown()

        # ✅ Stop cron job on app shutdown
        if self.cron:
            self.cron.session.stop_cron()

    # Hot reload callback
    async def reload_data(self):
        print("Reloading server data...")