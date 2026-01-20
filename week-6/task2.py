import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average"] = sum(grades) / len(grades)

with open(BASE_DIR / "students_updated.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
