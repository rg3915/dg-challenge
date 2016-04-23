migrate:
	python manage.py makemigrations core
	python manage.py migrate

shell_customer:
	python manage.py shell < shell/shell_customer.py

selenium_customer:
	python selenium/selenium_customer.py

selenium_dress:
	python selenium/selenium_dress.py

createuser:
	python manage.py createsuperuser --username='admin' --email=''

backup:
	python manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	python manage.py loaddata fixtures.json
