#!/usr/bin/env python3
# em.py - contains emote definitions

import random
from enum import Enum

emote = Enum('emote', 'all nope bye error hi huh yep')
# All Scootaloo emotes (-NSFW ones)
all_emotes = [ ]
# Emotes to express disagreement or that something is not possible
nope = ['3g','angryal','confidentscoots','creepingloo','cutealoo','damusics',
        'danceofherpeople','depressedscoots','easemyscoots','evilscoot',
        'gonnabeawesome','ibelieveicanfly','icametowritefanfics','hoo1','hoo2',
        'iamafillyandwhatisthis','letmetellyousomething','masterofdrums',
        'mfilly','notquitedashie','needsmorerainbowdash','nicemoves',
        'scaredaloo','scaredyscoots','scaredyscoots2','scootaball','scootabark','scootabow2'
        'scootabreak','scootabuzzoff','scootachill','scootacloak',
        'scootacookie2','scootacool2','scootacornered','scootacrush',
        'scootacutie','scootadodo','scootadown','scootadrop','scootaderp',
        'scootaderp2','scootafloor','scootahey','scootamap','scootapissed',
        'scootasad2','scootasaywhat','scootaserious','scootasmug','scootasorry',
        'scootastare','scootastop','scootasure','scootasurprised',
        'scootathanks','scootathink','scootatrot','scootatwirl2','scootawat',
        'scootawhat','scootawink','scootaworried','scootdealwithit',
        'scootperplexity','scootpocker','scootired','scootscared','scootcontent',
        'scoottongue','scootuh','scootuhwhat','shockedscoots',
        'wetscoots']
# Emotes to say goodbye
bye = ['eqgscoots','fuzzygauntlet','hoo1','hoo2','masterofdrums','scootabat',
       'scootabow','scootabuzz3','scootacheer','scootacloak','scootacookie',
       'scootacookie2','scootacutie','scootaderp2','scootadorkable',
       'scootaduck','scootafun','scootahail','scootahanging','scootaheart',
       'scootahug2','scootalick','scootamarch','scootamunch','scootanap','scootanoms',
       'scootaready','scootasit2','scootasmug','scootastand','scootdealwithit',
       'scootheart','skydiverloo','sleepflying','sleepingscoots','snoozaloo',
       'sparkaloo']
# Emotes to display with error messages
error = ['3g','angryal','bindingofscootaloo','chicken','depressedscoots',
         'icametowritefanfics','needsmorerainbowdash','notquitedashie',
         'scaredyscoots','scootabow2','scootacrush','scootaderp','scootaderp2',
         'scootadown','scootadrop','scootaeww','scootafied','scootafloor',
         'scootafrown','scootahail','scootahat','scootamap','scootapaper',
         'scootaplease','scootasad2','scootasad3','scootasorry','scootasurprised',
         'scootawat','scootawhat','scootawhat2','scootired','scootperplexity',
         'scootreally','scoottongue','scootuh','scottaloo','wetscoots']
# Emotes to greet people
hi = ['adoorable','alandsublink','confidentscoots','creepaloo','cutealoo',
      'danceofherpeople','eqgscoots','grinaloo','needsmorerainbowdash',
      'scootaball','scootabat','scootabat2','scootabounce','scootabow',
      'scootacheer','scootacookie','scootacookie2','scootadorkable',
      'scootahanging','scootahoodie','scootajump','scootajump3','scootaloodle',
      'scootanoms','scootapoint2','scootaready','scootarear','scootarear2','scootasit',
      'scootasit2','scootasmile','scootasmile2','scootasmug','scootasquee',
      'scootastand','scootasure','scootawink','scootdealwithit','smirkaloo',
      'sparkaloo','telegram','wolfscoots','wonderscoots']
# Emotes to express confusion
huh = ['fuzzygauntlet','iamafillyandwhatisthis','icametowritefanfics',
       'needsmorerainbowdash','notquitedashie','scootaderp2','scootadodo',
       'scootaeww','scootafrown','scootaplease','scootashrug','scootastare',
       'scootasure','scootasurprised','scootawat','scootawhat','scootawhat2',
       'scootperplexity','scootuh','scootuhwhat']
# Emotes to show agreement towards something
yep = ['adoorable','confidentscoots','creepingloo','cutealoo','danceofherpeople',
       'eqgscoots','grinaloo','hoo1','hoo2','iwantit','numberonefan','scootabat',
       'scootabat2','scootabite','scootabloom','scootabow','scootabuzz',
       'scootabuzz3','scootachill','scootacloak','scootacookie','scootacool2',
       'scootacutie','scootadorkable','scootagrin','scootaheart','scootahoodie',
       'scootajump2','scootajump3','scootajump4','scootamarch','scootamunch',
       'scootaplotting','scootapoint','scootapoint2','scootapprove','scootarear',
       'scootarear2','scootasit','scootasmile','scootasmug','scootasquee',
       'scootastand','scootathink','scootdealwithit','scootexcited','scoothappy',
       'smirkaloo']

def get_emote(eid):
    """ Given an emote identifier it will give a corresponding, randomly generated emote """
    if (eid == emotes.all):
        return random.choice(all_emotes)
    elif (eid == emotes.nope):
        return random.choice(nope)
    elif (eid == emotes.bye):
        return random.choice(bye)
    elif (eid == emotes.error):
        return random.choice(error)
    elif (eid == emotes.hi):
        return random.choice(hi)
    elif (eid == emotes.huh):
        return random.choice(huh)
    elif (eid == emotes.yep):
        return random.choice(yep)
    else:
        return "invalid emote selection"
    
