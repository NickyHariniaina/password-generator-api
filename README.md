# FastAPI Password Generator & Checker

This project is a simple API built with FastAPI that provides two main functionalities:

- **Generate** random passwords
- **Check** if a password is strong based on criteria

---

## 🚀 Features

- Generate secure random passwords with customizable options
- Check password strength including presence of uppercase, lowercase, digits, and special characters
- FastAPI auto-generated interactive API docs at `/docs` and `/redoc`

---

## 📦 API Endpoints

### Generate Password

`GET /api/generate`

Generate a random password with a length of 8 characters that is strong enough.

`GET /api/generate?length=10`

Generate a random password with a length of 10 characters that is strong enough.

### Check Strength

`POST /api/check_password`

```json
{
  "password": "your_password_here"
}
```

## ⚙️Installation

First clone the repository:

```bash
git clone https://github.com/NickyHariniaina/password-generator-api.git
cd password-generator-api
```

(Optional but recommended)

Create and activate a virtual environments:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the following commands to run it:

```bash
uvicorn src.main:app --reload
```

Now test it with the base url: **http://127.0.0.1/**

_If you want to test it in the browser... I recommend you to use http://127.0.0.1/docs_
