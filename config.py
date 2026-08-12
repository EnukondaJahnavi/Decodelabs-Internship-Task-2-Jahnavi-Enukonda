from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"

ALLOWED_STATUSES = {"pending", "in-progress", "completed"}
MIN_TITLE_LENGTH = 3
MAX_TITLE_LENGTH = 100
