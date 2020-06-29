#!/bin/bash

set +e
echo "==> Django setup, executing: migrate pro"
python  manage.py migrate --settings=simpleapp.settings.production --fake-initial
echo "==> Django setup, executing: collectstatic"
python  manage.py collectstatic --settings=simpleapp.settings.production --noinput -v 3

gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=simpleapp.settings.production simpleapp.wsgi:application