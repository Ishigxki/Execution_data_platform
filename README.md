# Execution_data_platform
Productivity & Data intelligence platform

## Overview
This project provides a backend API system that allows structured data to be ingested, processed, and accessed through clean and modular endpoints.

## Problem
Many applications need to process and manage structured data workflows, but lack a simple backend system to handle ingestion, processing, and retrieval efficiently.

## Solution
A lightweight FastAPI backend with a PostgreSQL database that stores task entries and exposes endpoints for creating and fetching tasks.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- REST APIs
- JSON

## Features
- Data ingestion endpoints
- Task creation and retrieval
- Simple frontend UI for adding tasks
- Modular backend structure

## Screenshots
### Simple task creation UI
![Add task UI](screenshots/ui-add-task.png)
*Simple web UI for adding tasks and submitting them to the backend.*

### Backend data captured
![Backend data captured](screenshots/backend-data-captured.png)
*Database/backend view showing tasks captured from the UI.*

## How to Run
1. Clone the repo
2. Install dependencies from `requirements.txt`
3. Run the server with `python -m uvicorn main:app --reload`
4. Open `index.html` in your browser to use the frontend

## Future Improvements
- Authentication
- Scaling data processing
- Database integration enhancements


