from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#Similar to (from math import sqrt)

app = FastAPI(
    title="Student API",
    description="Student management system",
    version="1.0.0",
    summary="Demo API"
)
#Similar to car = Car() <- This is declaration of a class and storing in a variable

#GET - GET AN INFORMATION
#POST - CREATE SOMETHING NEW
#PUT - UPDATE
#DELETE - DELETE SOMETHING

students = {
  1: {
    'name': 'A',
    'age': 2,
    'year': 1999
  },
  2: {
    'name': 'B',
    'age': 3,
    'year': 2000
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: int

class UpdateStudent(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = None
  year: Optional[int] = None


@app.get("/") 
def index():
  return {"name":"First DATA"}
'''
  Above code tells what fastAPI should do when browser performs GET function.
  So here when GET function is called by browser,  if at main page -> indicated by / -> perform index function
'''

@app.get("/get-student/{student_id}")
def get_student(student_id : int):
  return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
  for student_id in students:
    if students[student_id]["name"] == name:
      return students[student_id]
  return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
  if student_id in students:
    return {"Error": "Student exists"}
  students[student_id] = student
  return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
  if student_id not in students:
    return{"Error": "Student exists"}
  if student.name != None:
    students[student_id]["name"] = student.name
  if student.age != None:
    students[student_id]["age"] = student.age
  if student.year != None:
    students[student_id]["year"] = student.year
  return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
  if student_id not in students:
    return {"Error": "student does not exist"}
  del students[student_id]
  return {"Student": "Deleted"}