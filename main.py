import requests as req
from dotenv import load_dotenv
import os
import requests_oauthlib



# Internal Imports
from twitterDS.endpoints import *
from twitterDS.criteriaBook import *
from twitterDS.requestBuilder import reqBuilder

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

# This could be a dictionary where we watch for the dangerous links
linkWatch = {}

# Response Parser
def responseParser(response, checkType=None):

    tweetList = []

    # For all the tweets in the response
    for tweet in result['data']:
        
        # Check all conditions
        for condition in tweetCriteria.keys():
            
            # If there is a condition listed that has happened - temporarily here to avoid errors during building
            if tweetCriteria[condition]['condition']:
                ret_dat = tweetCriteria[condition]['condition'](tweet['text'])
                
                # Bot has found something that matches the relevant conditions
                if ret_dat['bool'] is True:

                    # Debug print
                    print(ret_dat)
                    print(tweet['id'])

                    # Perform some action
                    # post_dat = tweetCriteria[condition]['action']()
            else:

                # To make sure we have a specific list
                ret_dat = {'fullLinks': []}

        print("---"*20)

        tweetList.append({
            tweet['id']: {
                'originalText': tweet['text'],
                'links': ret_dat['fullLinks']
            }
        })
    

headers = {"Authorization": f"Bearer {bearer}"}

twitter_agent = reqBuilder(support_acc_id, bearer)
# twitter_agent.sendRequest('getUserMentions')

result = twitter_agent.sendRequest('getUserMentions')

responseParser(result)
# print(result)
exit()
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

