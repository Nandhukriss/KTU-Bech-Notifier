
from db_utils import get_mongo_client, get_previous_announcements, save_announcements
from notification import send_message
from scraper import fetch_announcements



async def check_for_new_announcements():
    """Checks if there are new announcements by comparing with the previously saved ones."""
    client = await get_mongo_client()
    db = client["announcements_db"]
    collection = db["btech_announcements"]

    current_announcements = await fetch_announcements()
    previous_announcements = await get_previous_announcements(collection)

    # Compare the current announcements with the previous ones
    new_announcements = [announcement for announcement in current_announcements if announcement not in previous_announcements]

    if new_announcements:
        
        for announcement in new_announcements:
            print(announcement)
            send_message(announcement)
        await save_announcements(collection, new_announcements)
    else:
        print("No new announcements.")

    client.close()