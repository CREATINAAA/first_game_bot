import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__name__).resolve().parent.parent.parent

load_dotenv(os.path.join(BASE_DIR / '.env'))

BOT_TOKEN = os.environ.get('BOT_TOKEN')
