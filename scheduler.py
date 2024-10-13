from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from logger_config import logger
from check_notification import check_for_new_announcements

def start_scheduler():
    """Starts the APScheduler to check for new announcements periodically."""
    scheduler = AsyncIOScheduler()

    # Schedule the job every 60 minutes (1 hour)
    scheduler.add_job(check_for_new_announcements, 'interval', seconds=30)

    # Start the scheduler
    scheduler.start()
    logger.info("Scheduler started.")

    # Run the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.run_forever()

