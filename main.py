#!/usr/bin/env python3

# Global imports
import discord
import logging
import sys
import os # for script restarts
import subprocess
import traceback
import git
import asyncio

import time
import re
import random

# Local imports
import derpi
import emotes
import auth
import response

logging.basicConfig(level=logging.INFO, filename=time.strftime('logs/%Y-%m-%d_%H.%M.%S.log'))

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
        self.text = message.content.lower()

    def process(self):
        ret = None

        try:
            if self.text == '!reload':
                ret = restart(self.message.channel.id)
                # Only returns this if a restart isn't happening

            elif self.text == '!force-reload':
                restart(self.message.channel.id, force=True)

            elif self.text == '!stop':
                # Broken call
                #client.send_message(self.message.channel, emotes.get_message(emotes.BYE))
                sys.exit(0)

            elif self.text.startswith('!derpi ') or self.text == '!derpi':
                ret = derpi.process(self.message)
                self.last_command[self.message.author.id + ':' + self.message.channel.id] = self.text

            elif self.text == '!again':
                if (self.message.author.id + ':' + self.message.channel.id) in self.last_command:
                    self.text = self.last_command[self.message.author.id + ':' + self.message.channel.id]
                    self.message.content = self.last_command[self.message.author.id + ':' + self.message.channel.id]
                    return self.process()
                else:
                    ret = emotes.get_message(emotes.HUH)

            elif 'scootabot' in self.text:

                if 'roll' in self.text:
                    search_res = re.search(r'\d*d(\d+)(\s*\+\s*\d+)?', self.text)
                    if not search_res:
                        return

                    roll = [1 if e == '' else int(e) for e in search_res.group(0).replace(' ','').replace('d','+').split('+')]

                    dice = [random.randint(1, roll[1]) for _ in range(roll[0])]
                    if len(roll) == 3:
                        dice += [roll[2]]

                    if len(roll) == 2:
                        ret = "{}\n _Rolling {}d{}:_\n**{}**".format(
                            emotes.get_emote(emotes.YEP),
                            roll[0],
                            " + ".join(map(str,roll[1:])),
                            sum(dice)
                        )
                    else:
                        ret = "{}\n _Rolling {}d{}:_\n  {}\n**={}**".format(
                            emotes.get_emote(emotes.YEP),
                            roll[0],
                            " + ".join(map(str,roll[1:])),
                            " + ".join(map(str,dice)),
                            sum(dice)
                        )

                else:
                    ret = response.respond(self)
                #elif 'thanks' in self.text:
                #    ret = "{} {}".format(emotes.get_emote(emotes.YEP), "You're welcome!")

                #elif self.text[-1] == "!":
                #    ret = emotes.get_message(emotes.YEP)

                #elif self.text[-1] == "?":
                #    ret = emotes.get_message(emotes.NOPE)

            # elif 'scootabot' in self.text and 'hawke' in self.text and 'favorite pon' in self.text:
            #     ret = emotes.get_emote(emotes.YEP) + ' Twist!'

            #if re.search(r'(^| )(hi|hello|hey|hi there|hiya|heya|howdy)(! |, | )scootabot', self.text):
            #    author = re.search('(^| )\w+( ♀)?$', self.message.author.name).group().strip().title()
            #    ret = emotes.get_message(emotes.HI, author)

        except SystemExit:
            print("sys.exit called")
            sys.exit(0)

        except:
            exc = traceback.format_exc()
            # Broken call
            #client.send_message(self.message.channel, "[](/notquitedashie) ```{}```".format(exc))
            print(exc)

        return ret


@client.event
@asyncio.coroutine
def on_ready():
    # Restart info should be in sys.argv
    if len(sys.argv) == 3:
        logging.info('Launched with client ID {}. Last code revision: {}'.format(*sys.argv[1:3]))
    if len(sys.argv) > 1:
        print(sys.argv)
        channel = client.get_channel(sys.argv[1])
        print(channel)
        yield from client.send_message(channel, emotes.get_message(emotes.HI, random.choice(["all","everyone","everybody","folks","guys","y'all"])))
    logging.info("Ready!")
    logging.debug("Launched with args {}".format(sys.argv))

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author != client.user:
        logging.info(" {} said: {}".format(message.author, message.content))

        cmd = Command(message=message)
        response = cmd.process()

        if response:
            yield from client.send_message(message.channel, response)

def main():

    password = auth.find_pw("discord")

    #yield from client.login(EMAIL, password)
    client.run(password) # enter main loop

if __name__ == '__main__':
    main()

# TODO:
# Keep search object handle for !again
