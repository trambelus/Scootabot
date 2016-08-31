#!/usr/bin/env python3

PW_FILE = 'pw.txt'

# Borrowed from /trambelus/UserSimulator
def find_pw(username):
    """ Given a username (email in this case), looks it up in an external file
    and returns the password associated with it. """
    with open(PW_FILE,'r') as f:
        stuff = f.readlines()
        try:
            ret = next(x[1] for x in [t.split('\t') for t in stuff] if x[0] == username).rstrip()
        except StopIteration:
            ret = input("Enter password for {}: > ".format(username))
        return ret
