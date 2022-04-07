import os
<<<<<<< HEAD

=======
>>>>>>> sss
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = False
# Connect to the database
<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/project"
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/project'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> sss
