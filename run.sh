#!/bin/bash
python manage.py syncdb
python manage.py runserver 0.0.0.0:8080
