import requests as req
from dotenv import load_dotenv
import os
import urlexpander

# Internal Imports
from twitterDS.endpoints import *
from twitterDS.criteriaBook import *
from twitterDS.requestBuilder import reqBuilder

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")



# This could be a dictionary where we watch for the dangerous links
linkWatch = {}



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

# Main Twitter Bot Class
class twitterBot:
    def __init__(self) -> None:
        pass

    # First function for class is to create a list of tweets that we are "watching"
    def getRecent(self) -> dict:
        return {}

# We watch users on this list - as they're being suspicious
class watchlist:
    def __init__(self) -> None:
        pass

