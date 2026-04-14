#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
import os

DATA_FILE = "daily-logs/progress.json"
os.makedirs("daily-logs", exist_ok=True)

def log_day(day: int, completed: str, notes: str = ""):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "day": day,
        "completed": completed.split(","),
        "notes": notes,
        "hours": 3.0
    }
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(entry)
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Día {day} guardado correctamente!")
    print(f"Completado: {completed}")
    print(f"Notas: {notes}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tracker de progreso Hacking DevSecOps")
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--completed", type=str, required=True, help="Tareas separadas por coma")
    parser.add_argument("--notes", type=str, default="")
    args = parser.parse_args()
    log_day(args.day, args.completed, args.notes)
