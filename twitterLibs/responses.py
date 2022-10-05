import random

class responses:
    def __init__(self):

        # response book with example response
        self.responseBook = {
            'telegram': [{
                'text': "Ledger Support doesn't offer support via Telegram, be careful out there! There are scammers abound!"
            }],
            'dms': [{
                'text': 'Hey, Ledger Support would never ask to go into DMs. This is really suspicious!'
            }],
            'googleForm': [{
                'text': "Ledger support doesn't ask to solve cases with Google Forms, are you trying to scam people?"
            }]
        }
    
    def addResponse(self, responseType, text, **kwargs):

        # Add text to response book
        self.responseBook[responseType].append({
            'text': text
        })

    def getRandomResponse(self, responseType):

        # Return a random choice from the specific response type
        return random.choice(self.responseBook[responseType])