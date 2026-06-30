# 🚀 FastAPI Practice

A simple project to practice and learn **FastAPI** concepts like routing, path parameters, query parameters, validation, and Pydantic schemas.

## 📂 Project Structure
* **`app/app.py`**: API routes and main application logic.
* **`app/schemas.py`**: Pydantic schemas for request validation.
* **`main.py`**: Entry point to start the development server.

## 🛠️ How to Run
Start the development server using `uv`:
```bash
uv run python main.py
```

Once running, you can access the automatic interactive API documentation at:
* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
