runprod:
	python -m gunicorn mitraauto.asgi:application -k uvicorn.workers.UvicornWorker

dev:
	python manage.py runserver

lint:
	python -m flake8 .

format:
	python -m black .

test:
	APP_ENV=testing coverage run manage.py test

coverage:
	APP_ENV=testing coverage run manage.py test
	coverage html -d ./reports/coverage

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations
