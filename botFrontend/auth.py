# I will need to contstruct a authoriseurl
import requests as req
# from ..twitterLibs.endpoints import baseurl, epData
from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session
import json

# Load .env
load_dotenv("../")
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

# Get request token - This can be done at the start of every session?
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(agent_key, client_secret=agent_secret)