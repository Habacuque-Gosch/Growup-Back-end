# from django.test import TestCase
import requests, jsonpath


# BASE API
base_api = 'http://127.0.0.1:8000/api/v2/'
headers = {'Authorization': 'Token c239c7a97f4a6e816c77c2af28ecb990a0b2ec0c'}

# GET COURSES:
courses = requests.get(base_api + 'courses/', headers=headers)
# print(f'DATA: {courses.json()}')
print(f'STATUS CODE: {courses.status_code}')

results = jsonpath.jsonpath(courses.json(), 'results[0]')
print(results)

all_titles = jsonpath.jsonpath(courses.json(), 'results[*].title')
print(all_titles)