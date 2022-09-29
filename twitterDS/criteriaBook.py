# import re
import urlexpander

domainBook = ['twitter.com', 't.me', 'telegram.me', 'docs.google.com']
ledgerBook = ['ledger.com', 'ledger.fr']
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
        
        shortURL = url_prefix+text.split(url_prefix)[-1]
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

def answered(text):
    pass

def includeLink(text):
    pass

def askMessage(text):
    pass