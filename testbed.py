# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session

# I will need to contstruct a authoriseurl
import requests as req
from twitterDS.endpoints import baseurl, epdata
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
bearer = os.getenv("BEARER")
support_acc_id = os.getenv("SUPPORT_ACC_ID")
ledger_acc_id = os.getenv("LEDGER_ACC_ID")

agent_key = os.getenv("API_KEY")
agent_secret = os.getenv("API_SECRET")

headers = {
    'Content-type': 'application/json', 
    "Authorization": f"Bearer {bearer}"
    }
