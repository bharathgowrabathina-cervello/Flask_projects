from udemy.lectures.models import User,Course,Section,Lecture,LectureSchema
from flask import jsonify,request
from udemy.extensions import db
import pandas as pd

def get_lectures():

    #getting all the lectures data
   
    lectureschema=LectureSchema(many=True)
    lectures=Lecture.query.all()
    print(lectures)
    result=lectureschema.dump(lectures)

    return jsonify(result)

def add_lecture():
    """
    adding a lecture to the Lectures data
    Args:
        lecture data: json-data
    """
    data=request.get_json()
    id=data['id']
    title=data['title']
    section_id=data['section_id']
    try:
        lecture=Lecture(id=id,title=title,section_id=section_id)
        db.session.add(lecture)
        db.session.commit()
        return "lecture added successfully"
    except Exception as e:
        return "invalid lecture or lecture already exists"

def update_lecture():
    data=request.get_json()
    id=data['id']
    title=data['title']
    section_id=data['section_id']
    try:
        lecture=Lecture.query.get(id)
        lecture.title=title
        lecture.section_id=section_id
        db.session.commit()
        return "Lecture updated successfully"

    except Exception as e:
        return "invalid Lecture"

def delete_lecture():
    data=request.get_json()
    id=data['id']
    try:
        lecture=Lecture.query.get(id)
        db.session.delete(lecture)
        db.session.commit()
        return "Lecture deleted successfully"
    except Exception as e:
        return "Invalid Lecture"

def upload_lectures_data(input_sheet):
    """
    UPload the lecture data
    Args:
        excel_file (bytes): excel file with data to upload

    """
    xlsx=pd.ExcelFile(input_sheet)
    sheet_df_dict = pd.read_excel(xlsx,sheet_name=["lecture","section","course"],skiprows=1)
    df_dict=sheet_df_dict["lecture"].copy()
    list_df_lecture = df_dict.to_dict("records")
    db.engine.execute(Lecture.__table__.insert(), list_df_lecture)
    return "successfully uploaded the lecture data"