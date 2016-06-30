
import random

import re

import emotes

nicknames = {
	'134968288772882432': ['Hawkaloo', 'Hawke', 'Hawkey', 'Hawkey Hawke'],
	'136190686230741002': ['Trambles', 'Trambelus', 'Trambuck', 'Buck', 'Applebuck', 'Applepone', 'Best Apple'],
	'110932722322505728': ['Woof', 'Woofy', 'Ian', 'Woofy Woof', 'Best Woof'],
	'166229158681247753': ['Carbon', 'Dragon', 'Carburd', 'Best Dragon'],
	'any': ['Sexy', 'Butts' ]
}

def respond(self):
	response = ""


	if re.search(r'(^| )(hi|hello|hey|hi there|hiya|heya|howdy)(! |, | )scootabot', self.command):
		#author = re.search('(^| )\w+( ♀)?$', self.message.author.name).group().strip().title()
		#ret = emotes.get_message(emotes.HI, author)
		chance = random.randint(0, 10)

		if (chance < 7):
			response = emotes.get_message(emotes.HI, nicknames[self.message.author.id])
		elif (7 <= chance < 9):
			response = emotes.get_message(emotes.HI, self.message.author.display_name)
		else:
			response = emotes.get_message(emotes.HI, nicknames['any'])
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

