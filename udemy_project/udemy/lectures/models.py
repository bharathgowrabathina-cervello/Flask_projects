from udemy.extensions import db,ma
from flask_marshmallow import fields

# Third party imports
from sqlalchemy import (
    Column,
    DECIMAL,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    NVARCHAR,
    BigInteger
)
  
class User(db.Model):
    username = db.Column(db.String(80),primary_key=True)
    password = db.Column(db.Text)    
    firstname=db.Column(db.Text)
    lastname=db.Column(db.Text)
    email=db.Column(db.String(50),unique=True,nullable=False)
    phoneNo=db.Column(db.BigInteger)

    def __repr__(self):
        return '<Users %r>' % self.username

    @classmethod
    def lookup(cls,username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls,username):
        return cls.query.get(username).one_or_none()

    # properties and methods required by Praetorian
    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return  self.username


class Course(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    section=db.relationship('Section',backref='course', cascade='all, delete, delete-orphan')

class Section(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    course_id=db.Column(db.Integer,db.ForeignKey(Course.id),nullable=False)
    lecture=db.relationship('Lecture',backref='section', cascade='all, delete, delete-orphan')

class Lecture(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50))
    section_id=db.Column(db.Integer,db.ForeignKey(Section.id),nullable=False)

#schema to serialize the lectures data
class LectureSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model=Lecture
