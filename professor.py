import os
import requests
import random
from uuid import uuid4
import json
from user_agent import generate_user_agent
uid = uuid4()
P_W_7=str(uuid4())

print('---------TooL professor ----------')
def az():
 while True:
  user='1234567890_.qwertyuiopasdfghjklzxcvbnm'
  num='123456'
  rng=int("".join(random.choice(num)for i in range(1)))
  ing=str("".join(random.choice(user)for i in range(rng)))
  useq='instaup'+ing
  url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={useq}&rank_token=0.38549261586414585&include_reel=true'
  hes = {
		        'accept': '*/*',
		        'accept-encoding': 'gzip, deflate, br',
		        'accept-language': 'en-US,en;q=0.9',
		        'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=B5EvgsGegpjkHbwakmeZzZeibMUyPXOo; ds_user_id=479320179; sessionid=479320179:YJP7Mp7LRlvDVe:17; shbid="6887\054479320179\0541685041134:01f78226f1ed25a1fd638da513ee9fc0bd85ad7b75335c66e00546dddc526839ed8673b3"; shbts="1653505134\054479320179\0541685041134:01f7359bb436c3c2a6a593d450045a6d47feeeb49309f4e3e34f16846a86521cd654f96c"; fbsr_124024574287414=-t_KkO2zVCJ8dtHJUTSp1hNWF4FvrBOMic2GrdYXfXo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQmtRTDJLM0F6eC1NYUE5blBMQ3lrYXBONFVQYUU4RDJ3cG1GcmlJTjFqN0x4aVU1UWdtekFGcDEwaEtHZ2Y3RUdhY3VFNFBFMDdwN0VNWUtnTFVyT0lPbGNLN3BBWEExVDBCbjRtTnI2bVFSbFpBY0tuOWp4ZS1HNGd3QVk2bUZwdmZoeXVHeXV5U09ZcWtIVW83VWM3V1ZFUTdERG4wQU16dDN6WmVxckxYOGhVMXE2WnRqbEhvMlQwdVRHQzZ0SXpWak4wT3otNjUyU2pkQVRLbmZBcmM1MkEzeVQ2c0JmbGZUX2M3alQ4TWZuZU02b3NQcmZuTF9CVnptbWp4eVBYbm85alRDRUMyRzNGLWgyNE5Ua0Y4NkVZbDRFR1Q0NExqQkl3NnZfekdHYW5MckF3Q3dMVUJMMF81Mzd3bDlnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ5SmR4WTE5T0t5M1pDQlpBTkJqaWc5d0M0bTlqSVdUZHdWVTdJa01PTjBXVkZ2ZXVpSE4waHZTamF4cXpaQTJxWkJzVXR6cXBMWkNwYzJNYzVJS0lUVW5DMHJNWWZuVDRVRVFhYWhaQ2JKZm03bEQ1Q1hNdE14bGVyV2FFRGZrT2U2Y0RSSmg2OWFtZlV4eGFVRmFHMGlkRHR3VnJZNXo1VzVMZ0U5Q2UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MzUwNjE1NH0; rur="ASH\054479320179\0541685042266:01f7314545b2fc6431250d9f16c78ee257c43ef7fffb40f551f9109cef47d42ed774d508"',
		        'referer': 'https://www.instagram.com/explore/search/',
		        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		        'sec-ch-ua-mobile': '?0',
		        'sec-fetch-dest': 'empty',
		        'sec-fetch-mode': 'cors',
		        'sec-fetch-site': 'same-origin',
		        'user-agent': str(generate_user_agent()),
		        'x-asbd-id': '437806',
		        'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
		        'x-ig-app-id': '936619743392459',
		        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
		        'x-requested-with': 'XMLHttpRequest'
}

  rr = requests.get(url, headers=hes).json()
  mn=0
  try:
   while True:
        mn += 1
        id=(rr['users'][mn]['user']['pk_id'])
        co=requests.get(f'http://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={id}').json()['return']['coins']
        print(f'id : {id} : Coin : {co}')
  except IndexError:
  	print('bad')
  	az()
  except KeyError:
  	az()
az()
