from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from check_notification import check_for_new_announcements

def start_scheduler():
    """Starts the APScheduler to check for new announcements periodically."""
    scheduler = AsyncIOScheduler()

    # Schedule the job every 60 minutes (1 hour)
    scheduler.add_job(check_for_new_announcements, 'interval', seconds=120)

    # Start the scheduler
    scheduler.start()
    print("Scheduler started.")

    # Run the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.run_forever()

