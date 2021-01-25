import requests
import os

base_url = 'https://redtest.ca/api/'

response = requests.post(f'{base_url}users/login/', data={'username': 'test', 'password': 'test'})
access = response.json()['access']
headers = {'Authorization': f'Bearer {access}'}
print(access)

response = requests.get(f'{base_url}users/self', headers=headers)
user_id = response.json()['id']
print(user_id)

response = requests.post(f'{base_url}users/{user_id}/git/', data={'repo': 'https://github.com/sudomakeinstall2/fuzzgoat.git',
                                               'commit': os.getenv('GITHUB_SHA')},headers=headers)

print(response.status_code)
