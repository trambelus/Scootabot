
import random

import re

import emotes

def respond(self):
	response = ""


	if re.search(r'(^| )(hi|hello|hey|hi there|hiya|heya|howdy)(! |, | )scootabot', self.command):
		#author = re.search('(^| )\w+( ♀)?$', self.message.author.name).group().strip().title()
		#ret = emotes.get_message(emotes.HI, author)
		response = emotes.get_message(emotes.HI, self.message.author.id)
	elif ("?" in self.command):
		chance = random.randint(0, 98)

		if (chance < 34):
			response = emotes.get_message(emotes.YEP)
		elif (34 <= chance < 67):
			response = emotes.get_message(emotes.NOPE)
		else:
			response = emotes.get_message(emotes.HUH)
	else:
		response = "no u"

	return response

