#!/bin/sh

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server using gunicorn on port 8080
exec gunicorn --bind 0.0.0.0:8080 MyBlog.wsgi


