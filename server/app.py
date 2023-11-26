#!/usr/bin/env python3

from flask import Flask, request, make_response, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_cors import CORS

from models import db, Student, Department, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

CORS(app)

@app.route('/students', methods=['GET', 'POST'])
def students():

    if request.method == 'GET':
        students = []
        for student in Student.query.all():
            student_dict = student.to_dict()
            students.append(student_dict)

        response = make_response(
            students,
            200
        )

        return response

    elif request.method == 'POST':
        
        data = request.get_json()
        students = Student(
             address = data['address'],
            matric_number = data['matric_number'],
            name = data['name'],
            phone_number = data['phone_number'],
            sex = data['sex'],

        )
        db.session.add(students)
        db.session.commit()
        
        response = make_response(
            students.to_dict(),
            201
        )

        return response

@app.route('/students/<int:id>', methods = ['PATCH','DELETE'])
def students_by_id(id):
    
    students = Student.query.filter_by(id=id).first() 
    if request.method == 'PATCH':
        data = request.get_json()
        for attr in data:
            set (students, attr, data[attr])
            db.session.add(students)
            db.session.commit()
            
            response = make_response (
                students.to_dict(),
                200,
            )
            return response
        
    elif request.method == 'DELETE':
        db.session.delete(students)
        db.session.commit()
        
        response = make_response(
            {'deleted': True},
            200,
        )      
        
        return response

class student(FlaskForm):
    name = StringField("Name")
    address = StringField("Address")
    phone_number = StringField("Phone_number")
    sex = StringField("Sex")
    matric_number = StringField("Matric_number")
    submit = SubmitField("Submit")


@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    name = False
    address = False
    phone_number = False
    sex = False
    matric_number = False
    
    form = student()
    
    if form.validate_on_submit():
        name =  form.name.data
        address = form.address.data
        phone_number = form.phone_number.data
        sex = form.sex.data
        matric_number = form.matric_number.data
        form.name.data=""
        form.address.data=""
        form.phone_number.data=""
        form.sex.data="" 
        form.matric_number.data=""
        
    
    
    return render_template ("add_student.html", form=form, name = name, address = address, phone_number=phone_number,
                           sex = sex, matric_number = matric_number
                           )
 


@app.route('/departments', methods=['GET', 'POST'])
def departments():

    if request.method == 'GET':
        departments = []
        for department in Department.query.all():
            department_dict = department.to_dict()
            departments.append(department_dict)

        response = make_response(
            departments,
            200
        )

        return response

@app.route('/faculties', methods=['GET', 'POST'])
def faculties():

    if request.method == 'GET':
        faculties = []
        for faculty in Faculty.query.all():
            faculty_dict = faculty.to_dict()
            faculties.append(faculty_dict)

        response = make_response(
            faculties,
            200
        )

        return response



if __name__ == '__main__':
    app.run(port=5555, debug=True)
