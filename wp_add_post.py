import requests
import base64

credentials = "YOUR_EMAIL_HERE:YOUR_APPLICATION_PASSWORD" # You can generate application password in WordPress > Users > Profile
token = base64.b64encode(credentials.encode())
post_url = "https://www.YOUR_DOMAIN.com/wp-json/wp/v2/posts"

header = {"Authorization": "Basic " + token.decode('utf-8'), "Content-Type":"application/json"}

post = {'date': '2022-07-10T20:00:35',
        'title': 'First REST API post',
        'slug': 'rest-api-1',
        'status': 'publish',
        'content': 'this is the content post',
        'author': '1',
        'excerpt': 'Exceptional post!',
        'format': 'standard'
        }

response = requests.post(post_url , headers=header, json=post)
print(response.status_code)
print(response.content)