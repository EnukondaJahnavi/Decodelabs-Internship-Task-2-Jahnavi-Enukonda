# DecodeLabs Project 2 — Backend API Development

## Project
**Student Task Manager REST API**

This project implements the requirements described in the DecodeLabs Project 2 brief:
- Create GET and POST API endpoints
- Handle user input and responses
- Validate basic data
- Demonstrate backend/server-side logic and API concepts

It also includes additional professional API features such as PUT, PATCH, DELETE, JSON documentation, CORS, error handling, HTTP status codes and automated tests.

## Technology
- Python
- Flask
- Flask-CORS
- JSON file persistence
- Pytest

## Folder Structure

```text
DecodeLabs_Project_2_Backend_API/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── errors.py
│   ├── routes.py
│   ├── store.py
│   └── validation.py
├── data/
│   └── tasks.json
├── tests/
│   └── test_api.py
├── .gitignore
├── .env.example
├── requirements.txt
├── run.py
└── README.md
```

## Setup

### 1. Open the project folder
```bash
cd DecodeLabs_Project_2_Backend_API
```

### 2. Create a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the API
```bash
python run.py
```

Server:
`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome response |
| GET | `/api/health` | Health check |
| GET | `/api/tasks` | Get all tasks |
| GET | `/api/tasks/<id>` | Get a task |
| POST | `/api/tasks` | Create a task |
| PUT | `/api/tasks/<id>` | Replace a task |
| PATCH | `/api/tasks/<id>` | Partially update a task |
| DELETE | `/api/tasks/<id>` | Delete a task |
| GET | `/api/docs` | API documentation |

## POST Example

URL:
`POST http://127.0.0.1:5000/api/tasks`

Header:
`Content-Type: application/json`

Body:
```json
{
  "title": "Finish DecodeLabs Project 2",
  "description": "Test and submit the backend API",
  "status": "pending"
}
```

Expected result:
- HTTP `201 Created`
- JSON response containing the created task.

## Validation

`title`:
- required
- must be a string
- 3–100 characters

`description`:
- optional string

`status`:
- `pending`
- `in-progress`
- `completed`

Invalid input returns `400 Bad Request`.

## HTTP Status Codes

- `200 OK` — successful request
- `201 Created` — resource created
- `204 No Content` — resource deleted
- `400 Bad Request` — invalid input
- `404 Not Found` — resource does not exist
- `415 Unsupported Media Type` — request is not JSON
- `500 Internal Server Error` — unexpected server error

## Testing

Run:
```bash
pytest -q
```

The included tests cover:
- health endpoint
- GET tasks
- POST task
- validation
- 404 handling

## GitHub Submission

Do not upload the `venv` folder. It is excluded by `.gitignore`.

Recommended repository name:
`decodelabs-project-2-backend-api`

After pushing the project, submit the GitHub repository URL according to your internship instructions.

## Project Requirement Mapping

### GET / POST
Implemented in `app/routes.py`.

### User input and responses
The POST/PUT/PATCH endpoints accept JSON request bodies and return structured JSON responses.

### Basic validation
Implemented in `app/validation.py`.

### Backend/server-side logic
Implemented through Flask routes, validation, persistence and centralized error handling.

### API concepts
The project demonstrates REST resource naming, HTTP methods, JSON, status codes, stateless request handling and error responses.
