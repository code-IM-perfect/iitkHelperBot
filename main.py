#!/usr/bin/python

import telebot
import re
import requests
import random

from bot_token import BOT_TOKEN
from quotes import quotes

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message,"""
	Welcome! This is an iitk helper bot, it can do various things-
	- /start and /help : Show this message
	- /attendance : Get your attendance
	- /khol : Bot se khulva lo
	- /studentPhoto : Get anybody's original student search photo
	- /customdp : Get anybody's Custom DP on student search
	- /motivate : Get a motivational quote
	- /dice : rolls a dice...idk why I included this
	""")

# @bot.message_handler(func=lambda m: m.text == "yooo")
# def echo_all(message):
# 	bot.reply_to(message, message.text)


###############################  ATTENDANCE  ###############################

def get_attendance(message,rollNo,backupMessage):
	dates = re.findall("\d\d",message.text)
	if len(dates)==6:
		months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		fromDate = f"{int(dates[0])}-{months[int(dates[1])-1]}-20{dates[2]}"
		toDate = f"{int(dates[3])}-{months[int(dates[4])-1]}-20{dates[5]}"
		bot.send_message(message.chat.id, f"Getting attendance for {rollNo}\nFrom {fromDate} to {toDate}")
		bot.send_message(message.chat.id, "http://172.26.192.62/Smartrollcall/Account/Login")
		bot.send_message(message.chat.id, f"http://172.26.192.62/Smartrollcall/Reports/ReportViewer.aspx?ReportID=11&Category=1&from={fromDate}&to={toDate}&RollNumber={rollNo}")
		bot.send_message(message.chat.id, "Open *BOTH* these links to see your attendance. The second link will not open unless the first one is already open\n\nAlso you need to be on the IITK network (iit wifi or vpn)")
	else:
		bot.send_message(message.chat.id, "Uhh something seems to be wrong with the date format")
		attendance_ask_date(backupMessage)
		return 0

	

def attendance_ask_date(message):
	rollNo = re.findall("\d\d\d\d\d\d\d\d|\d\d\d\d\d\d",message.text)

	if (not rollNo):
		bot.send_message(message.chat.id, "Uhh the RollNo seems to be wrong")
		attendance_ask_roll(message)
		return 0

	bot.send_message(message.chat.id,"Okay, from when to when?")
	askingStartDate = bot.send_message(message.chat.id,"Input format-\n`DD-MM-YY DD-MM-YY`\nlike `13-02-24 05-03-24`", parse_mode="markdown")
	bot.register_next_step_handler(askingStartDate, get_attendance, rollNo[0],message)

@bot.message_handler(commands=['attendance'])
def attendance_ask_roll(message):
	askingRoll = bot.send_message(message.chat.id, "So you're calculating if you can leave today's class?\nCool just gimme your *Roll No*", parse_mode="markdown")
	bot.register_next_step_handler(askingRoll, attendance_ask_date)


###############################  PHOTO  ###############################

def get_SPhoto(message):
	rollNo = re.findall("\d\d\d\d\d\d\d\d|\d\d\d\d\d\d",message.text)

	if rollNo:

		bot.send_message(message.chat.id, f"There you go-\noa.cc.iitk.ac.in/Oa/Jsp/Photo/{rollNo[0]}_0.jpg")
		# bot.send_photo(message.chat.id, f"http://oa.cc.iitk.ac.in/Oa/Jsp/Photo/{rollNo[0]}_0.jpg")
	else:
		bot.send_message(message.chat.id, "Uhh the RollNo seems to be wrong")
		photo_ask_rollNo(message)
		return 0


@bot.message_handler(commands=['studentPhoto'])
def photo_ask_rollNo(message):
	askingRoll = bot.send_message(message.chat.id, "Gimme a *RollNo*", parse_mode="markdown")
	bot.register_next_step_handler(askingRoll, get_SPhoto)


###############################  CUSTOM DP  ###############################

def get_CustomDP(message):
	url = f'https://home.iitk.ac.in/~{message.text}/dp'
	try:
		page = requests.get(url)
		bot.send_photo(message.chat.id, url, f'home.iitk.ac.in/~{message.text}/dp')
	except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
		bot.send_message(message.chat.id, f'home.iitk.ac.in/~{message.text}/dp')
		bot.send_message(message.chat.id, "Couldn't access the image. Either the username is incorrect or this guy did not upload a custom dp")
		bot.send_message(message.chat.id, "Manybe try /studentPhoto")

@bot.message_handler(commands=['customdp'])
def photo_ask_username(message):
	askingUsername = bot.send_message(message.chat.id, "Gimme a *Username*", parse_mode="markdown")
	bot.register_next_step_handler(askingUsername,get_CustomDP)

###############################  QUOTES  ###############################
@bot.message_handler(commands=['motivate'])
def get_quote(message):
	bot.send_message(message.chat.id, random.choice(quotes))

###############################  KHOL  ###############################
@bot.message_handler(commands=['khol'])
def khol_de(message):
	response="Mera naam @codeCraftHelperBot hai. Mere baap ka naam @imNO_Jedi hai. Mai yaha pyTelegramBotAPI se aya hun. pclub dwara ayojit codeCraft ko utten kar maine yaha Telegram me pravesh kia hai. Meri mukhya abhiruchiya logo ki madad karna hai."
	bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['dice'])
def roll_dice(message):
	bot.send_dice(message.chat.id)


bot.infinity_polling()