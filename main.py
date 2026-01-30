# task 2
from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)

@app.get('/')
async def hello_world():
    return 'Hello, World!'

# task 3
@app.get('/students')
async def get_students():
    return data

# task 4
@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id:
      return student
    
# task 5
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
              filtered_students.append(student)
        return filtered_students
    return data


# exercise 1
@app.get('/stats')
async def generate_stats():
    chicken_count = 0
    fish_count = 0
    vege_count = 0
    cs_major_count = 0
    cs_special_count = 0
    it_major_count = 0
    it_special_count = 0

    for student in data:
        if student['pref'] == 'Chicken':
            chicken_count += 1
        elif student['pref'] == 'Fish':
            fish_count += 1
        elif student['pref'] == 'Vegetable':
            vege_count += 1
            
        if student['programme'] == 'Computer Science (Major)':
            cs_major_count += 1
        elif student['programme'] == 'Computer Science (Special)':
            cs_special_count += 1
        elif student['programme'] == 'Information Technology (Major)':
            it_major_count += 1
        elif student['programme'] == 'Information Technology (Special)':
            it_special_count += 1
        
    return{
        "Chicken": chicken_count,
        "Fish": fish_count,
        "Vegetable": vege_count,
        "Computer Science (Major)": cs_major_count,
        "Computer Science (Special)": cs_special_count,
        "Information Technology (Major)": it_major_count,
        "Information Technology (Special)": it_special_count,
    }

# exercise 2
@app.get('/add/{a}/{b}')
async def add(a:int, b:int):
    return a + b

@app.get('/subtract/{a}/{b}')
async def add(a:int, b:int):
    return a - b

@app.get('/multiply/{a}/{b}')
async def add(a:int, b:int):
    return a * b

@app.get('/divide/{a}/{b}')
async def add(a:int, b:int):
    return a / b