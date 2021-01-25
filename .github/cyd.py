import requests

base_url = 'https://redtest.ca/api/'

response = requests.post(f'{base_url}users/login/', data={'username': 'test', 'password': 'test'})
access = response.json()['access']
headers = {'Authorization': f'Bearer {access}'}
print(access)

response = requests.get(f'{base_url}users/self', headers=headers)
user_id = response.json()['id']
print(user_id)

response = requests.post(f'{base_url}users/{user_id}/git/', data={'repo': 'https://github.com/sudomakeinstall2/fuzzgoat.git',
                                               'commit': '7b89cc8598721efb888251476cafb982d84b65db'},headers=headers)

print(response.status_code)
