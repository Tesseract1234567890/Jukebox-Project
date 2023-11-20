# CatJam

  

  

An online jukebox application for creating a shared/collaborative music queue.

Made with Django, Python, and HTML/CSS/JS.

Developed by Charlotte George, Matt Marafino, Saavan Tandon, and Jinna Smail as part of the CSHacks and Opcommathon hackathons.

Available at [catjam.cs.house](catjam.cs.house)

  

## Features

  

- Search for songs + add songs to queue

  

- Manage queue in admin panel

  

- Spotify API integration

  

- Updates queue in real time for users

  

  

## Installation
If you would like to run CatJam locally on your machine, first create a new POSTGRES database - if you are a CSH member, you can do this at deadass.csh.rit.edu

In your terminal, clone into the repo, set up your venv, and then run:

  

    pip install -r requirements.txt

Go to `settings.py`and scroll down to the `DATABASES` variable. which looks like this:

    DATABASES  = {
	    'default': {
		    'ENGINE': 'django.db.backends.postgresql',
		    'NAME': 'catjam',
		    'HOST': 'postgres.csh.rit.edu',
		    'PASSWORD': 'password',
		    'USER': 'catjam'
	    }
    }
Replace the name, host, user, and password to match your POSTGRES database.
Make a new .env file that looks like this:

  

    CLIENT_ID = ""
    
    CLIENT_SECRET = ""
    
    ADMIN_ID = ""
    
    ADMIN_PW = ""

  
  

Replace the CLIENT_ID and CLIENT_SECRET values with your Spotify client ID and secret.

To get your client ID and secret, head to https://developer.spotify.com/dashboard and make a new app. When you're done, go to Settings to find your ID and secret.

**Note: You MUST have a Spotify Premium account to access certain parts of the API that are used here. The current version of catjam uses my client ID + secret as a temporary measure.**

The ADMIN_ID and ADMIN_PW values will be your admin login for the admin panel, which displays and plays the current song and gives access to certain admin commands such as emptying the queue and skipping songs (still a work-in-progress).

  

## Usage

  

To run the server locally, activate your venv and then run

  

py manage.py runserver

The terminal will spit out a link to a local server that runs the website locally. It will also automatically update if you make any changes to your code.

