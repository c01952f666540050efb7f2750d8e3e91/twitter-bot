import dash
from dash import Dash, dcc, html, Input, Output, State, dcc, ctx, callback
import dash_bootstrap_components as dbc

from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session

# Load .env
load_dotenv(dotenv_path="../.env")

class authorisation:
    def __init__(self):
        # .env varibales
        bearer = os.getenv("BEARER")
        support_acc_id = os.getenv("SUPPORT_ACC_ID")
        ledger_acc_id = os.getenv("LEDGER_ACC_ID")

        self.agent_key = os.getenv("API_KEY")
        self.agent_secret = os.getenv("API_SECRET")

        # URLS
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        self.base_authorization_url = "https://api.twitter.com/oauth/authorize"

        # variable definition
        self.access_token = None
        self.access_token_secret = None

        # Get request token - This can be done at the start of every session?
        self.oauth = OAuth1Session(
            self.agent_key, 
            client_secret=self.agent_secret
        )

        try:
            fetch_response = self.oauth.fetch_request_token(request_token_url)
        except ValueError:
            print("Something went wrong")
        
        # # Attempt to fetch
        # try:
        #     fetch_response = self.oauth.fetch_request_token(self.request_token_url)
        # except ValueError:
        #     print(
        #         "There may have been an issue with the consumer_key or consumer_secret you entered."
        #     )

        # set variables
        self.resource_owner_key = fetch_response.get("oauth_token")
        self.resource_owner_secret = fetch_response.get("oauth_token_secret")


    def getAuthURL(self):
        # Get authorization URL    
        return self.oauth.authorization_url(
            self.base_authorization_url
        )


    def submitPin(self, verifier):

        # Get the access token
        self.access_token_url = "https://api.twitter.com/oauth/access_token"
        self.oauth = OAuth1Session(
            self.agent_key,
            client_secret=self.agent_secret,
            resource_owner_key=self.resource_owner_key,
            resource_owner_secret=self.resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = self.oauth.fetch_access_token(self.access_token_url)

        self.access_token = oauth_tokens["oauth_token"]
        self.access_token_secret = oauth_tokens["oauth_token_secret"]

        # Make the request
        self.oauth = OAuth1Session(
            self.agent_key,
            client_secret=self.agent_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )