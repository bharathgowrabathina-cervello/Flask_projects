"""This Module contains custom management commands.
Useful for updating the seed data information & data to be inserted via deployments.
"""

import pandas as pd
import click
from flask.cli import with_appcontext,AppGroup
from udemy.lectures.models import Lecture,Section,Course
from .extensions import db
from udemy.commands_seed_data import lecturedata,sectiondata,coursedata

# creating custom command using AppGroup
command_code = AppGroup("udemy", help="udemy commands")

@command_code.command(name="lecturedata")
@with_appcontext
def lecturedatac():
    return lecturedata()

@command_code.command(name="sectiondata")
@with_appcontext
def sectiondatac():
    return sectiondata()

@command_code.command(name="coursedata")
@with_appcontext
def coursedatac():
    return coursedata()

@command_code.command(name="deploy")
@with_appcontext
def deploy():
    coursedata()
    sectiondata()
    lecturedata()
    return 



