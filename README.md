# How to add cyderian fuzz testing to your CI/CD

First create a file with the path `.github/workflows/`. You can call this file `fuzztest.yaml`.

Add a job to send a fuzzing request by adding the following content `fuzztest.yaml`:

```yaml
name: Cyderian

on: [push]

jobs:
  fuzztest:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests
    - name: sending requests
      env:
        CYDERIAN_USERNAME: ${{ secrets.CYDERIAN_USERNAME }}
        CYDERIAN_PASSWORD: ${{ secrets.CYDERIAN_PASSWORD }}
      run: |
        python .github/cyd.py
```

In this job first we install requests package for python and then we run a script that authenitcates the project with the api and send a fuzz request to the server.

Next step is to add the script. Create a file in the path `.github/cyd.py` and copy the following content into it:

```python3
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

response = requests.post(f'{base_url}users/{user_id}/git/', data={'repo': 'https://github.com/sudomakeinstall2/fuzzgoat.git',
                                               'commit': os.getenv('GITHUB_SHA')},headers=headers)

print(response.status_code)
```

The final step is to create secret values for your cyderian credentials. Go to your secrets page of your project and add `CYDERIAN_USERNAME`, `CYDERIAN_PASSWORD` with proper values.

Now you should be able to run fuzztest on every push on the repository.
