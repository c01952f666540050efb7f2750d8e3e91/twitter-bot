import requests as req
from dotenv import load_dotenv
import os
import urlexpander

# Internal Imports
from twitterDS.endpoints import *
from twitterDS.criteriaBook import *

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")


def epInfo(epType) -> dict:
        return epdata[epType]


tweetCriteria = {
    'answered': {
        'condition': None,
        'action': None
    },
    'link': {
        'condition': linkShared,
        'action': None
    },
    'message': {
        'condition': None,
        'action': None
    },
    'ignore': {
        'condition': None,
        'action': None
    }
}

linkWatch = {
    
}

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
    
    def parsedParams(self, epType, **params) -> dict:
        # Add all the params required for request

        # If there are relevant params we want to use
        if epInfo(epType)['params']:
            # Match params
            print(epInfo(epType)['params'])
            print(params)
            
        # print(epInfo(epType)['params'])
        # exit()
        return {}

    def sendRequest(self, epType, **params) -> dict:

        # Send request - Currently only sending with bearer auth.
        # TODO - Assign correct authentication when required
        return epdata[epType]['method'](
            self.getURL(epType), 
            headers=self.bearer_auth,
            params=params
            ).json()



# Response Parser
def responseParser(response, checkType=None):

    # For all the tweets in the response
    for tweet in result['data']:
        print("---"*20)
        print(tweet)
        
        # Check all conditions
        for condition in tweetCriteria.keys():
            
            # If there is a condition listed that has happened - temporarily here to avoid errors during building
            if tweetCriteria[condition]['condition']:
                ret_dat = tweetCriteria[condition]['condition'](tweet['text'])
                
                if ret_dat['bool'] is True:

                    print(ret_dat)
        
        print("---"*20)

    

headers = {"Authorization": f"Bearer {bearer}"}

twitter_agent = reqBuilder(support_acc_id, bearer)
# result = twitter_agent.sendRequest('getUserMentions')
# GetIdBy
result = twitter_agent.sendRequest('getUserMentions')

print(responseParser(result))
# print(result)
exit()

for tweets in result['data']:
    
    if "t.co" in tweets['text']:
        print(tweets['id'])
        print(tweets['text'])
        print("-----")
    else:
        print(tweets)
    


exit()


# Main Twitter Bot Class
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

