# Event Scheduling & Resource Allocation System

A full-stack web application that allows organizations to create events, manage shared resources, and prevent scheduling conflicts through backend-enforced validation.

This project focuses on **correct conflict detection**, **dynamic data handling**, and **clear user feedback**, making it suitable for real-world scheduling scenarios.

---

## 🚀 Features

### Event Management
- Create events with title, start time, end time, and description
- Automatic validation for invalid time ranges
- Dynamic event ID generation

### Resource Management
- Create shared resources (rooms, instructors, equipment)
- Dynamic resource ID generation
- Input validation with user-friendly error messages

### Resource Allocation
- Allocate resources to events
- Backend-enforced conflict detection
- Prevents double-booking of resources
- Clear error messages displayed in the UI

### Conflict Detection
- Detects overlapping time intervals
- Handles edge cases:
  - Partial overlaps
  - Fully nested intervals
  - Exact boundary conditions (end = start allowed)
- Implemented at the backend level for reliability

### Resource Utilization Report
- Generate reports for a selected date range
- Displays total hours each resource is utilized
- Computed dynamically based on current data

---

## 🧠 Conflict Detection Logic

A resource conflict is detected using the following rule:

existing_event.start_time < new_event.end_time
AND
existing_event.end_time > new_event.start_time

yaml
Copy code

If this condition is true for the same resource, the allocation is rejected.

This logic correctly handles all overlapping scenarios and avoids false positives.

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy (ORM)
- SQLite (Database)

### Frontend
- HTML
- Bootstrap 5
- Vanilla JavaScript (Fetch API)

---

## 📁 Project Structure

Event-Scheduling-System/
│
├── backend/
│ ├── app.py
│ ├── database.py
│ ├── models.py
│ ├── routes/
│ │ ├── events.py
│ │ ├── resources.py
│ │ ├── allocations.py
│ │ └── reports.py
│
├── frontend/
│ ├── templates/
│ │ ├── index.html
│ │ ├── events.html
│ │ ├── resources.html
│ │ ├── allocate.html
│ │ └── report.html
│
├── .gitignore
└── README.md


## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/event-scheduling-system.git
cd event-scheduling-system
2️⃣ Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
Mac/Linux

bash
Copy code
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install Flask Flask-SQLAlchemy python-dateutil
4️⃣ Run the Application
bash
Copy code
cd backend
python app.py
The application will run at:

cpp
Copy code
http://127.0.0.1:5000/
🧪 Sample Usage Flow
Create a resource (e.g., Room A)

Create an event with start and end time

Allocate the resource to the event

Try allocating the same resource to another overlapping event

Observe the conflict error displayed in the UI

Generate a utilization report for a selected date range

🎯 Design Decisions
Conflict detection is enforced at the backend, not the UI

SQLite is used for simplicity and quick setup

ORM-based database access for cleaner and safer queries

UI kept lightweight to emphasize backend correctness

🔮 Future Enhancements
Dropdown-based resource and event selection

Authentication and role-based access

Calendar-based event visualization

Detailed conflict explanation in UI

Migration to PostgreSQL or MySQL

```
Output Screenshots:

<img width="1917" height="970" alt="image" src="https://github.com/user-attachments/assets/336fe15a-d2a7-4e4b-9925-06dcbd34e94a" />

<img width="1915" height="976" alt="image" src="https://github.com/user-attachments/assets/4faa11b1-4f91-4238-b817-189b2ce0f671" />

<img width="1919" height="966" alt="image" src="https://github.com/user-attachments/assets/98119084-2b6d-454f-b1a0-755db7e4924b" />

<img width="1912" height="970" alt="image" src="https://github.com/user-attachments/assets/e2b2f1fc-70ac-416e-a406-c6e69dfa5e29" />

<img width="1918" height="971" alt="image" src="https://github.com/user-attachments/assets/48ec5d3a-4382-4dd6-820a-f9b62f8eaaeb" />


