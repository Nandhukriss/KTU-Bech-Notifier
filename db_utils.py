from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DB_NAME = "announcements_db"

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
