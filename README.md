Project : The REST API enables you to view Member information along with their respective activity periods.

Tech Stack : Dhango 3.0.8, Python 3.8 with Sqlite3.

BackGround : There is a one to many relationship between Member and Activty Period. 
            Each Member can have multiple Activty Periods. Activity Period has a field Customer ID as the foreign key.

Commands to run : 1) Clone the repository to a "Projects" folder.
                 2) Open the project "MemberAPI" in VSCode preferably.
                 2) Open terminal and ensure Python,pip are installed.
                 3) pip install virtualenvwrapper-win #virtual environment to run our project on windows.
                 4) virtualenv venv #create environment
                 5) workon venv #to confirm the environment is active.
                 5) pip install django
                 6) python manage.py runserver #run the local server
         

The application has been deployed on PythonAnywhere :  http://srkdav1994.pythonanywhere.com/


                 
                  
