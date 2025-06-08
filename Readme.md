# Smart Meeting Planner 🧠📅

A lightweight FastAPI-based meeting planner that finds the earliest common free slots between users.

## 🚀 How to Run

```bash
git clone https://github.com/vivekTiw120303/smart-meeting-planner.git
cd smart-meeting-planner
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
uvicorn main:app --reload

Visit http://127.0.0.1:8000

📌 Features
/slots – Store busy schedules

/suggest?duration=30 – Suggest free time slots

/calendar/{userId} – View individual calendar

/book – Book a time slot

🧠 Reflection Questions
1. How did you use AI in this project?
Used ChatGPT to scaffold the FastAPI structure, handle time conflict logic, and generate frontend templates. Success: fast prototyping. Failure: needed tweaking of overlapping time logic.

2. What would you add if you had 2 more days?
# Persistent DB (SQLite)
# Timezone support
# User authentication
# Drag-and-drop calendar UI
