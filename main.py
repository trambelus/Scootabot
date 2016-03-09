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
import re # for command processing, later
# Local imports
import derpi
import emotes
import auth

logging.basicConfig(level=logging.DEBUG)

EMAIL = 'hawke252.reddit@gmail.com'

client = discord.Client()

def restart(channel_id):
	if os.name == 'nt':
		logging.debug("NT restart")
		subprocess.Popen(' '.join(["python", sys.argv[0], str(channel_id)]))
		client.logout()
		sys.exit(0)

	elif os.name == 'posix':
		logging.debug("POSIX restart")
		msg = git.cmd.Git('.').pull()
		logging.debug("Git pull yielded {}".format(msg))

		if msg == 'Already up-to-date.':
			return msg
		else:
			logging.debug("Logging out")
			client.logout()
			
			logging.debug("Restarting with args [{}], [{}]".format(sys.argv[0], str(channel_id)))
			sys.stdout.flush()
			os.execl(sys.argv[0], str(channel_id))

	else:
		logging.error("Unknown OS {}, could not restart".format(os.name))

class Command:
	def __init__(self, message):
		self.message = message
		self.command = message.content.lower()

	def process(self):
		try:
			if self.command.startswith('!reload'):
				return restart(self.message.channel.id)
				# Only returns this if a restart isn't happening

			if self.command.startswith('!stop'):
				client.send_message(self.message.channel, "Stopping!")
				sys.exit(0)

			if self.command.startswith('!derpi'):
				return derpi.process(self.message)

		except SystemExit:
			print("sys.exit called")
			sys.exit(0)

		except:
			exc = traceback.format_exc()
			client.send_message(self.message.channel, "[](/notquitedashie) ```{}```".format(exc))
			print(exc)

		return None


@client.event
def on_ready():
	# Restart info should be in sys.argv
	if len(sys.argv) == 3:
		logging.info('Launched with client ID {}. Last code revision: {}'.format(*sys.argv[1:3]))
	if len(sys.argv) > 1:
		print(sys.argv)
		channel = client.get_channel(int(sys.argv[1]))
		print(channel)
		client.send_message(channel, "Hi!")
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
