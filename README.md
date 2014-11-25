project-6-group-15
==================
Functional testing on imageApp
The functional testing provided was based off of the TA's project sample solution- ImageSpace app

(First few steps is the same as TA's)
Make sure you have installed python 2.7, postgresql and pip
Setting up server and Running server:

1.	Create virtual environment and activate it. Then run pip install -r requirements.txt
2.	In command line run export DATABASE_URL='postgresql://127.0.0.1:5432/database_name'replacing database name with corresponding value. (Change port and host if necessary)
3.	Run migrations. python manage.py migrate
4.	Run django server. python manage.py runserver
5.	Your application will be available at http://127.0.0.1:8000

To run Tests:
1.	Run python manage.py test imageapp

To run functional tests:
1. Run harvest. python manage.py harvest

To get test coverage
1.	Run test with python manage.py test imageapp
2.	Run coverage report
