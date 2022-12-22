"""This Module contains custom management commands.
Useful for updating the seed data information & data to be inserted via deployments.
"""

import pandas as pd
import click
from flask.cli import with_appcontext
from udemy.lectures.models import Lecture,Section,Course
from .extensions import db

@click.command(name="lecturedata")
@with_appcontext
def lecturedata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='lecture',skiprows=1)
    list_df_lecture=df.to_dict("records")
    db.engine.execute(Lecture.__table__.insert(),list_df_lecture)
    print("Data inserted successfully")

@click.command(name="sectiondata")
@with_appcontext
def sectiondata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='section',skiprows=1)
    list_df_lecture=df.to_dict("records")
    db.engine.execute(Section.__table__.insert(),list_df_lecture)
    print("Data inserted successfully")

@click.command(name="coursedata")
@with_appcontext
def coursedata():
    df=pd.read_excel("C:/Users/gkumar01/Downloads/Tables.xlsx",sheet_name='course',skiprows=1)
    list_df_lecture=df.to_dict("records")
    db.engine.execute(Course.__table__.insert(),list_df_lecture)
    print("Data inserted successfully")
