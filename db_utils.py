from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()

# Retrieve the environment variables
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
host = os.getenv("MONGODB_HOST")
db_name = os.getenv("MONGODB_DB")

# URL-encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Construct the MongoDB URI
MONGODB_URI = f"mongodb+srv://{encoded_username}:{encoded_password}@{host}/{db_name}"

async def get_mongo_client():
    """Creates a MongoDB client connection."""
    return AsyncIOMotorClient(MONGODB_URI)


async def get_previous_announcements(collection):
    """Retrieves previously saved announcements from MongoDB."""
    cursor = collection.find({})
    return {announcement['text'] async for announcement in cursor}


async def save_announcements(collection, announcements):
    """Saves the current announcements to MongoDB."""
    for announcement in announcements:
        if await collection.count_documents({"text": announcement}) == 0:
            await collection.insert_one({"text": announcement})
