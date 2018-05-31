import requests

url = "https://api.twitter.com/1.1/search/tweets.json"

# Modify your search query here
querystring = {"q": "#nasa", "src": "typd", "result_type": "recent"}

headers = {
    'authorization': "OAuth oauth_consumer_key=\"xxxxxx\","
                     "oauth_token=\"xxxxxx\","
                     "oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"xxxx\",oauth_nonce=\"xxxxxx\","
                     "oauth_version=\"1.0\",oauth_signature=\"xxxxxx\"",
    'cache-control': "no-cache",
    'postman-token': "xxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json)
print("************************************************")
print(response.text)
