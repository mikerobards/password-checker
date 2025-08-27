import requests

url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'
response = requests.get(url)
print(response.text)
