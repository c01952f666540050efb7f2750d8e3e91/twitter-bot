import re
import urlexpander

# Book of domains we are looking into
domainBook = ['twitter.com', 't.me', 'telegram.me', 'docs.google.com']
tco = 't.co'

# Using regex to search for links
def urlSearch(stringinput):
 #regular expression
 regularex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))))+(?:(([^\s()<>]+|(([^\s()<>]+))))|[^\s`!()[]{};:'\".,<>?«»“”‘’]))"
 
 #finding the url in passed string
 urlsrc = re.findall(regularex,stringinput)
 
 #return the found website url
 return [url[0] for url in urlsrc]

def linkShared(text):    
    
    # The data we are looking to return
    ret_dat = {
        'bool': False,
        'fullLinkS': []
    }

    # Since all links on twitter are shortened, we look for the shortened tweet
    if tco in text:
        
        # Get all the urls in text
        urlList = urlSearch(text)
        expandedURLList = [urlexpander.expand(x) for x in urlList]

        # For all the urls in the list
        for url in expandedURLList:
            for domain in domainBook:
                if domain in url:
                    #  A DOMAIN HAS A HIT
                    ret_dat['bool'] = True

                    if 'fullLinks' in ret_dat:
                        # ADD IT TO THE LIST
                        ret_dat['fullLinks'].append(url)
                    else:
                        pass
    return ret_dat

# This has already been answered by Ledger Support
def answered(text):
    return None

# TODO - We might have to remove this - it's essentially a repeat
def includeLink(text):
    pass

# Asking for a message - this also includes a link though
def askMessage(text):
    pass

def composeReply():
    return {
        'replyText': ''
    }

# Currently relatively arbitrary for testing purposes
tweetCriteria = {
    'answered': {
        'condition': None,
        'action': None
    },
    'link': {
        'condition': linkShared,
        'action': None,
        'authType': 'oauth'
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