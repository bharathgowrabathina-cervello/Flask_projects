"""Controller Logic for User and Lectures Module
"""

from udemy.lectures.models import User,Course,Section,Lecture,LectureSchema
from flask import jsonify,request
from udemy.extensions import db,cache
import pandas as pd
import redis


import logging



FLASK_CACHE="flask_cache_get_lectures"
FLASK_CACHE=FLASK_CACHE.upper()

def get_lectures():

    """List all the lectures
    Args:
        args (dict): pagination and filter information
    Returns:
        list :  lectures information serialised as json
    """
    logging.info("Trying to access lectures data")

    result=cache.get("get_lectures")
    if result is not None:
        logging.info('accessed the lectures data')
        return result

    lectureschema=LectureSchema(many=True)
    lectures=Lecture.query.all()
    result=lectureschema.dump(lectures)
    cache.set("get_lectures",result,0)
    logging.info('accessed the lectures data')
    return jsonify(result)

def add_lecture():
    """
    adding a lecture to the Lectures data
    Args:
        lecture data: json-data
    Returns:
        str : Status of adding lecture
    """
    data=request.get_json()
    id=data['id']
    title=data['title']
    section_id=data['section_id']
    try:
        lecture=Lecture(id=id,title=title,section_id=section_id)
        db.session.add(lecture)
        db.session.commit()
        cache.clear()
        logging.info("new lecture added")
        return jsonify({"message":"lecture added successfully"})
    except Exception as e:
        response={"message":"invalid lecture or lecture already exists"}
        return response,400


def update_lecture():
    """Update an existing lecture
    Args:
        args (dict): lecture information
    Returns:
        object (dict) : updated lecture information object
    """
    
    data=request.get_json()
    id=data['id']
    title=data['title']
    section_id=data['section_id']
    try:
        lecture=Lecture.query.get(id)
        lecture.title=title
        lecture.section_id=section_id
        db.session.commit()
        cache.clear()
        logging.info("lecture has updated")
        return jsonify({"message":"Lecture updated successfully"})

    except Exception as e:
        return jsonify({"message":"invalid Lecture"})

def delete_lecture():
    """Delete existing lecture
    Args:
        lecture_id : id of the lecture to be deleted
    Returns:
        str : Status of deletion
    """
    
    data=request.get_json()
    id=data['id']
    try:
        lecture=Lecture.query.get(id)
        db.session.delete(lecture)
        db.session.commit()
        cache.clear()
        logging.info("lecture has deleted")
        return jsonify({"message":"Lecture deleted successfully"})
    except Exception as e:
        return jsonify({"message":"Invalid Lecture"})

def upload_lectures_data(input_sheet):
    """
    UPload the lecture data
    Args:
        excel_file (bytes): excel file with data to upload
    Returns:
        str : Status of uploading bulk lectures data
    """
    xlsx=pd.ExcelFile(input_sheet)
    sheets_df_dict = pd.read_excel(xlsx,sheet_name=["course","section","lecture"],skiprows=1)
    
    try:

        upload_sheet(sheets_df_dict["course"], Course)
        upload_sheet(sheets_df_dict["section"], Section)
        upload_sheet(sheets_df_dict["lecture"], Lecture)
        
        # df_dict=sheet_df_dict["lecture"].copy()
        # list_df_lecture = df_dict.to_dict("records")
        # db.engine.execute(Lecture.__table__.insert(), list_df_lecture)
        return jsonify({"message":"successfully uploaded the lecture data"})

    except Exception as e:
        return jsonify({"message":"unable to upload"})


def upload_sheet(input_sheet,table):    
    df_dict=input_sheet
    list_df_table=df_dict.to_dict("records")
    db.engine.execute(table.__table__.insert(),list_df_table)
    












