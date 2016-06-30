
import random

import emotes

	def respond(message):
		response = ""

		if ("?" in message):
			chance = random.randint(0, 98)

			if (chance < 34):
				response = emotes.get_message(emotes.YEP)
			elif (34 <= chance < 67):
				response = emotes.get_message(emotes.NOPE)
			else:
				response = emotes.get_message(emotes.HUH)

		return response
