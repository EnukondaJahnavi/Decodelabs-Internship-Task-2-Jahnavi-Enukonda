# GitHub Submission

This is the final DecodeLabs Project 2 Backend API submission.

## Run
```bash
pip install -r requirements.txt
python run.py
```

## Test
```powershell
$env:PYTHONPATH="."
pytest -q
```

Expected result:
```text
5 passed
```

## API
- GET /api/tasks
- POST /api/tasks
- GET /api/tasks/<id>
- PUT /api/tasks/<id>
- PATCH /api/tasks/<id>
- DELETE /api/tasks/<id>
- GET /api/docs
