import requests as req

# Universal immutables
baseurl = 'https://api.twitter.com'

# Endpoint package
epdata = {
    'getTweets': {
        'method': req.get,
        'ep': '/2/tweets'
    },
    'postTweet': {
        'method': req.post,
        'ep': '/2/tweets'
    },
    'deleteTweet': {
        'method':  req.delete,
        'ep': '/2/tweets'
    },
    'getUserTweets': {
        'method': req.get,
        'ep': '/2/users/:id/tweets'
    },
    'getUserMentions': {
        'method': req.get,
        'ep': '/2/users/:id/mentions'
    },
    'getIdByUsername': {
        'method': req.get,
        'ep': '/2/users/by',
        'params': {
            'usernames': None
        }
    }
}