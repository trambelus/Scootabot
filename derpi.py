#!/usr/bin/env python3
# derpi.py - module for derpibooru commands

import derpibooru
import random
import emotes

def search(query, highvoted=True):
	print(query)
	s = derpibooru.search.Search(key=find_pw('derpibooru'), sf='random',
		q=set(query))
	i = next(s)
	while highvoted and i.upvotes < 100:
		i = next(s)
	return i.full + '\n' + i.url

def process(message):
	words = [s.strip() for s in message.lower().split(' ',maxsplit=1)]
	if len(words) == 1:
		tags = []
	else:
		tags = words[1].split(',')
	if "nsfw" not in message.channel.name:
		tags.append("safe")
	try:
		response = search(tags)
		return response
	except StopIteration:
		try:
			response = search(tags, highvoted=False)
			return response
		except StopIteration:
			return "[](/{}) Nope.".format(random.choice(emotes.nope))
