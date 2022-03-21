# django-rest

## Requirements
- Python 3.8


## Installation
0. Setup virtual environment
1. Install Python dependencies
```
# for production
pip install -r requirements-prod.txt

# for development & testing
pip install -r requirements.txt
```

2. copy and configure env variables to match your setup
```
# using .env file
cp .env.example .env
```

3. Run migration and load initial data
```
python manage.py migrate
python manage.py loaddata --app apps.geolocation geo_locations_id.json 
```

4. Run local server
```
python manage.py runserver
```

6. (Production) Run server with gunicorn
```
python -m gunicorn mitraauto.asgi:application -k uvicorn.workers.UvicornWorker
```

## Testing

1. Run test
```
APP_ENV=testing manage.py test

# using Makefile
make test
```

2. Run test with coverage
```
APP_ENV=testing coverage run manage.py test

# using Makefile
make coverage
```

3. Generate coverage output as HTML
```
coverage html
```
