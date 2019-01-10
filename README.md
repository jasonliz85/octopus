# octopus
## Prerequisite
-	must have python (3.6 > ), pip and git installed
o	pip install Django
o	pip install mysqlclient
o	pip install django-tornado-websockets
o	pip install django-bootstrap3
o	pip install pycrypto
## Setup
1.	git clone git@github.com:jasonliz85/octopus.git
2.	cd octopus
3.	python manage.py migrate
4.	python manage.py runserver
a.	Server should be here: http://127.0.0.1:8000/
i.	http://127.0.0.1:8000/wordcloud -> the main word cloud page
ii.	http://127.0.0.1:8000/wordcloud/admin -> to view the counted words
## TODO
-	Configure docker-compose to prevent the setup stages
-	Configure tornado websockets to connect url routes
-	Configure mysql server setting and configurations
-	Write tests
## BUGS
-	Fix duplicate entries in the admin page



