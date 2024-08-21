db:
	python manage.py makemigrations
	python manage.py migrate
server:
	python manage.py runserver

reset:
	python manage.py migrate relationship_app zero
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	python manage.py makemigrations
	python manage.py migrate
weka:
	git add .
	git commit -m "updates"
	git push