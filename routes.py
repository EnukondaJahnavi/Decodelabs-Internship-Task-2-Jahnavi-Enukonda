from datetime import datetime, timezone
from flask import Blueprint, jsonify, request
from .store import read_tasks, write_tasks
from .validation import validate_task_payload

api = Blueprint("api", __name__)

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def find_task(tasks, task_id):
    return next((task for task in tasks if task["id"] == task_id), None)

@api.get("/health")
def health():
    return jsonify({
        "success": True,
        "status": "healthy",
        "service": "DecodeLabs Project 2 API",
        "timestamp": utc_now()
    }), 200

@api.get("/tasks")
def get_tasks():
    tasks = read_tasks()
    status = request.args.get("status")

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    return jsonify({
        "success": True,
        "count": len(tasks),
        "data": tasks
    }), 200

@api.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = find_task(read_tasks(), task_id)

    if not task:
        return jsonify({
            "success": False,
            "error": {"code": 404, "message": "Task not found."}
        }), 404

    return jsonify({"success": True, "data": task}), 200

@api.post("/tasks")
def create_task():
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": {"code": 415, "message": "Content-Type must be application/json."}
        }), 415

    payload = request.get_json(silent=True)
    errors = validate_task_payload(payload)

    if errors:
        return jsonify({
            "success": False,
            "error": {
                "code": 400,
                "message": "Validation failed.",
                "details": errors
            }
        }), 400

    tasks = read_tasks()
    next_id = max((task["id"] for task in tasks), default=0) + 1

    task = {
        "id": next_id,
        "title": payload["title"].strip(),
        "description": payload.get("description", "").strip(),
        "status": payload.get("status", "pending"),
        "created_at": utc_now(),
        "updated_at": utc_now()
    }

    tasks.append(task)
    write_tasks(tasks)

    return jsonify({
        "success": True,
        "message": "Task created successfully.",
        "data": task
    }), 201

@api.put("/tasks/<int:task_id>")
def replace_task(task_id):
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": {"code": 415, "message": "Content-Type must be application/json."}
        }), 415

    payload = request.get_json(silent=True)
    errors = validate_task_payload(payload)

    if errors:
        return jsonify({
            "success": False,
            "error": {"code": 400, "message": "Validation failed.", "details": errors}
        }), 400

    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        return jsonify({
            "success": False,
            "error": {"code": 404, "message": "Task not found."}
        }), 404

    task.update({
        "title": payload["title"].strip(),
        "description": payload.get("description", "").strip(),
        "status": payload.get("status", "pending"),
        "updated_at": utc_now()
    })
    write_tasks(tasks)

    return jsonify({
        "success": True,
        "message": "Task replaced successfully.",
        "data": task
    }), 200

@api.patch("/tasks/<int:task_id>")
def update_task(task_id):
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": {"code": 415, "message": "Content-Type must be application/json."}
        }), 415

    payload = request.get_json(silent=True)
    errors = validate_task_payload(payload, partial=True)

    if errors:
        return jsonify({
            "success": False,
            "error": {"code": 400, "message": "Validation failed.", "details": errors}
        }), 400

    if not payload:
        return jsonify({
            "success": False,
            "error": {"code": 400, "message": "At least one field is required."}
        }), 400

    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        return jsonify({
            "success": False,
            "error": {"code": 404, "message": "Task not found."}
        }), 404

    for field in ("title", "description", "status"):
        if field in payload:
            value = payload[field]
            task[field] = value.strip() if isinstance(value, str) else value

    task["updated_at"] = utc_now()
    write_tasks(tasks)

    return jsonify({
        "success": True,
        "message": "Task updated successfully.",
        "data": task
    }), 200

@api.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        return jsonify({
            "success": False,
            "error": {"code": 404, "message": "Task not found."}
        }), 404

    tasks = [item for item in tasks if item["id"] != task_id]
    write_tasks(tasks)

    return jsonify({
        "success": True,
        "message": "Task deleted successfully."
    }), 204

@api.get("/docs")
def docs():
    return jsonify({
        "name": "DecodeLabs Project 2 - Student Task Manager API",
        "version": "1.0.0",
        "description": "Simple RESTful backend API demonstrating GET/POST, validation, JSON responses and HTTP status codes.",
        "endpoints": [
            {"method": "GET", "path": "/api/health", "description": "Health check"},
            {"method": "GET", "path": "/api/tasks", "description": "Get all tasks"},
            {"method": "GET", "path": "/api/tasks/<id>", "description": "Get one task"},
            {"method": "POST", "path": "/api/tasks", "description": "Create a task"},
            {"method": "PUT", "path": "/api/tasks/<id>", "description": "Replace a task"},
            {"method": "PATCH", "path": "/api/tasks/<id>", "description": "Partially update a task"},
            {"method": "DELETE", "path": "/api/tasks/<id>", "description": "Delete a task"}
        ],
        "validation": {
            "title": "required, string, 3-100 characters",
            "description": "optional string",
            "status": "pending | in-progress | completed"
        },
        "status_codes": [200, 201, 204, 400, 404, 415, 500]
    }), 200
