runprod:
	python -m gunicorn mitraauto.asgi:application -k uvicorn.workers.UvicornWorker

dev:
	python manage.py runserver

lint:
	python -m flake8 mitraauto/

format:
	python -m black mitraauto/

test:
	coverage run manage.py test

coverage:
	coverage run manage.py test
	coverage html

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations
