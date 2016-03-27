#!/usr/bin/env python3
# msg_db.py - Stores incoming messages to sqlite

import sqlite3

DB_FILE = 'msg_db.db3'

class MessageDB:
	def __init__(self):
		self.db = sqlite3.connect(DB_FILE)
		self.db.execute("""CREATE TABLE IF NOT EXISTS messages""") # TODO

	def store(self, msg):
		# TODO
		author = msg.author.id # or .name?
		server = msg.server.id # .name? maybe a different table for these?
		channel = msg.channel.id # same as above

		ts = msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
		cont 

		self.db.execute("""INSERT INTO messages ()""") # TODO
		self.db.commit()