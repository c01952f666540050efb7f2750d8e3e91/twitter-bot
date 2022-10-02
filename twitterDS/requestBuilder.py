# INTERNAL IMPORTS
from twitterDS.endpoints import *

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
        # Adding headers - arbitrary currently
        headers = {}.update(self.bearer_auth)

        # Send request - Currently only sending with bearer auth.
        # TODO - Assign correct authentication when required
        return epdata[epType]['method'](
            self.getURL(epType), 
            headers=headers,
            params=params
            ).json()