#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, Student, Department, Faculty

fake = Faker()

with app.app_context():
    Student.query.delete()
    Department.query.delete()
    Faculty.query.delete()
    
    
    students = []
    for i in range(50):
        student = Student(
            name = fake.name(),
            address = fake.address(),
            phone_number = fake.country_calling_code(),
            sex = fake.text(),
            matric_number = fake.license_plate(),
        )
        students.append(student)

    db.session.add_all(students)
    db.session.commit()
    

    departments = []
    for i in range(50):
        department = Department(
            department_name = fake.name(),
            level = fake.address(),
            department_section = fake.text(),
        )
        departments.append(department)

    db.session.add_all(departments)
    
    
    faculties = []
    for i in range(50):
        faculty = Faculty(
            school = fake.name(),
            student_id = 'students.id',
            departments_id = 'departments.id'
        )
        faculties.append(faculty)

    db.session.add_all(faculties)
    db.session.commit()
 


