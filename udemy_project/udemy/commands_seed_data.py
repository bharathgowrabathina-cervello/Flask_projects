import pandas as pd
from udemy.extensions import db
from udemy.lectures.models import Lecture,Section,Course

def sectiondata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='section',skiprows=1)
    list_df_section=df.to_dict("records")
    try:
        db.engine.execute(Section.__table__.insert(),list_df_section)
        print("Data inserted successfully")
    except:
        pass

def lecturedata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='lecture',skiprows=1)
    list_df_lecture=df.to_dict("records")
    try:
        db.engine.execute(Lecture.__table__.insert(),list_df_lecture)
        print("Data inserted successfully")
    except:
        pass

def coursedata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='course',skiprows=1)
    list_df_course=df.to_dict("records")
    try:
        db.engine.execute(Course.__table__.insert(),list_df_course)
        print("Data inserted successfully")
    except:
        pass
