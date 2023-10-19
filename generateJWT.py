import jwt #pyjwt
import time
import requests

secret = 'secret_key_here'
now = int(time.time())
expires = now + 300

payload = {
    'iss': 'iss_value_here',
    'iat': now,
    'exp': expires
}

token = jwt.encode(payload, secret)
print("Firstbeat Token: ",token)

refreshURL = 'https://cloud.hawkindynamics.com/api/token'
api_key = 'api_key_here'

headers = {
    'Authorization': f'Bearer {api_key}'
}

try:
    response = requests.get(refreshURL, headers=headers)

    if response.status_code == 200:
        refreshTokenData = response.json()
        refreshToken = refreshTokenData['access_token']
        print("Hawkin Dynamics Token: ", refreshToken)
    else:
        print(f"API request failed with status code {response.status_code}")
except requests.execptions.RequestException as e:
    print(f"An error occure: {e}")
