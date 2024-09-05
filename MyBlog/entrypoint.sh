#!/bin/sh

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server 
exec gunicorn --bind 0.0.0.0:8080 MyBlog.wsgi


