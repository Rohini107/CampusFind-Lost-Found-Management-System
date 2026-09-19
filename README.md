# CampusFind — Lost & Found Management System

#Problem Statement

In colleges and universities, students frequently lose personal belongings such as mobile phones, wallets, identity cards, books, bags, calculators, keys, and other valuable items. Traditionally, information about lost and found items is shared through word of mouth, notice boards, or informal messaging groups.

These methods make it difficult to maintain organized records and find matching lost and found items efficiently.

CampusFind provides a centralized web-based platform where users can:

Report lost or found items.
Search for reported items.
Filter reports by type, category, and status.
Edit or delete their reports.
Track the status of reported items.
Find possible matches between lost and found reports.

The system helps organize lost-and-found information and makes the process easier and more systematic.

## Assigned Feature Set 
Add/edit/delete lost or found reports; category selection; search/filter; matching; status tracking; AI-Based Assignment.

## Technologies
Frontend: HTML5, CSS3, JavaScript, Bootstrap 5
Backend: Python, Flask
Database: MongoDB
Libraries: Flask-PyMongo, PyMongo, Werkzeug
Tools: VS Code, Git, GitHub

## Main Features
- Registration, Login and Logout
- Password hashing
- User session authentication
- Add, edit and delete reports
- Lost/Found and category selection
- Search and filters
- Status tracking
- AI-style explainable matching
- Responsive professional UI
- MongoDB persistence

## Run on Windows
1. Install Python 3.11+ and MongoDB Community Server, or use MongoDB Atlas.
2. Open this folder in VS Code.
3. Terminal:
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```
4.#Live Demo:
5. Open: [http://127.0.0.1:5000](https://campusfind-lost-found-management-system.onrender.com)

##MongoDB:
https://localhost:27017

## GitHub Repository

https://github.com/Rohini107/CampusFind-Lost-Found-Management-System

MongoDB database/collections are created automatically after data is inserted.

## AI-Based Matching
This project uses an explainable similarity algorithm: same category, shared keywords, related location and same date contribute to a percentage score. It is not a trained ML model, which makes the feature easy to explain in a beginner viva.

## Suggested Screenshots
Home:
<img width="1897" height="957" alt="Screenshot 2026-09-18 230436" src="https://github.com/user-attachments/assets/954b2b73-cf2f-4c1d-b742-8b0515f84c6c" />

Register:
<img width="1900" height="952" alt="Screenshot 2026-09-18 220644" src="https://github.com/user-attachments/assets/10bdceb0-edcf-4693-9969-6b40191d4d1a" />

Login:
<img width="1890" height="797" alt="Screenshot 2026-09-18 220748" src="https://github.com/user-attachments/assets/d17dbd0c-fc37-4c10-a75e-48b7eb891898" />

Add Report:
<img width="1912" height="965" alt="Screenshot 2026-09-18 220247" src="https://github.com/user-attachments/assets/0dd8ac01-d94e-4b18-a0b7-ef745713085e" />

Search/Filter:
<img width="1912" height="786" alt="Screenshot 2026-09-18 220346" src="https://github.com/user-attachments/assets/35634e9d-c319-4594-bd97-ab6d606b002e" />

Edit Report:
<img width="1912" height="961" alt="Screenshot 2026-09-18 220431" src="https://github.com/user-attachments/assets/82e5abab-141e-490c-bde2-cec32962f1e6" />

Match Results:
<img width="1917" height="738" alt="Screenshot 2026-09-18 220504" src="https://github.com/user-attachments/assets/e2c3e5ca-2a2e-4bb7-b8a5-8c18e05e9682" />

MongoDB Compass collections:
<img width="1908" height="697" alt="Screenshot 2026-09-18 220541" src="https://github.com/user-attachments/assets/e075e76c-7992-4064-8043-e136d99761ae" />
<img width="1908" height="697" alt="Screenshot 2026-09-18 220541" src="https://github.com/user-attachments/assets/afed6ba7-290c-4f5b-9a93-10e861000af7" />

Logout:
<img width="1872" height="957" alt="Screenshot 2026-09-18 231455" src="https://github.com/user-attachments/assets/b240279f-ad4e-4a0c-8b09-d37cb326893b" />

## AI Usage
ChatGPT was used as a learning/development assistant for planning, code generation, debugging guidance, UI ideas, testing and documentation. The student should review, test and understand the code before submission.

## Important AI Prompts / AI Usage

The following are examples of important prompts used during development:

Project Planning

"Create a beginner-friendly full-stack Lost and Found Management System using Flask, MongoDB, HTML, CSS and JavaScript according to Feature Set B."

Backend Development

"Create Flask backend code for adding, editing, deleting and viewing lost and found reports using MongoDB."

Authentication

"Implement user registration and login in Flask using password hashing and session authentication."

Search and Filtering

"Implement search and filtering for lost and found reports based on item name, category, type, location and status."

Matching Feature

"Create an explainable similarity matching algorithm to find possible matches between lost and found items using category, keywords, location and date."

MongoDB

"Explain how to connect a Flask application to MongoDB Atlas using an environment variable."

Debugging

"Help debug the Flask MongoDB connection error and explain how to fix the database connection."

Deployment

"Guide me step-by-step to deploy my Flask application with MongoDB Atlas from GitHub to Render."

GitHub

"Explain how to safely upload the Flask project to GitHub while keeping the .env file and database credentials private."

Documentation

"Create professional README documentation for a Lost and Found Management System developed for a college assignment."
