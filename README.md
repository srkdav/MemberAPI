
<!-- PROJECT SHIELDS -->
<!-- PROJECT LOGO -->
<br />
<p align="center">
 
  <h3 align="center">Member REST API</h3>

  <p align="center">
   The REST API enables you to view Member information along with their respective activity periods.  
    <br />
    <a href="http://srkdav1994.pythonanywhere.com/">Access from PythonAnyWhere</a>
  </p>
</p>

### Built With
   * Django 3.0.8 
   * Python 3.8  
   * Sqlite3

### BackGround  
           
 There is a one to many relationship between Member and Activty Period. 
 Each Member can have multiple Activty Periods. Activity Period has a field Customer ID as the foreign key.

### Commands to run  
            
1) Clone the repository to a "Projects" folder.
2) Open the project "MemberAPI" in VSCode preferably.
3) Open terminal and ensure Python,pip are installed.
4) Down Virtual environment setup to run our project on windows.
    pip install virtualenvwrapper-win
5) Create environment
    virtualenv venv 
6) To confirm the environment is active.
    workon venv
7) Install Django.
   pip install django
8) Run the local server
   python manage.py runserver
         

The application has been deployed on PythonAnywhere :  http://srkdav1994.pythonanywhere.com/


                 
                  
