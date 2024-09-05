from django.test import TestCase
import environ

env = environ.Env()
environ.Env.read_env()

print("SECRET_KEY:", env('SECRET_KEY', default='not_found'))

# Create your tests here.
