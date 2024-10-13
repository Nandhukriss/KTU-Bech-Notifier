import logging
from pathlib import Path

# Create a folder for logs if it doesn't exist
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# Define the log file path within the logs folder
log_file_path = log_folder / "ktu_notification_bot.log"

# Create a custom logger
logger = logging.getLogger("ktu_notification_bot")
logger.setLevel(logging.INFO)  # Set logging level to INFO (or DEBUG, WARNING as needed)

# Create handlers
file_handler = logging.FileHandler(log_file_path)
console_handler = logging.StreamHandler()

# Set the level for each handler
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# To avoid propagating logs to the root logger (which prevents other loggers' messages)
logger.propagate = False



