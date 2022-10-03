# EXTERNAL IMPORTS
import requests as req
from twitterLibs.endpoints import baseurl, epdata
from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session
import json

# INTERNAL IMPORTS
from twitterLibs.endpoints import *

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")
agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

# Get request token - This can be done at the start of every session?
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(agent_key, client_secret=agent_secret)

# Attempt to fetch
try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

# set variables
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")

def epInfo(epType) -> dict:
        return epData[epType]

# Request Builder
class reqBuilder:
    def __init__(self, subject, bearer, key, secret) -> None:
        self.subject = subject

        # Things that we replace
        self.replace = {
            ':id': self.subject,
        }

        # Specific Auth Types
        self._bearer_auth = {"Authorization": f"Bearer {bearer}"}
        self._resource_owner_key = None
        self._resource_owner_secret = None
        
        # create oauth object
        self.oauth = OAuth1Session(agent_key, client_secret=agent_secret)

    # Get request token - This can be done at the start of every session?
    def initOAuth(self, **kwargs):
        
        # Currently aribtrary
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    
        try:
            # Attempt to fetch
            fetch_response = oauth.fetch_request_token(request_token_url)

        except ValueError:

            # Debug print
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        # Set key and secret
        self._resource_owner_key = fetch_response.get("oauth_token")
        self._resource_owner_secret = fetch_response.get("oauth_token_secret")

    # Get authorization - Requires log in!
    def authorise(self):

        base_authorization_url = "https://api.twitter.com/oauth/authorize"

        # We will get a URL that we will navigate to
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)

        # and input our pin
        verifier = input("Paste the PIN here: ")

    def completeAuth(self, verifier):
        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            agent_key,
            client_secret=agent_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        # Make the request
        oauth = OAuth1Session(
            agent_key,
            client_secret=agent_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

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
        # TODO - Adding headers - arbitrary currently
        # headers = {}.update()

        # Send request - Currently only sending with bearer auth.
        # TODO - Assign correct authentication when required
        return epData[epType]['method'](
            self.getURL(epType), 
            headers=self.bearer_auth,
            params=params
            ).json()