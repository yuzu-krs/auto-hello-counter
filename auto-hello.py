import requests
import json

url='http://127.0.0.1:50021/'

text='こんにちは'

speaker_id=1

item_data={}

res=requests.post(url+'audio_query',params=item_data)

res_join=res.json()

print(res_join)

query_data=json.dumps(res_join)
a_params={
}
res=requests.post(url+'synthesis',params=a_params,data=query_data)
print(res.content)