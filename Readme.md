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
```

🔗 Visit: http://127.0.0.1:8000

📌 Features
✅ POST /slots – Store busy schedules for users

✅ GET /suggest?duration=30 – Suggest earliest common free slots

✅ GET /calendar/{userId} – View a specific user’s busy and booked slots

✅ POST /book – Book a suggested time slot (optional bonus)

🧠 Reflection Questions
1. How did you use AI in this project?
I used ChatGPT for:

* Scaffolding the initial FastAPI structure
* Designing the core time conflict resolution logic
* Generating frontend templates (HTML + JS)
* Iterating quickly on endpoint behavior and debugging

Success: Rapid prototyping and clarity in structure
Challenge: Time overlap logic needed manual tweaks for edge cases

2. What would you add if you had 2 more days?
If I had more time, I would prioritize:

🗃️ Persistent database (e.g. SQLite or PostgreSQL)
🌐 Timezone support to handle users across regions
🔐 User authentication & session handling
🖱️ Interactive frontend with:
- Drag-and-drop calendar
- Click-to-book suggestions
- Real-time updates (optional WebSockets)

📂 Sample Input for /slots
```bash
{
  "users": [
    { "id": 1, "busy": [["09:00","10:30"], ["13:00","14:00"]] },
    { "id": 2, "busy": [["11:00","12:00"], ["15:00","16:00"]] }
  ]
}
```
