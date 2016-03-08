#!/usr/bin/env python3

# Global imports
import discord
import logging
import sys
import os # for script restarts
import re # for command processing, later
# Local imports
import derpi
import emotes
import time

logging.basicConfig(level=logging.INFO)

EMAIL = 'hawke252.reddit@gmail.com'
PW_FILE = 'pw.txt'

client = discord.Client()

# Borrowed from /trambelus/UserSimulator
def find_pw(username):
	""" Given a username (email in this case), looks it up in an external file
	and returns the password associated with it. """
	with open(PW_FILE,'r') as f:
		stuff = f.readlines()
		try:
			ret = next(x[1] for x in [t.split('\t') for t in stuff] if x[0] == username).rstrip()
		except StopIteration:
			raise LookupError("User not found: %s" % username)
		return ret

def restart(channel_id):
	if os.name == 'nt':
		os.spawnl(os.P_NOWAIT, sys.argv[0], channel_id)
		client.logout()
		sys.exit(0)
	elif os.name == 'posix':
		ex = os.execl(sys.argv[0], channel_id)
	else:
		logging.error("Unknown OS {}, could not restart".format(os.name))

class Command:
	def __init__(self, message):
		self.message = message
		self.command = message.content.lower()

	def process(self):
		if self.command.startswith('!reload'):
			restart(self.message.channel.id)
		if self.command.startswith('!stop'):
			client.send_message(self.message.channel, "Stopping!")
			sys.exit(0)

	def get_response(self):
		if self.command.startswith('!derpi'):
			return derpi.process(self.message)


@client.event
def on_ready():
	# Restart info should be in sys.argv
    if len(sys.argv) == 3:
    	logging.info('Launched with client ID {}. Last code revision: {}'.format(*sys.argv[1:3]))
    	channel = client.get_channel(int(sys.argv[1]))
    	client.send_message(channel, "Restarted!")

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
	try:
		password = find_pw(EMAIL)
	except LookupError:
		password = input("Enter password for {}: > ".format(EMAIL))
	
	client.login(EMAIL, password)
	client.run() # enter main loop

if __name__ == '__main__':
	main()

# TODO:
# Keep search object handle for !again
