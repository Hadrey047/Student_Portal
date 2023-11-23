#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Student, Department

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


# class Home(Resource):
    
#     def get(self):

#         response_dict = {
#             "message": "Welcome to the Newsletter RESTful API",
#         }

#         response = make_response(
#             response_dict,
#             200
#         )

#         return response

# api.add_resource(Home, '/')

# @api.route('/students')

# class Student(Resource):

#     def get(self,):

#         response_dict_list = [n.to_dict() for n in Student.query.all()]

#         response = make_response(
#             response_dict_list,
#             200,
#         )

#         return response

    # def post(self):
    #     # new_record = Student(
    #     #         name=request.form['name'],
    #     #         address=request.form['address'],
    #     #         phone_number=request.form['phone_number'],
    #     #         sex=request.form['sex'],
    #     #         matric_number=request.form['matric_number'],
    #     #         address=request.form['address'],
    # # )
    
    # db.session.add(new_record)
    # db.session.commit()

    # response_dict = new_record.to_dict()

    # response = make_response(
    #     response_dict,
    #     201,
    # )

    # return response

# api.add_resource(Student,'/students')

# class NewsletterByID(Resource):

#     def get(self, id):

#         response_dict = Newsletter.query.filter_by(id=id).first().to_dict()

#         response = make_response(
#             response_dict,
#             200,
#         )

#         return response

# api.add_resource(NewsletterByID, '/newsletters/<int:id>')'

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

if __name__ == '__main__':
    app.run(port=5555, debug=True)
