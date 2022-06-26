# Menu-of-Meals
To run this project it is needed to install:

Python 3.9

Run to commend to install the requirements:

```
pip install -r requirments.py
```

It is necessary to create, and configure the **.env** file.

```
FLASK_ENV=production
FLASK_APP=start.py
SECRET_KEY=root
SQLALCHEMY_DATABASE_URI=mysql+pymysql://{username}:{password}@{host}:{port}/{dbName}
LOG_LEVEL=DEBUG
LOG_FILE=menu-meals.log
```

To run the flask app:
```
python start.py
```
---------
To run with docker:
```
docker build -t menu-of-meal .
docker run --env-file .env -d -p 5001:5001 menu-of-meal
```
---------

Links:

Swagger
```
{base_url}:{port}/v1/docs

example:
http://127.0.0.1:5001/v1/docs
```

Health
```
{base_url}:{port}/v1/health

example:
http://127.0.0.1:5001/v1/health
```

Menu
```
{base_url}:{port}/v1/menu/{YYYY-MM-DD}/{type}

example:
http://127.0.0.1:5001/v1/menu/2021-03-03/MEAL_KIT
```
