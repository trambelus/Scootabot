#!/usr/bin/env python3
# em.py - contains emote definitions

from random import choice
import time
hour = lambda: int(time.strftime("%H"))

ALL,NOPE,BYE,ERROR,HI,HUH,YEP = range(7) # like the enum, but top-level
# so we can do emotes.ALL instead of emotes.emote.all

# All Scootaloo emotes (-NSFW ones, banana ones and a few weird ones)
all_emotes = ['1g','20','3g','adoorable','agentscoots','alandsublink','aliloo',
              'angryal','angryscoots','ascootafresh','bindingofscootaloo',
              'blegh','bunnyloo','checkemscoots','cheekyscoots','cheekyscootsghost',
              'chicken','chickendance','chickeneating','confidentscoots',
              'creepaloo','creepingloo','crusadingscoots','cutealoo','damusics',
              'danceofherpeople','darnsquids','depressedscoots','doodoodooscootaloo',
              'easemyscoots','eqgscoots','evilscoot','fuzzygauntlet','gigglingscoots',
              'gonnabeawesome','grinaloo','grumpyscoot','grumpyscoots','hoo1',
              'hoo2','hugs','iamafillyandwhatisthis','ibelieveicanfly',
              'icametowritefanfics','imrainbowdash','iwantit','masterofdrums',
              'mfilly','mspscootaloo','needsmoarsleep','needsmorerainbowdash',
              'nicemoves','notquitedashie','numberonefan','pikaloo','rainbowscootafun',
              'rockaloo','scaredaloo','scaredyscoots','scaredyscoots2','scfear',
              'scootaball','scootabark','scootabass','scootabat','scootabat2',
              'scootabetes','scootabike','scootabite','scootabloom','scootablue',
              'scootablush','scootablush2','scootabop','scootabounce','scootabow',
              'scootabow2','scootabrag','scootabreak','scootabrows','scootabunny',
              'scootabuzz','scootabuzz3','scootabuzzoff','scootacheer','scootacheering',
              'scootachicken','scootachill','scootacloak','scootacomfy','scootacookie',
              'scootacookie2','scootacool','scootacool2','scootacorn','scootacornered',
              'scootacrush','scootacutie','scootaderp','scootaderp2','scootadoctor11',
              'scootadodo','scootadorkable','scootadown','scootadrop',
              'scootaduck','scootaeww','scootafied','scootafine','scootaflex',
              'scootafloor','scootafly','scootafreakout','scootafresh',
              'scootafrown','scootafun','scootaglider','scootagram','scootagrin',
              'scootahail','scootahanging','scootahappy','scootahat',
              'scootaheadbang','scootaheart','scootahey','scootahoodie',
              'scootahug2','scootajeez','scootajew','scootajump','scootajump2',
              'scootajump3','scootajump4','scootalick','scootalk','scootalong',
              'scootaloo','scootaloodle','scootalooisdissapoint','scootaloospeople',
              'scootamap','scootamarch','scootamunch','scootanap','scootannoyed',
              'scootanoms','scootaomg','scootapaper','scootapissed','scootaplease',
              'scootaplotting','scootapoint','scootapoint2','scootapoke','scootapprove',
              'scootapuppyeyes','scootarace','scootaready','scootarear','scootarear2',
              'scootarelax','scootarun','scootasad','scootasad2','scootasad3','scootasad4',
              'scootasaywhat','scootascared','scootascoot','scootascoots','scootaserious',
              'scootashock','scootashocked','scootashrug','scootasing','scootasit',
              'scootasit2','scootasmile','scootasmile2','scootasmug','scootasnooze',
              'scootasocks','scootasorry','scootasquee','scootastand','scootastare',
              'scootastop','scootasure','scootasurprised','scootathanks',
              'scootathat','scootathink','scootatimer','scootatrot','scootatwirl',
              'scootatwirl2','scootatwitch','scootawan','scootawat','scootawhat',
              'scootawhat2','scootawhip','scootawings','scootawink','scootawoo',
              'scootaworried','scootayawn','scootayay','scootayeah','scootayell',
              'scootayes','scootbeyond','scootbrag','scootcane','scootcontent',
              'scootdealwithit','scooteww','scootexcite','scootexcited',
              'scootflip','scoothappy','scootheart','scootidea','scootingscoots',
              'scootired','scootles','scootno','scootperplexity','scootpiano',
              'scootpocker','scootpoutghost','scootreally','scoots','scootsafraid',
              'scootsalute','scootsassin','scootscantholdit','scootscared',
              'scootsdunno','scootshandpizza','scootsscared','scootsseenthings',
              'scoottongue','scootuh','scootuhwhat','scottaloo','scshock',
              'seriouslyruffled','shockedscoots','skeptiloo','skydiverloo',
              'sleepflying','sleepingscoots','smirkaloo','snoozaloo','sparkaloo',
              'squintaloo','stokeloo','supercreepaloo','takemerainbowdash',
              'telegram','uhhh','v41','wetscoots','wolfscoots','wonderscoots',
              'wrongneighborhood','youreawesome','yourock','z47','zz11']
# Emotes to express disagreement or that something is not possible
nope_emotes = ['3g','angryal','confidentscoots','creepingloo','cutealoo','damusics',
        'danceofherpeople','depressedscoots','easemyscoots','evilscoot',
        'gonnabeawesome','ibelieveicanfly','icametowritefanfics','hoo1','hoo2',
        'iamafillyandwhatisthis','letmetellyousomething','masterofdrums',
        'mfilly','notquitedashie','needsmorerainbowdash','nicemoves',
        'scaredaloo','scaredyscoots','scaredyscoots2','scootaball','scootabark','scootabow2',
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
bye_emotes = ['eqgscoots','fuzzygauntlet','hoo1','hoo2','masterofdrums','scootabat',
       'scootabow','scootabuzz3','scootacheer','scootacloak','scootacookie',
       'scootacookie2','scootacutie','scootaderp2','scootadorkable',
       'scootaduck','scootafun','scootahail','scootahanging','scootaheart',
       'scootahug2','scootalick','scootamarch','scootamunch','scootanap','scootanoms',
       'scootaready','scootasit2','scootasmug','scootastand','scootdealwithit',
       'scootheart','skydiverloo','sleepflying','sleepingscoots','snoozaloo',
       'sparkaloo']
# Emotes to display with error messages
error_emotes = ['3g','angryal','bindingofscootaloo','chicken','depressedscoots',
         'icametowritefanfics','needsmorerainbowdash','notquitedashie',
         'scaredyscoots','scootabow2','scootacrush','scootaderp','scootaderp2',
         'scootadown','scootadrop','scootaeww','scootafied','scootafloor',
         'scootafrown','scootahail','scootahat','scootamap','scootapaper',
         'scootaplease','scootasad2','scootasad3','scootasorry','scootasurprised',
         'scootawat','scootawhat','scootawhat2','scootired','scootperplexity',
         'scootreally','scoottongue','scootuh','scottaloo','wetscoots']
# Emotes to greet people
hi_emotes = ['adoorable','alandsublink','confidentscoots','creepaloo','cutealoo',
      'danceofherpeople','eqgscoots','grinaloo','needsmorerainbowdash',
      'scootaball','scootabat','scootabat2','scootabounce','scootabow',
      'scootacheer','scootacookie','scootacookie2','scootadorkable',
      'scootahanging','scootahoodie','scootajump','scootajump3','scootaloodle',
      'scootanoms','scootapoint2','scootaready','scootarear','scootarear2','scootasit',
      'scootasit2','scootasmile','scootasmile2','scootasmug','scootasquee',
      'scootastand','scootasure','scootawink','scootdealwithit','smirkaloo',
      'sparkaloo','telegram','wolfscoots','wonderscoots']
# Emotes to express confusion
huh_emotes = ['fuzzygauntlet','iamafillyandwhatisthis','icametowritefanfics',
       'needsmorerainbowdash','notquitedashie','scootaderp2','scootadodo',
       'scootaeww','scootafrown','scootaplease','scootashrug','scootastare',
       'scootasure','scootasurprised','scootawat','scootawhat','scootawhat2',
       'scootperplexity','scootuh','scootuhwhat']
# Emotes to show agreement towards something
yep_emotes = ['adoorable','confidentscoots','creepingloo','cutealoo','danceofherpeople',
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
    if (eid == ALL):
        ret = choice(all_emotes)
    elif (eid == NOPE):
        ret = choice(nope_emotes)
    elif (eid == BYE):
        ret = choice(bye_emotes)
    elif (eid == ERROR):
        ret = choice(error_emotes)
    elif (eid == HI):
        ret = choice(hi_emotes)
    elif (eid == HUH):
        ret = choice(huh_emotes)
    elif (eid == YEP):
        ret = choice(yep_emotes)
    else: # default case
        ret = choice(nope_emotes)

    return '[](/{})'.format(ret)
    
def get_message(eid, author=None):
  """ Given an emote identifier, return a random message. Doesn't apply to all emotes. """
  current_hour = hour() - 5
  
  if (eid == NOPE):
    ret = choice(["Nope", "Nuh-uh", "No way", "Nah"]) + choice(["", ".", "!"])

  if (eid == YEP):
    ret = choice(["Yep","Yeah","Yes","Uh-huh"]) + choice(["",".","!","!"])

  if (eid == BYE):
    bye_messages = ["Later{}", "Bye{}"]
    if 19 < current_hour or current_hour < 6:
      ret = choice(bye_messages + ["Goodnight{}", "Good night{}", "Sleep well{}", "Have a good sleep{}"]) + "!"
    else:
      ret = choice(bye_messages) + "!"

    if author:
      ret = ret.format(choice(['', ' {}', ', {}']).format(author))
    else:
      ret = ret.format('')

  if (eid == HI):
    hi_messages = ["Hi{}!", "Hey{}!", "Hiya{}!", "What's up{}?"]
    if 6 < current_hour < 12:
      ret = choice(hi_messages + ["Morning{}!", "Good morning{}!"])
    elif 12 < current_hour <= 17:
      ret = choice(hi_messages + ["Afternoon{}!", "Good afternoon{}!"])
    elif 17 < current_hour < 23:
      ret = choice(hi_messages + ["Evening{}!", "Good evening{}!"])
    else:
      ret = choice(hi_messages)

    if author:
      ret = ret.format(choice(['', ' {}', ', {}']).format(author))
    else:
      ret = ret.format('')

  if eid == HUH:
    huh_messages = ["Whah?","Huh?","Whah-huh?","What's that?","Sorry?","What?","Uhhh.."]
    ret = choice(huh_messages)

  return get_emote(eid) + ' ' + ret
