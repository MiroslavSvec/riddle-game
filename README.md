# Riddle Game

Simple Python riddle game

## Credits

### Boostrap template

https://blackrockdigital.github.io/startbootstrap-sb-admin/index.html

### Databases

Mixed

https://github.com/inuits/hubot-scripts/blob/master/riddles.json

General

https://github.com/azeemigi/riddle-server/blob/master/modules/core/src/main/resources/riddles.json

## Working on profiles creation

For profile using JSON:

create separate file for each of the profile to work only with small files

Created separate all-profiles.txt:
file with all profile names for events

## Bugs and Testing

Check values of the profile

Check if profile already exist

Fix bug when all-profiles.txt exist without data (redirect) --  Fixed with checking if the len(profiles) is > 0

Fix "Wiev all messages" in window button (bad redirecting)

Fix bug with injecting nav links (multiple click add to link) --- Fixed

Fix Chat window working in profile page only


## Chngelog

Scraped redirection to login page as I do not think that is good user experiences.
If user enters user name wich already exist (as he does not have to know about it)
will use JS to handle the form check and and then redirect via Python

Created rest API for profile data