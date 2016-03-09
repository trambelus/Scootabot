#!/usr/bin/env python3

# Global imports
import discord
import logging
import sys
import os # for script restarts
import re # for command processing, later
import traceback
import subprocess
import time
# Local imports
import derpi
import emotes
import auth

logging.basicConfig(level=logging.INFO)

EMAIL = 'hawke252.reddit@gmail.com'

client = discord.Client()

def restart(channel_id):
	if os.name == 'nt':
		logging.info(sys.argv[0])
		subprocess.Popen(' '.join(["python", sys.argv[0], str(channel_id)]))
		client.logout()
		sys.exit(0)
	elif os.name == 'posix':
		ex = os.execl(sys.argv[0], str(channel_id))
	else:
		logging.error("Unknown OS {}, could not restart".format(os.name))

class Command:
	def __init__(self, message):
		self.message = message
		self.command = message.content.lower()

	def process(self):
		try:
			if self.command.startswith('!reload'):
				restart(self.message.channel.id)
			if self.command.startswith('!stop'):
				client.send_message(self.message.channel, "Stopping!")
				sys.exit(0)
		except SystemExit:
			print("sys.exit called")
			sys.exit(0)
		except:
			exc = traceback.format_exc()
			client.send_message(self.message.channel, "[](/notquitedashie) ```{}```".format(exc))
			print(exc)

	def get_response(self):
		if self.command.startswith('!derpi'):
			return derpi.process(self.message)


@client.event
def on_ready():
	# Restart info should be in sys.argv
	if len(sys.argv) == 3:
		logging.info('Launched with client ID {}. Last code revision: {}'.format(*sys.argv[1:3]))
	if len(sys.argv) > 1:
		print(sys.argv)
		channel = client.get_channel(sys.argv[1])
		print(channel)
		client.send_message(channel, "Hi!")

@client.event
def on_message(message):
	if message.author != client.user:
		logging.info("{} said: {}".format(message.author, message.content))

		cmd = Command(message=message)
		cmd.process()
		response = cmd.get_response()

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
