# API Testing Checklist

Use Postman, Thunder Client, curl, or a browser for GET requests.

## 1. Health
GET `/api/health`
Expected: `200`

## 2. Get tasks
GET `/api/tasks`
Expected: `200`

## 3. Create task
POST `/api/tasks`
Content-Type: application/json

```json
{
  "title": "Test POST request",
  "description": "Created from Postman",
  "status": "pending"
}
```

Expected: `201`

## 4. Invalid task
POST `/api/tasks`

```json
{
  "title": "Hi"
}
```

Expected: `400`

## 5. Get one task
GET `/api/tasks/1`
Expected: `200` if task 1 exists.

## 6. Missing task
GET `/api/tasks/99999`
Expected: `404`

## 7. Update
PATCH `/api/tasks/1`

```json
{
  "status": "completed"
}
```

Expected: `200`

## 8. Delete
DELETE `/api/tasks/1`
Expected: `204`
