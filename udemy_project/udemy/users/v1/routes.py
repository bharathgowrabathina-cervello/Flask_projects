from . import controller as c
from udemy.extensions import db,guard

from udemy.lectures.models import User,Course,Section,Lecture,LectureSchema
from flask_restx import Namespace,Resource
from flask import jsonify,request
from flask_praetorian import auth_required
import pandas as pd

open_api=Namespace("openapi")
auth_api=Namespace("authapi",
    decorators=[auth_required]
)

############ Authentication Routes ##################

@open_api.route('/login')
class Login(Resource):
    def post(self):
        json_data=request.get_json()
        username=json_data['username']
        password=json_data['password']

        user=guard.authenticate(username,password)
        token=guard.encode_jwt_token(user)
        return jsonify({"access_token":token})

@open_api.route('/signup')
class Signup(Resource):
    def post(self):
        json_data=request.get_json()
        username=json_data['username']
        password=json_data['password']
        email=json_data['email']
        firstname=json_data['firstname']
        lastname=json_data['lastname']
        phoneNo=json_data['phoneNo']
        user=User(username=username,password=guard.hash_password(password),firstname=firstname,lastname=lastname,email=email,phoneNo=phoneNo)
        db.session.add(user)
        db.session.commit()

        return "User created successfully"


################ Lecture routes ###########################

@auth_api.route('/lectures')
class Lectures(Resource):
    def get(self):
        return c.get_lectures()

    def post(self):
        return c.add_lecture()

    def put(self):
        return c.update_lecture()
    
    def delete(self):
        return c.delete_lecture()


############## endpoint to Bulk upload of Lectures API ######################

@auth_api.route('/lectures-upload')
class LectureUpload(Resource):
    def post(self):
        input_sheet=request.files.get("sheet",None)
        if not input_sheet:
            return "required parameter missing in the post body"
            # return Response.failure{
            #     400,
            #     "Input payload validation failed" ,
            #     payload={"message":"Missing required parameter in the post body"}
            # }

        return c.upload_lectures_data(input_sheet)

