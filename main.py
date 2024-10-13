
from scheduler import start_scheduler
from logger_config import logger
def main():
    """Main function to start the scheduler."""
    start_scheduler()
    logger.info("Scheduler started, checking for new announcements periodically...")

if __name__ == "__main__":
    main()