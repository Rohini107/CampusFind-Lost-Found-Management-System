# CampusFind — Lost & Found Management System

## Assigned Feature Set B
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
4. Open http://127.0.0.1:5000

For Atlas, set:
```powershell
$env:MONGO_URI="YOUR_ATLAS_CONNECTION_STRING"
```

Default local database:
`mongodb://localhost:27017/campusfind`

MongoDB database/collections are created automatically after data is inserted.

## AI-Based Matching
This project uses an explainable similarity algorithm: same category, shared keywords, related location and same date contribute to a percentage score. It is not a trained ML model, which makes the feature easy to explain in a beginner viva.

## Suggested Screenshots
Home, Register, Login, Add Report, Search/Filter, Edit Report, Match Results, MongoDB Compass collections, Logout.

## AI Usage
ChatGPT was used as a learning/development assistant for planning, code generation, debugging guidance, UI ideas, testing and documentation. The student should review, test and understand the code before submission.

## GitHub
Create a repository, upload the complete project including README.md, and submit the repository link as required by the assignment.
