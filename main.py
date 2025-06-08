from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

WORK_START = "09:00"
WORK_END = "18:00"

user_data = {}
booked_slots = []

class UserBusySlot(BaseModel):
    id: int
    busy: List[List[str]]
    
class UsersBusySlot(BaseModel):
    users: List[UserBusySlot]
    
def parse_time(t):
    return datetime.strptime(t, "%H:%M")

def format_time(t):
    return t.strftime("%H:%M")

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/slots')
def post_slots(data: UsersBusySlot):
    global users_data
    users_data = {user.id: user.busy for user in data.users}
    return {"Message": "Slots stored successfully."}
    
@app.get('/suggest')
def get_suggestions(duration: int):
    start = parse_time(WORK_START)
    end = parse_time(WORK_END)
    day_minutes = []
    
    while start + timedelta(minutes=duration) <= end:
        slot_start = start
        slot_end = start + timedelta(minutes=duration)
        
        conflict = False
        for user_id, busy_times in users_data.items():
            for busy in busy_times + booked_slots:
                busy_start = parse_time(busy[0])
                busy_end = parse_time(busy[1])
                if not(slot_end <= busy_start or slot_start >= busy_end):
                    conflict = True
                    break
            if conflict:
                break
            
        if not conflict:
            day_minutes.append([format_time(slot_start), format_time(slot_end)])
            if len(day_minutes) == 10:
                break
            
        start += timedelta(minutes=1)
    return day_minutes

@app.get("/calendar/{user_id}")
def get_calendar(user_id: int):
    return {
        "busy": users_data.get(user_id, []),
        "booked": booked_slots
    }
    
@app.post("/book")
def book_slot(slot: List[str]):
    booked_slots.append(slot)
    return {"Message": "Slot booked successfully.", "slot": slot}