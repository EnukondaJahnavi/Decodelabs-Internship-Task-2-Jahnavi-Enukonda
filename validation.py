from .config import (
    ALLOWED_STATUSES,
    MIN_TITLE_LENGTH,
    MAX_TITLE_LENGTH,
)

def validate_task_payload(payload, partial=False):
    if not isinstance(payload, dict):
        return ["Request body must be a JSON object."]

    errors = []

    if not partial or "title" in payload:
        title = payload.get("title")
        if not isinstance(title, str):
            errors.append("title must be a string.")
        elif not title.strip():
            errors.append("title is required.")
        elif len(title.strip()) < MIN_TITLE_LENGTH:
            errors.append(f"title must be at least {MIN_TITLE_LENGTH} characters.")
        elif len(title.strip()) > MAX_TITLE_LENGTH:
            errors.append(f"title must not exceed {MAX_TITLE_LENGTH} characters.")

    if "description" in payload and payload["description"] is not None:
        if not isinstance(payload["description"], str):
            errors.append("description must be a string.")

    if "status" in payload:
        status = payload["status"]
        if status not in ALLOWED_STATUSES:
            errors.append(
                "status must be one of: " + ", ".join(sorted(ALLOWED_STATUSES)) + "."
            )

    return errors
