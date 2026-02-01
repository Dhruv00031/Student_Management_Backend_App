# Student Management System (Backend)

## 📌 Project Description
A backend REST API built using Django and Django REST Framework to manage student records with authentication and role-based access control.

The project focuses on backend fundamentals such as authentication, authorization, CRUD operations, and database integrity.

---

## 🛠 Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (PostgreSQL ready)
- Git & GitHub

---

## 🔐 Authentication
- User Registration
- User Login
- Token-based Authentication
- Admin-only delete permission

---

## 👨‍🎓 Student Module
Each student contains:
- Name
- Roll Number (unique)
- Email (unique)
- Course
- Year
- Created Timestamp

---

## 📡 API Endpoints

### Auth
- `POST /api/users/register/`
- `POST /api/users/login/`

### Students
- `GET /api/students/`
- `POST /api/students/`
- `GET /api/students/<id>/`
- `PUT /api/students/<id>/`
- `DELETE /api/students/<id>/` (Admin only)

---

## ⚙️ Setup Instructions
```bash
git clone <repository-url>
cd student_management
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


## 🗄 Database
- SQLite used for local development
- PostgreSQL configuration prepared for production use

## 🔒 Security Notes
- Token-based authentication
- Role-based permissions (admin-only delete)
- Input validation at serializer level

## 🔄 API Versioning
All endpoints are versioned to support future changes without breaking clients.

Current version:
- `/api/v1/`

## 🗄 Database Strategy
- SQLite used for local development
- PostgreSQL configuration prepared for production
- Designed to switch databases without code changes

## ✨ Key Backend Concepts Demonstrated
- Token-based authentication
- Role-based permissions
- RESTful CRUD APIs
- Serializer-level validation
- Pagination, filtering, ordering, and search
- API versioning
