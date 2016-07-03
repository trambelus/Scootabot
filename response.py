#!/usr/bin/env python3
#  Response.py: given text, return a response.

import nltk
import random
import re

import emotes

nicknames = {
    '134968288772882432': ['Hawkaloo', 'Hawke', 'Hawkey', 'Hawkey Hawke'],
    '136190686230741002': ['Trambles', 'Trambelus', 'Trambuck', 'Buck', 'Applebuck', 'Applepone', 'Best Apple'],
    '110932722322505728': ['Woof', 'Woofy', 'Ian', 'Woofy Woof', 'Best Woof'],
    '166229158681247753': ['Carbon', 'Dragon', 'Carburd', 'Best Dragon'],
    'any': ['Sexy', 'Butts' ]
}

# Answer a general-purpose question with yes, no, or huh?
def question_general():
    ret = ""
    chance = random.randint(0, 98)
    if (chance < 34):
        ret = emotes.get_message(emotes.YEP)
    elif (34 <= chance < 67):
        ret = emotes.get_message(emotes.NOPE)
    else:
        ret = emotes.get_message(emotes.HUH)
    return ret

# Answer a question asking for a choice to be made.
def question_which(text):
    if not re.search(r'[^\w]or\s', text):
        return None
    words = nltk.word_tokenize(text)
    pos = nltk.pos_tag(words)
    idx = words.index('or')
    choices = []
    
    def read_choice(i, mod):
        choice = []
        if pos[i][1] == ',':
            i -= 1
        while True:
            tr = (pos[i][1][:2] if 0 <= i < len(pos) else '')
            if tr in ['JJ', 'NN', 'DT', 'RB']:
                if mod > 0:
                    choice.append(words[i])
                else:
                    choice.insert(0,words[i])
            else:
                choice = ' '.join(choice)
                if len(choice) > 0:
                    choice = choice[0].upper() + choice[1:]
                    choices.append(choice)
                if tr == ',':
                    return i
                return None
            i += mod
    i = idx
    read_choice(i+1, 1)
    while i != None:
        i = read_choice(i-1,-1)
    if len(choices) == 0:
        return emotes.get_message(emotes.HUH)
    return "{} {}!".format(emotes.get_emote(emotes.YEP), random.choice(choices))

    #capture_words = re.compile("(\w[\w']*\w|\w)")
    #words = capture_words.findall(text)
    #choices = re.search(r"((\w+,[^\w]+)+|\w+[^\w]+)or[^\w]\w+", text).group(0).replace(', or ',', ').split(', ')

def default():
    return "no u"

# TODO: make this a class to make parameter-sharing less awkward
# Hawke was right from the first
def respond(command):
    response = ""

    if re.search(r'(^| )(hi|hello|hey|hi there|hiya|heya|howdy)(! |, | )scootabot', command.text):
        #author = re.search('(^| )\w+( ♀)?$', command.message.author.name).group().strip().title()
        #ret = emotes.get_message(emotes.HI, author)
        chance = random.randint(0, 10)

        #if (chance < 7):
        #    response = emotes.get_message(emotes.HI, random.choice(nicknames[command.message.author.id]))
        #elif (7 <= chance < 9):
        response = emotes.get_message(emotes.HI, command.message.author.nick)
        #else:
        #    response = emotes.get_message(emotes.HI, random.choice(nicknames['any']))
    elif ("?" in command.text):
        response = question_which(text)
        if response == None:
            response = question_general()
    else:
        response = default()

    return response

