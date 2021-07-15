import requests    #pip install requests

#404 --> Not Found
#200 --> OK

response = requests.get("http://ip-api.com/json/176.240.172.93")

print(response)
print(response.json())