#!/usr/bin/env python3

# Global imports
import discord
import logging
import sys
import os # for script restarts
import subprocess
import traceback
import git

import time
import re
import random

# Local imports
import derpi
import emotes
import auth

logging.basicConfig(level=logging.INFO, filename=time.strftime('logs/%Y-%m-%d_%H.%M.%S.log'))

EMAIL = 'hawke252.reddit@gmail.com'

client = discord.Client()

def restart(channel_id, force=False):
	if os.name == 'nt':
		logging.debug("NT restart")
		subprocess.Popen(' '.join(["python", sys.argv[0], str(channel_id)]))
		client.logout()
		sys.exit(0)

	elif os.name == 'posix':
		logging.debug("POSIX restart")
		msg = git.cmd.Git('.').pull()
		logging.debug("Git pull yielded {}".format(msg))

		if not force and msg == 'Already up-to-date.':
			return emotes.get_emote(emotes.NOPE) + ' ' + msg
		else:
			logging.debug("Logging out")
			client.logout()

			logging.debug("Restarting with args {}, {}".format(sys.argv[0], str(channel_id)))
			sys.stdout.flush()
			os.execl(sys.argv[0], sys.argv[0], str(channel_id))

	else:
		logging.error("Unknown OS {}, could not restart".format(os.name))

class Command:
	last_command = {}

	def __init__(self, message):
		self.message = message
		self.command = message.content.lower()

	def process(self):
		ret = None

		try:
			if self.command == '!reload':
				ret = restart(self.message.channel.id)
				# Only returns this if a restart isn't happening
				
			elif self.command == '!force-reload':
				restart(self.message.channel.id, True)

			elif self.command == '!stop':
				client.send_message(self.message.channel, emotes.get_message(emotes.BYE))
				sys.exit(0)

			elif self.command.startswith('!derpi ') or self.command == '!derpi':
				ret = derpi.process(self.message)
				self.last_command[self.message.author.id + ':' + self.message.channel.id] = self.command

			elif self.command == '!again':
				if (self.message.author.id + ':' + self.message.channel.id) in self.last_command:
					self.command = self.last_command[self.message.author.id + ':' + self.message.channel.id]
					self.message.content = self.last_command[self.message.author.id + ':' + self.message.channel.id]
					return self.process()
				else:
					ret = emotes.get_message(emotes.HUH)

			elif 'scootabot' in self.command:

				if 'roll' in self.command:
					search_res = re.search(r'\d*d(\d+)(\s*\+\s*\d+)?', self.command)
					if not search_res:
						return

					roll = [1 if e == '' else e for e in search_res.group(0).replace(' ','').replace('d','+').split('+')]

					dice = [random.randint(1, int(roll[1])) for _ in range(int(roll[0]))]
					if len(roll) == 3:
						dice += [int(roll[2])]

					ret = "{}\n _Rolling {}d{}:_\n  {}\n**={}**".format(
						emotes.get_emote(emotes.YEP),
						roll[0],
						" + ".join(roll[1:]),
						" + ".join(dice),
						sum(dice)
					)

			# elif 'scootabot' in self.command and 'hawke' in self.command and 'favorite pon' in self.command:
			# 	ret = emotes.get_emote(emotes.YEP) + ' Twist!'

			if re.search(r'(^| )(hi|hello|hey|hi there|hiya|heya|howdy)(! |, | )scootabot', self.command):
				author = re.search('(^| )\w+( ♀)?$', self.message.author.name).group().strip().title()
				ret = emotes.get_message(emotes.HI, author)

		except SystemExit:
			print("sys.exit called")
			sys.exit(0)

		except:
			exc = traceback.format_exc()
			client.send_message(self.message.channel, "[](/notquitedashie) ```{}```".format(exc))
			print(exc)

		return ret


@client.event
def on_ready():
	# Restart info should be in sys.argv
	if len(sys.argv) == 3:
		logging.info('Launched with client ID {}. Last code revision: {}'.format(*sys.argv[1:3]))
	if len(sys.argv) > 1:
		print(sys.argv)
		channel = client.get_channel(sys.argv[1])
		print(channel)
		client.send_message(channel, emotes.get_message(emotes.HI, "all"))
	logging.info("Ready!")
	logging.debug("Launched with args {}".format(sys.argv))

@client.event
def on_message(message):
	if message.author != client.user:
		logging.info(" {} said: {}".format(message.author, message.content))

		cmd = Command(message=message)
		response = cmd.process()

		if response:
			client.send_message(message.channel, response)

def main():

	password = auth.find_pw(EMAIL)

	client.login(EMAIL, password)
	client.run() # enter main loop

if __name__ == '__main__':
	main()

# TODO:
# Keep search object handle for !again
