#!/usr/bin/env python3

import discord
import logging
import derpibooru
import random

logging.basicConfig(level=logging.INFO)

EMAIL = 'hawke252.reddit@gmail.com'
PW_FILE = 'pw.txt'

nope_em = ['3g','angryal','confidentscoots','creepingloo','cutealoo','damusics','danceofherpeople',
	'depressedscoots','easemyscoots','evilscoot','gonnabeawesome','ibelieveicanfly','icametowritefanfics',
	'hoo1','hoo2','iamafillyandwhatisthis','letmetellyousomething','mfilly','notquitedashie','needsmorerainbowdash',
	'nicemoves','scaredaloo','scaredyscoots','scaredyscoots2','scootaball','scootabreak','scootabuzzoff','scootachill',
	'scootacloak','scootacookie2','scootacool2','scootacornered','scootacrush','scootacutie','scootadodo','scootadown',
	'scootadrop','scootaderp','scootaderp2','scootafloor','scootahey','scootamap','scootapissed','scootasad2','scootasaywhat',
	'scootaserious','scootasmug','scootasorry','scootastare','scootasure','scootathanks','scootathink','scootatrot',
	'scootatwirl2','scootawat','scootawhat','scootawink','scootaworried','scootperplexity','scootired','scootscared',
	'scootcontent','scoottongue','shockedscoots','sparkaloo', 
	'masterofdrums', 'scootastop', 'scootasurprised', 'scootuh', 'scootuhwhat', 'wetscoots'] # Unsorted, emotes Hawke added

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

def derpi(query, highvoted=True):
	print(query)
	s = derpibooru.search.Search(key=find_pw('derpibooru'), sf='random',
		q=set(query))
	i = next(s)
	while highvoted and i.upvotes < 100:
		i = next(s)
	return i.full + '\n' + i.url

@client.event
def on_ready():
    print('Ready!')

@client.event
def on_message(message):
	if message.author != client.user:
		print("{} said: {}".format(message.author, message.content))
		msg = message.content.lower()
		if msg.startswith('!scootabot') or msg.startswith('!derpi'):
			words = [s.strip() for s in message.content.lower().split(' ',maxsplit=1)]
			if len(words) == 1:
				tags = []
			else:
				tags = words[1].split(',')
			if "nsfw" not in message.channel.name:
				tags.append("safe")
			try:
				response = derpi(tags)
				client.send_message(message.channel, response)
			except StopIteration:
				try:
					response = derpi(tags, highvoted=False)
					client.send_message(message.channel, response)
				except StopIteration:
					client.send_message(message.channel, "[](/{}) Nope.".format(random.choice(nope_em)))

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
