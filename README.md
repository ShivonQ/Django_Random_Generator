# Django_Random_Generator

## Summary
My life as a Dungeon Master for D&D 3.5 over the last fifteen years has always been very enjoyable, though one of the most annoying things is generating random treasure.  So I created this generator to create the rudimentary elements of treasure from the 3.5 Dungeon Masters guide, with a few additions of my own. 
This is a Django based project and as such in order to run it you'll need to fork this repo, then navigate to the folder in your command line running the following:

## Requirements
---
1. Must have python3.5 or later involved
2. Must havce the latest version of Django
3. Must have my database from this repo, unless you are willing to enter 800+ rows of data yourself. **this is not recommended**

## Run Server
---
Navigate to your file folder and run the following command:
`python manage.py runserver`

Then navigate to `localhost:8000` for the main site.
Enter a number from 1-20 into the form on the Treasure Generator page.

If you desire to manipulate the database you can navigate to `localhost:8000\admin`
and enter the root superuser information 

`username: admin 
password:0okm9ijn
`

###Known Issues
---
1. The views.py file is extremely busy and has a lot of things in it that really don't belong there.  In a major refactor for SPrint #2 I will clean up quite a bit.
2. Also at the moment the checkboxes for No Gems and No Art don't work. This is due to the need to pass them into the goods retrieval function and I just ran out of time.
3. Scrolls do not generate which is becaseu that requires tables not only of all spells, but also of the 9 levels of spells. Hundreds and hundreds of entries. It will happen evantually.


#### Next Sprint
---
1. Refactor for organization.
2. Scrolls
3. Weapons
4. Diary Entries
5. User Accounts
6. Knowledge Checks
