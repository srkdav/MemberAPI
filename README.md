
<!-- PROJECT SHIELDS -->
<!-- PROJECT LOGO -->
<br />
<p align="center">
 
  <h3 align="center">Member REST API</h3>

  <p align="center">
   The REST API enables you to view Member information along with their respective activity periods.  
    <br />
    <a href="http://srkdav1994.pythonanywhere.com/">Access from PythonAnywhere</a>
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
4) pip install virtualenvwrapper-win #virtual environment to run our project on windows.
5) virtualenv venv #create environment
6) workon venv #to confirm the environment is active.
7) pip install django
8) python manage.py runserver #run the local server
         

The application has been deployed on PythonAnywhere :  http://srkdav1994.pythonanywhere.com/


                 
                  
