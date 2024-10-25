# Stock Simulator Backend


Clone the repository (if you haven't already):
```git clone <repository-url>```
```cd <project-directory>```

Create a virtual environment:
```python -m venv venv```

Activate the virtual environment:

```.\venv\Scripts\activate```


Install the project dependencies:
```pip install -r requirements.txt```


Database Setup
Run database migrations:
```python manage.py makemigrations```
```python manage.py migrate```

If you want to access admin panel and db:
Create a superuser:
```python manage.py createsuperuser```


Running the Project

Start the development server:
```python manage.py runserver```
The server will start, usually on http://127.0.0.1:8000/

To access the admin panel, go to http://127.0.0.1:8000/admin/ and login with the superuser credentials you created.


# API Endpoints
