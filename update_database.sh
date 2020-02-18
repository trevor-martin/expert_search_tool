#!/bin/bash
echo "Start makemigrations: python manage.py makemigrations"
python manage.py makemigrations

echo "Start migrate: python manage.py migrate"
python manage.py migrate

