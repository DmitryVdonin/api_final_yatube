# api_final
### Description
Yatube social network API. Allows you to work with the Yatube social network API: create and receive posts, subscribe to authors and get a list of your subscriptions, get a list of existing communities and their descriptions.
### Technologies
- Python 3.7
- django 2.2.16
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
- djoser 2.1.0
### Running a project in dev mode
- Install and activate the virtual environment
- Install dependencies from requirements.txt file
```
pip install -r requirements.txt
``` 
- Run the migrations. In the folder with the manage.py file, run the command:

```
 python3.manage.py migtate (windows: py.manage.py migtate)
 ```
- Start the developer server. In the folder with the manage.py file, run the command:

```
python3 manage.py runserver (windows: py manage.py runserver)
```
### Administration and Features
- Create a superuser to administer the project. In the folder with the manage.py file, run the command:

```
python3 manage.py createsuperuser (windows: py manage.py createsuperuser)
```
- The admin area is located at the relative address /admin/
- Creation of groups in the project is possible only for the administrator in the admin area
### Working with the API
- Get a token for the superuser by sending a post request to the relative endpoint api/v1/jwt/create/ passing username and password
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/jwt/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "password"
}'
```
- Sample requests for getting a post/list of posts
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/1/' \
--header 'Authorization: Bearer <your token>' \
--data-raw ''
```
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer <your token>' \
--data-raw ''
```
- An example of a post request to create a post
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer <your token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "My first post"
}'
```
- A complete list of possible endpoints and types of requests is available at the relative endpoint redoc/


### Authors
Dmitry Vdonin


