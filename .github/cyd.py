import requests
import os

base_url = 'https://redtest.ca/api/'

response = requests.post(f'{base_url}users/login/', data={'username': os.getenv('CYDERIAN_USERNAME'), 'password': os.getenv('CYDERIAN_PASSWORD')})
access = response.json()['access']
headers = {'Authorization': f'Bearer {access}'}
print(access)

response = requests.get(f'{base_url}users/self', headers=headers)
user_id = response.json()['id']
print(user_id)

response = requests.post(f'{base_url}users/{user_id}/git/', data={'repo': os.getenv('GIT_REPO'),
                                               'commit': os.getenv('TRAVIS_COMMIT')},headers=headers)

print(response.status_code)
