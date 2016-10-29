#!/usr/bin/env python3
# reminder.py - module for reminder commands and threading

import os
import datetime
import threading

def createThread():
  threading.Timer(60.0, checkReminders).start()

def checkReminders():
  createThread()
  print("Checking reminders")