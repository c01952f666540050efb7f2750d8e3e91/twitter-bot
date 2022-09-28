import requests as req
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

# Universal immutables
baseurl = 'https://api.twitter.com'

epdata = {
    'getTweets': {
        'method': 'GET',
        'ep': '/2/tweets'
    },
    'postTweet': {
        'method': 'POST',
        'ep': '/2/tweets'
    },
    'deleteTweet': {
        'method':  'DELETE',
        'ep': '/2/tweets'
    },
    'getUserTweets': {
        'method': 'GET',
        'ep': '/2/users/:id/tweets'
    },
    'getUserMentions': {
        'method': 'GET',
        'ep': '/2/users/:id/mentions'
    },
    'getIdByUser': {
        'method': 'GET',
        'ep': ''
    }
}

def epInfo(epType) -> dict:
        return epdata[epType]


# Request Builder
class reqBuilder:
    def __init__(self, subject, bearer) -> None:
        self.subject = subject
        self.bearer = bearer

        # Things that we replace
        self.replace = {
            ':id': self.subject,
        }

        # Specific Auth Types
        self.bearer_auth = {"Authorization": f"Bearer {bearer}"}

    # Injection of data into Endpoint URLs
    def parsedEPData(self, epType) -> str:

        # Get the data to be returned as a string
        ret_data = epInfo(epType)['ep']

        # For all things that potentially need to be replaced, replace them with relevant data points
        for point in self.replace.keys():
            if point in ret_data:
                ret_data = ret_data.replace(point, str(self.replace[point]))
        
        # Return the data required
        return ret_data
        

    def getURL(self, epType) -> str:
        
        # Get the relevant request URL
        reqURL = baseurl+self.parsedEPData(epType)

        # Return data
        return reqURL

    def sendRequest(self, epType) -> dict:
        

        # Make sure to get the right method - must be better way than an if elif tree
        if epdata[epType]['method'] == 'GET':
            
            # Return processed data
            return req.get(self.getURL(epType), headers=self.bearer_auth).json()

        elif self.parsedEPData['method'] == 'POST':
            pass


# Response Parser
def responseParser(response):
    pass

    

userid = ledger_acc_id
headers = {"Authorization": f"Bearer {bearer}"}

twitter_agent = reqBuilder(1161639845531455489, bearer)
result = twitter_agent.sendRequest('getUserTweets')
print(result)
exit()
# 449517989 - example spam acc
# url = baseurl+'/2/users'+f'/{userid}'+'/mentions'
url = baseurl+'/2/users'+f'/{str(ledger_acc_id)}'+'/tweets'
# url = baseurl+'/oauth/request_token'
result = req.get(url, headers=headers).json()
print(result)


def getIDByUser(user) -> str:
    pass

class twitterBot:
    def __init__(self) -> None:
        pass

    # First function for class is to create a list of tweets that we are "watching"
    def getRecent(self) -> dict:
        req.get
        return {}

# We watch users on this list - as they're being suspicious
class watchlist:
    def __init__(self) -> None:
        pass

