
# FastAPI Project Troubleshooting Guide

This guide provides solutions to common errors that you might encounter while setting up and running a FastAPI project.

## Table of Contents

- [ModuleNotFoundError](#modulenotfounderror)
- [Attribute Not Found](#attribute-not-found)
- [ASGI App Import Error](#asgi-app-import-error)

## ModuleNotFoundError

**Error Message**: `ModuleNotFoundError: No module named 'app'`

**Solution**:

1. **Check Directory Structure**: Ensure your project structure resembles:
fastapi-mongo/
├── app/
│ ├── init.py
│ ├── main.py
│ └── server/
│ ├── init.py
│ ├── app.py
└── venv/


2. **Import Path**: Use correct import path in "main.py":
```python
uvicorn.run("app.server.app:app", host="0.0.0.0", port=8000, reload=True)

3. Activate Virtual Environment: Ensure virtual environment is active:
source venv/bin/activate  # macOS/Linux

Attribute Not Found

Error Message: Attribute "app" not found in module "server.app"

Solution:

1. Check Import Path: Verify the import path in "main.py":
uvicorn.run("app.server.app:app", host="0.0.0.0", port=8000, reload=True)
2. Verify Module Definition: Confirm "app" object is defined in "app.py".
3. Run without --reload: Try:
uvicorn app.server.app:app --host 0.0.0.0 --port 8000

Contributing

Contributions to this troubleshooting guide are welcome! If you encounter new errors and solutions, please submit a pull request.






    