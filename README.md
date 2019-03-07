# platforma-edu

A portal for the institute to facilitate Interaction between students and teachers to solve course related queries. Features include news feed, custom notifications, course forum for discussions, assignments upload and download and file sharing. 

#### Teacher view

![command_open](https://github.com/krzyrad/platforma-edu/blob/master/images/t_1.png)

![command_open](https://github.com/krzyrad/platforma-edu/blob/master/images/t_2.png)


#### Student View

![command_open](https://github.com/krzyrad/platforma-edu/blob/master/images/s_1.png)

![command_open](https://github.com/krzyrad/platforma-edu/blob/master/images/s_2.png)

## Requirements

- Python 3.x
- Django 1.11.6

## Procedure

Clone this repository and then

- First install a virtual environment with command
```
    $ virtualenv portalenv 
    $ source portalenv/bin/activate
    $ pip install -r requirements.txt
```
- Just do migration for the app from project root.

```
    $ python manage.py migrate
```
### Creating users

- Admin can be created using this command. 
```
   $ python manage.py createsuperuser
```
after that run server locally with following command 
```
   $ python manage.py runserver
```

Visit <http://localhost:8000/admin> in the browser to add few students & teachers.
