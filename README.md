# Requirements for the application
  pyhton3 , pip3 , postgressql database, PostgreSQL 14.2

# Steps to install the application:
1. Create venv in python3
   python3 -m venv shivamproject

2. change directory to project folder
   cd shivamproject

3. activate venv
   . bin/activate

4. install the required pip pakages
   pip install -r requirements.txt

5. export the flask env variables
   export FLASK_APP=app.py
   export FLASK_ENV=development

6. run the flask app on port 80
   flask run --host 0.0.0.0 --port 80
7. shivam is king
