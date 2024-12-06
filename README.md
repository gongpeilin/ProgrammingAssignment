# ProgrammingAssignment

##### URL to access web app####################

http://ec2-47-129-244-133.ap-southeast-1.compute.amazonaws.com


###### URL to download the source code in Github########

https://github.com/gongpeilin/ProgrammingAssignment.git

#### Introduciton ####

This project utilize the Django framework to buit one cafe app to check the menu and make the reservation.

To run it locally, you may follow the belwo steps:

1) set up the Django virutal enviroment and activate it
2) pip install -r requirements.txt , to install the required pyton libaray, inlcuding Django. 
    You can find the requirements.txt in the root folder.
3) for data sensitive, i didn't upload the database file: sqlite in Github, you may run the python manage.py migrate
    to rebuilt the related tables.
4) once it is ready, you can access to folder: assignment and run the command: python manage runserver to access it locally.