# Execution Data Platform

A backend task management platform built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**, demonstrating modern backend engineering practices including REST API design, relational database modelling, authentication, cloud deployment, and API documentation.

---

## Overview

Execution Data Platform is a backend-driven application developed to explore modern software engineering principles through a practical productivity platform.

The project provides a RESTful API that allows users to create and manage tasks while demonstrating clean backend architecture, secure authentication, persistent data storage, and cloud deployment.

Rather than focusing solely on functionality, the project was built to strengthen core backend engineering skills including API development, database design, deployment, and software architecture.

---

## Problem

Many productivity applications require a reliable backend capable of storing, retrieving, and managing structured task data. This project explores how such a backend can be designed using modern Python technologies while remaining lightweight, maintainable, and scalable.

---

## Solution

The application exposes a REST API built with FastAPI that integrates with a PostgreSQL database to provide persistent task management.

The backend demonstrates:

- RESTful API design
- JWT-based authentication
- Relational database design
- Interactive API documentation
- Cloud deployment
- Modular project structure

---

## Features

- RESTful API endpoints
- Task creation and retrieval
- JWT Authentication
- PostgreSQL database integration
- Interactive Swagger / OpenAPI documentation
- Persistent cloud-hosted database
- Modular backend architecture

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| SQLAlchemy | ORM |
| JWT | Authentication |
| HTML / CSS / JavaScript | Frontend |
| Swagger / OpenAPI | API Documentation |
| Railway | Cloud Deployment |

---

## Architecture

```
                Browser
                     │
     HTML / CSS / JavaScript
                     │
             REST API Requests
                     │
              FastAPI Application
                     │
          Authentication (JWT)
                     │
               PostgreSQL Database
```

---

## API Documentation

Interactive API documentation is automatically generated using Swagger/OpenAPI.

After running the application locally, documentation is available at:

```
/docs
```

---

## Live Demo

https://executiondataplatform-production-c903.up.railway.app/tasks

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Ishigxki/Execution_data_platform.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn main:app --reload
```

### Open

```
http://127.0.0.1:8000/docs
```

to explore the API using Swagger.

---

## Project Structure

```
Execution_data_platform/

├── app/
├── routers/
├── models/
├── database/
├── static/
├── templates/
├── main.py
├── requirements.txt
└── README.md
```

*(Folder names may vary slightly depending on the current project version.)*

---

## Screenshots

### Task Management Interface

Displays the web interface used to create and manage tasks.

![Add task UI](screenshots/ui-add-task.png)
*web UI for adding tasks and submitting them to the backend.*

---

### Swagger Documentation

Interactive API documentation generated automatically by FastAPI.

![Backend data captured](screenshots/backend-data-captured.png)
*Database/backend view showing tasks captured from the UI.*

---


## Lessons Learned

Developing this project strengthened my understanding of:

- Backend API architecture
- FastAPI application development
- REST API design
- PostgreSQL database modelling
- JWT authentication
- API documentation using Swagger/OpenAPI
- Deploying backend services to the cloud

---

## Future Improvements

- Role-Based Access Control (RBAC)
- Docker containerisation
- CI/CD with GitHub Actions
- Automated testing
- Redis caching
- Background task processing
- User analytics dashboard
- Email notifications

---

## Author

**Bonga Maseko**

Graduate Software Engineer

GitHub: https://github.com/Ishigxki

LinkedIn: https://www.linkedin.com/in/bonga-maseko-187547361/

---

## License

This project is provided for educational and portfolio purposes.
