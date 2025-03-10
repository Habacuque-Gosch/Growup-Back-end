# from django.test import TestCase
import requests


# BASE API
base_api = 'http://127.0.0.1:8000/api/v2/'

# GET COURSES:

courses = requests.get(base_api + 'courses/').json()
print(courses)
