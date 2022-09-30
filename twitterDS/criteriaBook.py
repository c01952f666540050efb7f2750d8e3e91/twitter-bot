# import re
import urlexpander

domainBook = ['twitter.com', 't.me', 'telegram.me', 'docs.google.com']

url_prefix = "https://"
tco = 't.co'

def linkShared(text):
    ret_dat = {
        'bool': False,
        'linkType': None,
        'fullLink': None
    }
    

    # Since all links on twitter are shortened, we look for the shortened tweet
    if tco in text:
        
        # TODO - We have to remember this might not be the only link
        urlList = url_prefix+text.split(url_prefix)


        for shortURL in urlList:
            shortURL = url_prefix + shortURL
            print(f"ShortURL: {shortURL}")
            
            print(urlexpander.expand(shortURL))
            url_candidate = urlexpander.expand(shortURL)

            for domain in domainBook:
                if domain in url_candidate:
                    print(f"Someone linked: {domain}")
                    
                    # They shared a link!
                    ret_dat = {
                            'bool': True,
                            'linkType': domain,
                            'fullLink': url_candidate
                        }
        
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