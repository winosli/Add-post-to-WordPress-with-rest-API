import base64
import json
import os

import requests

# You need to add email, application password and image in this folder (name it img.jpg)
credentials = "YOUR_EMAIL@gmail.com:YOUR_APPLICATION_PASSWORD"  # You can generate application password in WordPress > Users > Profile
token = base64.b64encode(credentials.encode())
post_url = "https://www.YOUR_WEB.com/wp-json/wp/v2/posts"
media_url = "https://www.YOUR_WEB.com/wp-json/wp/v2/media"
img_name = "img.jpg"

header = {"Authorization": "Basic " + token.decode('utf-8'), "Content-Type": "application/json",
          'Content-Disposition': 'attachment; filename={}'.format(img_name)}

the_title = "YOUR TITLE"
the_description = "YOUR DESCRIPTION"

from datetime import datetime, timedelta

date_now = datetime.now() - timedelta(days=1)
# date_now =  datetime.now()
today = date_now.strftime('%Y-%m-%dT%H:%M:%S')
print("Today's date:", today)

data = open(img_name, 'rb').read()
fileName = os.path.basename(img_name)

res = requests.post(media_url,
                            data=data,
                            headers={'Content-Type': 'image/jpg',
                                     'Content-Disposition': 'attachment; filename=%s' % fileName},
                            auth=('YOUR_EMAIL@gmail.com', 'YOUR_APPLICATION_PASSWORD'))
print(res.content)

print("Upload Media ")

print(res.text)
user = json.loads(res.text)
print(user)
print("******")
print(user["id"])

# UPLOAD DATA WITH FEATURE MEDIA ID

post = {'date': today,
        'title': the_title ,
        'slug': the_title.replace(" ","-"),
        'status': 'publish',
        'content': the_description,
        'author': '1',
        'format': 'standard',
        'featured_media': user["id"]
        }

response = requests.post(post_url, headers=header, json=post, )

print(response)
