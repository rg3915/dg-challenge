migrate:
	python manage.py makemigrations core
	python manage.py migrate

shell_customer:
	python manage.py shell < dress/shell/shell_customer.py

shell_dress:
	python manage.py shell < dress/shell/shell_dress.py

shell_order:
	python manage.py shell < dress/shell/shell_order.py

selenium_customer:
	python dress/selenium/selenium_customer.py

selenium_dress:
	python dress/selenium/selenium_dress.py

createuser:
	python manage.py createsuperuser --username='admin' --email=''

backup:
	python manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	python manage.py loaddata fixtures.json
