# Twitter Bot - "Ledger Protect"

### Concept

This twitter bot is made to engage with scammers that are constantly attempting to scam users via the Ledger twitter account. The general idea would be to either interact with our tweets automatically (like a pinned post on Reddit), or to directly reply to twitter bots.

### Audience

While this is sometihng that many other enterprise entites could use, this is currently slated for in-house use, but the tech support team.

### Inputs / Outputs

##### Inputs
Main account and Support account tweets and replies.

##### Outputs
Tweet an initial response that advises that scammers are always attempting to scam users via replies and DMs

Reply to scam accounts that identify potential scammers (that may try to engage via google form links or built-in "send a message" links)

### Flowchart

List of "watched" tweets (Latest tweets? Most engaged tweets?)
*Note* - There is currently no way to get tweets older than 7 days
->
Poll REST endpoint to find all the latest replies
-> 
Identify new replies that have not be engaged with
-> 
Remove user tweets (that we do not want the bot to interact with)
->
reply to scam tweets (?)


### Technical Feasibility

The feasibility of automatically replying to an existing account is very easy. The main technical hurdle I am currently investigating, is the ability to very specifically target accounts that are **not** users, but scammers that are trying to scam users.

We will always be behind, with regard to this, as we will want to make sure that we do not go after any regular users.

