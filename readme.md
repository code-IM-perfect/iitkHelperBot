# Telegram based IITK Helper Bot

This is a telegram bot that aims to help the iitk folks. It was made for CodeCraft 2024 by pclub iitk.

## Features
- ### **Attendance:**
	Easily check your attendace without needing to go to the attendance office or keeping track of all the links.
- ### **khol:** 
	As a culture-respecting member of the iitk community this bot has learnt its pure Hindi intro by heart.
- ### **studentPhoto:**
	Get anybody's embarrassing ID Card photo.
- ### **customdp:**
	Get anybody's cool new Custom DP
- ### **motivate:**
	Life in iitk can get very dull and depressing, this bot can get you back on track by motivating you...one quote at a time.
- ### **dice:**
	Literally rolls a dice...for all the late night ludo matches(??)...idk why I included this tbh

## Setup
First clone the project-
```
git clone https://github.com/code-IM-perfect/iitkHelperBot.git
```

To power your instance of this bot you need to get your bot's API Key from [botfather](https://t.me/botfather). Put that key in the `boy_token.py` file as the value of the `BOT_TOKEN` variable. At this point you are basically good to go.

Next just run the `main.py` file and your bot will become the **iitkHelperBot** (until you stop the program).


## Known Issues
- I tried hosting it with pythonanywhere but apparently I need a premium account for keeping it online for more than 2 days so you'll need to run it locally while testing.

- For some reason hosting with pythonanywhere can break the Custom DP checking functionality (`requests.get()` fails for some reason). To mitigate this it sends the dp URL even if Custom DP is not found.

- I realised I could have used webhooks on some webites that give the service for free but it was too late (totally not because it was harder™).