# Twitter Bot - Spam and Scam protection

### Concept

This twitter bot is made to engage with scammers that are constantly attempting to scam users via a twitter account. The general idea would be to either interact with our tweets automatically (like a pinned post on Reddit), or to directly reply to twitter bots.

### Audience

While this is sometihng that many other enterprise entites could use, this is currently slated for in-house use, with the tech support team.

### Inputs / Outputs

##### Inputs
Main account and Support account tweets and replies.

##### Outputs
Tweet an initial response that advises that scammers are always attempting to scam users via replies and DMs.
We are currently building a database of responses, that I will put into a data structure in the responses.py file.

Reply to scam accounts that identify potential scammers (that may try to engage via google form links or built-in "send a message" links)
There are many more ways that they might do so, but it will be important to know how to engage them.

### Flowchart

List of "watched" tweets (Latest tweets? Most engaged tweets?)
*Note* - We are currently only getting the last 10 tweets
->
Poll REST endpoint to find all the latest replies (only last 10 at the moment)
-> 
Identify new replies that have not be engaged with (and that need to be engaged with)
-> 
Remove user tweets (that we do not want the bot to interact with)
->
reply to scam tweets from database
