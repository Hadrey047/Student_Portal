from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    phone_number = db.Column(db.Integer())
    sex = db.Column(db.String())
    matric_number = db.Column(db.String())
    

    def __repr__(self):
        return f'<Student {self.name},{self.address},{self.phone_number},{self.sex},{self.matric_number}.>'


class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String())
    level = db.Column(db.String())
    department_section = db.Column(db.String())
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

     
    def __repr__(self):
        return f'<Department This student is from {self.department_name}{self.level}{self.department_section}>'
    
    class Faculty(db.Model):
     __tablename__ = 'faculties'

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String)
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    departments_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
    
    