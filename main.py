import requests
import sys

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
print('sys.version = {}'.format(sys.version))