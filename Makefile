help:
	django-admin --help


mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


mak:
	python3 manage.py makemigrations

mig:
	python3 manage.py migrate

run:
	python3 manage.py runserver

cre:
	python3 manage.py createsuperuser