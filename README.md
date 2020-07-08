
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
 Each Member can have multiple Activty Periods. Activity Period has a field Customer ID as the foreign key. Hence, it is pertinent that the Customer details are sent
 by POST method and THEN Activity period data is sent by POST due to the FK constraint.

### Commands to run  
            
1) Clone the repository to a "Projects" folder.
2) Open the project "MemberAPI" in VSCode preferably.
3) Open terminal and ensure Python,pip are installed.
4) Down Virtual environment setup to run our project on windows.
    -> pip install virtualenvwrapper-win
5) Create environment
    -> virtualenv venv 
6) To confirm the environment is active.
    -> workon venv
7) Install Django.
   -> pip install django
8) Run the local server
   -> python manage.py runserver
 
### Process to get the Json data in desired format
1) Sample Data for customers and acitvity period has been given in the customer_sample_data.json and acitivty_sample_data.json files.
2) Please POST the data from customer : "http://localhost:8000/customer/" and then from activty :"http://localhost:8000/activity/" using POSTMAN.
3) During the GET request from customer: "http://localhost:8000/customer/" , data will be received in the format as asked.


The application has been deployed on PythonAnywhere :  http://srkdav1994.pythonanywhere.com/


                 
                  
