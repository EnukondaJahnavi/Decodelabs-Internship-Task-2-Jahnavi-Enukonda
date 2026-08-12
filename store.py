import json
from threading import Lock
from . import config


_lock = Lock()


def _ensure_file():
    config.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not config.DATA_FILE.exists():
        config.DATA_FILE.write_text("[]", encoding="utf-8")


def read_tasks():
    _ensure_file()

    with _lock:
        try:
            return json.loads(
                config.DATA_FILE.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError):
            return []


def write_tasks(tasks):
    _ensure_file()

    with _lock:
        config.DATA_FILE.write_text(
            json.dumps(tasks, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )