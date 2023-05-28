import requests
import tweepy

client = tweepy.Client(consumer_key="YOUR_API_KEY",
                    consumer_secret="SECRET_API_KEY",
                    access_token="YOUR_ACCESS_TOKEN",
                    access_token_secret="SECRET_ACCESS_TOKEN")

limit = 3
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'wo/03o2osEKKHeMABwfvxg==abgstFHoi6bdbdkh'}).json()

joke = response[0]["joke"]
client.create_tweet(text = joke)



