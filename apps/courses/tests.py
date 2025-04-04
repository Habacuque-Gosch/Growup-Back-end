import requests

class TestCourses:
    
    # BASE API URL
    base_api = 'http://127.0.0.1:8000/api/v2/courses/'
    headers = {'Authorization': 'Token c239c7a97f4a6e816c77c2af28ecb990a0b2ec0c'}

    def test_get_all_courses(self):
        results = requests.get(url=self.base_api, headers=self.headers)
        assert results.status_code == 200