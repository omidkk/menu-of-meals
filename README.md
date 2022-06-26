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
SQLALCHEMY_DATABASE_URI=mysql+pymysql://candidat:ur8EHudXjAVW#2rG@interview.sunbasket-dev.com:3306/sunbasket
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