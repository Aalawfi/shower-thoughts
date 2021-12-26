# shower-thoughts
This app pulls posts from the subreddit r/Showerthoughts and sends a SMS message of a currently popular shower thought to a user.
User Interface: Kivy 
Back-end: Django 
Database: mySQL 
SMS service: Twilio? 

About the r/Showerthoughts subreddit: "Showerthought" is a loose term that applies to the types of thoughts you might have while carrying out a routine task like showering, driving, or daydreaming. At their best, showerthoughts are universally relatable and find the amusing/interesting within the mundane.

Development Plan: 

1) Building the user interface: 
    - Simple Components include: a simple form that takes in first and last names and a phone number
    - A submit button that first verifies if the entry is valid and if it is then call "generate" function 
    - "generate" function POSTs the name and phone number to the server
  
2) Building the back-end:
    i. Server 
        - Catch the JSON from the front end 
        - Communicate with reddit API and get a random popular post in r/ShowerThoughts 
        - Send the post to the phone number ONLY if the number did not get that same post previously 
        - Save to database
    ii. Database 
        - Non-touching to the front-end 
        - Table has 4 columns in addition to ID: 1) First Name 2) Last Name 3) Phone number 4) A text
