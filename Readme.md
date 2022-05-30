# CRUD Persons con Flask y SQLlite

Para empezar con este proyecto, se necesita instalar

* python
* virtualenv

Luego debemos seguir los siguientes pasos

```
virtualenv -p python3 .venv
pip install -r requirements.txt
python app.py
```
## Despliegue en heroku

1. Conectar su aplicacion heroku con github

![alt text](https://github.com/larrygf02/flask-sqlite-demo/blob/master/public/heroku-github.PNG?raw=true)


2. Procfile

```
web: gunicorn app:app
```
