import requests as req
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")

# Test Dict
url_data = {
    'baseurl': 'https://api.twitter.com',
    'endpoints': {
        'tweetsby': {
            'ep': '/2/users/by',
            'params': ['ids'],
            'expansions': {},
            'fields': {}
        }
    }
}

userid = 1161639845531455489

print(userid)
print(bearer)

print(url_data['baseurl']+url_data['endpoints']['tweetsby']['ep']+"?ids="+"Ledger_support")
headers = {"Authorization": f"Bearer {bearer}"}

print(req.get(url_data['baseurl']+url_data['endpoints']['tweetsby']['ep']+"?usernames="+"Ledger_support", headers=headers).json())

class twitterBot:
    def __init__(self, auth, userid) -> None:
        """
        :param auth: dict The parameters for authentication will be placed inside the auth, as a dictionary
        :param userid: str
        """
        pass

    # First function for class is to create a list of tweets that we are "watching"
    def get_list(self) -> dict:
        
        return {}