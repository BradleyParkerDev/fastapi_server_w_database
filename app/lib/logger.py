import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get log directory from environment variable (fallback to "logs" if not set)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Ensures base directory is project root
LOG_DIR = os.path.join(BASE_DIR, os.getenv("LOG_DIR", "logs"))  # Ensure logs stay inside project folder

# Ensure the logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger(name: str):
    """Create a logger for a given module."""
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        # File handler (logs to a file inside the project directory)
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, f"{name}.log"))
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Console handler (prints logs in the terminal)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))

        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
