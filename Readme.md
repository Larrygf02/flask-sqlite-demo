# CRUD Persons con Flask y SQLlite

Para empezar con este proyecto, se necesita instalar

* python
* virtualenv

Luego debemos seguir los siguientes pasos

```
virtualenv -p python3 .venv
pip install -r requirements.txt
```
## Despliegue en heroku

1. Procfile

```
web: gunicorn app:app
```
