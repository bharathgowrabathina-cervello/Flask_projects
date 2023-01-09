Python Flask backend application for udemy project.

Run Project
To run the application locally you must have .env file in the udemy_project folder.
With current working directory as Udemyproject run -
flask run

Project Details

Directory Structure
All source code is in udemy directory.
Code is modularized based on the Feature of the application. Each feature is grouped into its own directory following the undermentioned pattern.
feature_dir
├── models.py
└── v1
    ├── __init__.py
    ├── controllers.py
    └── routes.py

File and Folders
udemy: Root directory of the project	
migrations: Flask creates a migration folder when you run a command like flask db init. You can then convert your models into migration files with a command: flask db migrate. For converting your migration files to database tables use: flask db upgrade
udemy\user: Contains all the APIs for a User workflow. Majorly Contains CRUD APIs around Lecture. Refer Postman Collection for further API documentation
udemy\commands: Contains information on custom management commands.

udemy\extensions: Flask factory pattern implementation for integrating 3rd-Party APIs.



Configurations
Development, Testing and Production configurations are separated in the udemy/config.py file. All the required environment variables are extracted from OS in udemy/config.py file and put into application config.
While development, required environment variables should be set in .env file which will be automatically loaded into the OS.



Virtual Environment
Pipenv is a dependency manager for Python projects.
Pipenv is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

Editor Configs
Visual Studio Code (VSCode) is preferred IDE for developing this project.

Postman API documentation
Postman collection Json file for API documentation can be found under the base project section.
Get Started with Postman
1.	Import the Json Collection
2.	Update the Environment vaiable: base_url
3.	Refer the API Documentation of each module for detailed information



