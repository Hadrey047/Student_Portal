from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy()


class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    phone_number = db.Column(db.Integer())
    sex = db.Column(db.String())
    matric_number = db.Column(db.String()) 
    
    
    departments = db.relationship('Department', backref='student')
    
    def __repr__(self):
        return f'<Student {self.name},{self.address},{self.phone_number},{self.sex},{self.matric_number}.>'


class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'

    serialize_rules = ('-students')

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(40))
    level = db.Column(db.String(10))
    department_section = db.Column(db.String(30))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
     
     
    def __repr__(self):
        return f'<Department This student is from {self.department_name}{self.level}{self.department_section}>'
    
class Faculty(db.Model, SerializerMixin): 
    __tablename__ = 'faculties'

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(60))
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    departments_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    
   
   
    def __repr__(self):
        return f'Faculty {self.school}'
    