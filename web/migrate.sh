#!/bin/bash
DJANGO_SUPER_USER_EMAIL=${DJANGO_SUPER_USER_EMAIL:-'admin@admin.com'}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email "$DJANGO_SUPER_USER_EMAIL" --noinput || true


