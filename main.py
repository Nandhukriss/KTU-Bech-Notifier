import asyncio
from scheduler import start_scheduler


def main():
    """Main function to start the scheduler."""
    start_scheduler()
    print("Scheduler started, checking for new announcements periodically...")

if __name__ == "__main__":
    main()