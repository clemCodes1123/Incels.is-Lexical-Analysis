#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 01:18:13 2023

@author: clemmie
"""
from empath import Empath


lexicon = Empath()
categories = lexicon.cats
#print(categories)



CATEGORY_NAMES = {
 1: 'misogyny',
 2: 'flipping_the_narrative_injustice_victimhood_persecution',
 3: 'homophobia',
 4: 'violence',
 5: 'sexual_violence',
 6: 'racism_white_supremacy',
 7: 'high_divergence_incel_lexicon',
 8: 'martyrdom', 
 9: 'sex_sexuality', 
 10:'appearance'
}



#1

category_one = lexicon.create_category("misogyny",['misogyny', 'slut', 'whore', 
    'stupid woman', 'bitch', 'slag', 'dumbbitch'], model="reddit")
                                               

category_one = lexicon.cats['misogyny']

lexicon.cats['misogyny'].extend(['misogyny','b00bs', 'becky', 'big ass', 'bint', 
    'bints', 'bird', 'birds', 'boob', 'boobies', 'boobs', 'booobs', 'boooobs',
    'booooobs', 'booooooobs', 'camel toe', 'chesticles', 'cock waffle', 'dumb', 'dumbass', 'f4nny',
    'fanny', 'fannyflaps', 'female', 'femoid', 'fho', 'fugly', 'funfuck', 'muff', 'pearlnecklace', 'peehole',
    'pissflaps', 'poon', 'poonani', 'poontang', 'pornprincess', 'pua', 'puntang', 'puss', 'pussylips', 'roastie',
    'shit heel', 'shit heels', 'skin flute', 'smv', 'snowflake', 'spermhearder', 'spermherder',
    'stacy', 't1tt1e5', 't1tties', 'tittie', 'titties', 'titty', 'tittyfuck', 'unfuckable', 'va-j-j', 'b!tch', 'b17ch', 'b1tch', 'bad fuck', 'beaver', 'bi+ch', 'biatch', 'big butt', 'bitch', 'bitch ass', 'bitcher', 'bitchers', 'bitches', 'bitchtits', 'bite me',
'brotherfucker', 'byatch', 'clitface', 'cockblocker', 'cockmaster', 'cockmongler', 'cocknose', 'cocknugget', 'conchuda', 'conchudas', 'coochie', 'coochy', 'crotchrot',
'cum bubble', 'cum guzzler', 'cum jockey', 'cum tart', 'cumdumpster', 'cumquat', 'cumqueen', 'cumslut', 'cunt',
'cunt rag', 'cuntass', 'cuntface', 'cuntfuck', 'cunthole', 'cuntlick', 'cunts', 'cuntslut', 
'dick beaters', 'dicktickler', 'dumbbitch', 'fastfuck', 'fatass', 'felcher', 'feltcher', 'finger fucker', 'fingerfuckers',
'fist fuck', 'fistfucker', 'footfucker', 'fucka', 'fuckable', 'fuckass', 'fuckbag', 'fuckbrain',
'fuckbuddy', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead',
'fuckher', 'fuckina', 'fuckingbitch', 'fuckit', 'fuckknob', 'fuckpig', 'fucktard', 'fuckup',
'fuckwhore', 'fuckyou', 'gangbanger', 'gash', 'gashes', 'greaseball', 'hicks', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'hoes', 'honkey', 'honky',
'hore', 'hos', 'hurt', 'hussy', 'idiot', 'idiots', 'intimidate', 'jackass', 'kunt', 'l3i+ch', 'l3itch', 'milf', 'minge', 'pu55i', 'pu55y',
'punish', 'pusse', 'pussi', 'pussie', 'pussies', 'pussy', 'pussys', 'pusy', 'queerhole', 'rentafuck', 'scag', 'scags', 'scumbag', 'seppo', 'seppos', 'skag', 'skags', 'skank',
'skank bitch', 'skank fuck', 'skank whore', 'skanky', 'skanky bitch', 'skanky whore', 'skullfuck', 'slag',
'slags', 'slit', 'slits', 'slut', 'slut wear', 'slut whore', 'slutbag', 'sluts', 'slutt', 'slutting', 'slutty',
'slutwhore', 'smear', 'snatch', 'suckme', 'suckmytit', 'thrust', 'titfucker', 'titfuckin', 'trailertrash', 'trisexual',
'tw4t', 'twat', 'twathead', 'twats', 'twatty', 'twatwaffle', 'twobitwhore', 'twunt', 'twunter',
'whoar', 'whore', 'whore from fife','whore from fifes', 'whorefucker', 'whores', 'williewanker', 'hole', 'holes', 'toilet', 'toilets', 'cum dumpster'])

print(category_one)

#2

category_two = lexicon.create_category("flipping_the_narrative_injustice_victimhood_persecution",
    ['beta', 'mgtow', 'mra', 'normie', 'overthrow', 'prevail', 'vanquish', 
     'gynocracy', 'hypergamy', 'hypergamous'], model="reddit")
                                                                                                  
category_two = lexicon.cats['flipping_the_narrative_injustice_victimhood_persecution']

lexicon.cats['flipping_the_narrative_injustice_victimhood_persecution'].extend(['beta', 
    'mgtow', 'mra', 'normie', 'overthrow', 'prevail', 'vanquish', 'gynocracy', 
    'hypergamy', 'hypergamous', 'amog', 'betabuxx', 'compel', 'oblige', 'omega', 
    'overwhelm', 'subjugate', 'suppress', 'mistreatment', 'subhuman'])

print(category_two)


#3

category_three = lexicon.create_category("homophobia",['homo', 'fag', 'fagfucker', 
    'fagging', 'faggitt', 'faggot', 
    'faggs', 'fagot', 'fagots', 'fags', 'lezbo', 'dyke', 'cocksucker'], model="reddit")


category_three = lexicon.cats['homophobia']

lexicon.cats['homophobia'].extend(['analannie', 'ass cowboy', 'ass jacker', 
    'ass whore', 'ass-assinate', 'ass-jabber', 'ass-pirate', 'assbandit',
    'assbanger', 'assblaster', 'assfuck', 'assfucker', 'asshopper', 'assklown', 'asslick', 'asslicker', 'assman',
    'asspacker', 'asspuppy', 'assranger', 'asssucker', 'backdoor man', 'ball licker', 'bulldike', 'bulldyke',
    'bunny fucker', 'butchdyke', 'butt fucker', 'butt pirate', 'buttbang', 'buttfuck', 'buttfucka', 'buttpirate',
    'c0cksucker', 'carpet muncher', 'cock cowboy', 'cock jockey', 'cock licker', 'cock smoke', 'cock suck',
    'cock-sucker', 'cockmunch', 'cockmuncher', 'cockqueen', 'cockrider', 'cocksman', 'cocksmith', 'cocksmoker',
    'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka',
    'cokmuncher', 'coksucka', 'cuntfucker', 'cuntlick', 'cuntlicker', 'cuntlicking', 'dick licker', 'dickfuck',
    'dickfucker', 'dicklick', 'dickman', 'dickmonger', 'dicksucker', 'dyke', 'dyke jumper', 'dyke jumpers', 'dykes',
    'fag', 'fagfucker', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny fucker',
    'fannyfucker', 'fingerfucker', 'fingerfuckers', 'fistfucker', 'fistfuckers', 'fudge packer', 'fudgepacker',
    'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'homo',
    'muffdive', 'muffindiver', 'mufflikcer', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'penisbanger',
    'penisfucker', 'penispuffer', 'polesmoker', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylicking',
    'pussylover', 'pussypounder', 'queer', 'queers', 'rimjaw', 'sodomite', 'lez', 'lezbo', 'lezz', 'lezzie', 
    'lezzo', 'trannysisters'])


print(category_three)


#4

category_four = lexicon.create_category("violence",['annihilate', 'assail', 
    'assassinate', 'assault', 'attack', 'bang', 'batter', 'blast',
    'bruise', 'brutalise', 'burn', 'bust', 'butcher', 'carry off', 'choke', 'clobber', 'concuss', 'constrain',
    'crack', 'crush', 'cut', 'decimate', 'demolish', 'destroy', 'dispose of', 'drown', 'enslave',
    'exterminate', 'finish off', 'flagellate', 'force', 'gag', 'hit', 'jump', 'kick', 'kill', 'lock up', 'maul',
    'murder', 'obliterate', 'pelt', 'pounce upon', 'pummel', 'punch', 'raid', 'ram', 'shake', 'shake down',
    'shoot ', 'shove', 'slam', 'slap', 'slaughter', 'slog', 'smack', 'smash', 'smother', 'stab', 'strangle',
    'strike', 'strong-arm', 'thrash', 'thresh', 'thwack', 'trample', 'trounce', 'vaporize', 'wallop', 'whip', 
    'kill', 'rope', 'kys', 'roping', 'shoot', 'shooting', 'kill', 'killed', 'killing', 'nuke', 'rape', 'raped', 
    'raping', 'beating', 'hang', 'hanged', 'attack', 'attacks', 'gun', 'guns', 'assault', 'hurt', 'shot', 'punch', 
    'revenge', 'murder', 'behead'], model="reddit")

category_four = lexicon.cats['violence']

lexicon.cats['violence'].extend(['annihilate', 'assail', 'assassinate', 'assault', 
                'attack', 'bang', 'batter', 'blast', 'block', 'bring down',
    'bruise', 'brutalise', 'burn', 'bust', 'butcher', 'carry off', 'choke', 'clobber', 'concuss', 'constrain',
    'crack', 'crush', 'cut', 'decimate', 'demolish', 'destroy', 'dispose of', 'drown', 'enslave', 'er',
    'exterminate', 'finish off', 'flagellate', 'force', 'gag', 'hit', 'jump', 'kick', 'kill', 'lock up', 'maul',
    'murder', 'obliterate', 'pelt', 'plunk', 'pounce upon', 'pummel', 'punch', 'raid', 'ram', 'shake', 'shake down',
    'shoot ', 'shove', 'slam', 'slap', 'slaughter', 'slog', 'smack', 'smash', 'smother', 'stab', 'strangle',
    'strike', 'strong-arm', 'torture', 'thrash', 'thresh', 'thwack', 'trample', 'trounce', 'vaporize', 'wallop', 'whip', 'ER', 'elliot rodgers', 'kill', 'rope', 'kys', 'roping', 'shoot', 'shooting', 'kill', 'killed', 'killing', 'nuke', 'rape', 'raped', 'raping', 'beating', 'hang', 'hanged', 'attack', 'attacks', 'gun', 'guns', 'assault', 'hurt', 'shot', 'punch', 'revenge', 'murder', 'behead'])

print(category_four)


#5

category_five = lexicon.create_category("sexual_violence",['sexual violence', 
    'gangbang', 'gangbanged', 'gangbangs', 'incest', 'pedo', 'underage', 'insest', 
    'lolita', 'molest', 'molestation', 'pound', 'rape', 'raped', 'raping', 
    'sodomise', 'sodomize', 'spank', 'unclefucker', 'virginbreaker', 'choke', 
    'gangrape', 'force'], model="reddit")

category_five = lexicon.cats['sexual_violence']

lexicon.cats['sexual_violence'].extend(['sexual violence', 'cherry popper', 
    'clitfuck', 'cock block', 'cock carousel', 'cock tease', 'conquer', 'gangbang', 'gangbanged',
    'gangbangs', 'incest', 'infiltrate', 'insest', 'lolita', 'molest', 'molestation', 
    'pound', 'rape', 'raped', 'raping', 'sodomise', 'sodomize', 'spank', 'unclefucker', 
    'virginbreaker', 'choke', 'gangrape'])

print(category_five)


#6

category_six = lexicon.create_category("racism_white_supremacy",['racism', 
    'slur', 'nigger', 'kike', 'new world order', 'NWO', 'jews', 'goy',
    'coon', 'nigga','slant', 'slant eye', 'slant eyes', 'chink', 'monkey'], model="reddit")
   

category_six = lexicon.cats['racism_white_supremacy']

lexicon.cats['racism_white_supremacy'].extend(['abbo', 'abbos', 'abo', 'abos', 
    'african catfish', 'african catfishes', 'african forklift', 'africoon',
    'africoons', 'afro-saxon', 'afro-saxons', 'albino', 'albinos', 'alligator bait', 'alligator baits', 'americoon',
    'americoons', 'amo', 'amos', 'anglo', 'anglos', 'arab', 'argie', 'argies', 'armo', 'armos', 'assnigger',
    'aunt jemima', 'aunt jemimas', 'banana bender', 'banana benders',
    'banana lander', 'banana landers', 'banjo lips', 'bans and cans',
    'bean dipper', 'bean dippers', 'beaner', 'beaner shnitzel', 'beaner shnitzels', 'beaners', 'beaney', 'beanies',
    'bhrempti', 'bhremptis', 'bigger', 'bix nood', 'bix noods', 'black', 'black barbie', 'black barbies',
    'black dago', 'black dagos', 'blaxican', 'blaxicans', 'bluegum', 'bluegums', 'bog hopper', 'bog hoppers',
    'bog irish', 'bog irishes', 'bog jumper', 'bog jumpers', 'bog trotter', 'bog trotters', 'bohunk', 'booner',
    'booners', 'boong', 'boonga', 'boongas', 'boongs', 'boonie', 'boonies', 'border bunnies', 'border bunny',
    'border hoppers', 'buckethead', 'bucketheads', 'buckra', 'buckras',
    'buk buk', 'buk buks', 'bung', 'bunga', 'bungas', 'bungs', 'burrhead', 'burrheads',
    'camel cowboies', 'camel cowboy', 'camel fucker', 'camel fuckers', 'camel humper', 'camel humpers',
    'camel jacker', 'camel jackers', 'camel jockey', 'can eater', 'can eaters', 'canuck', 'carpet pilot',
    'carpet pilots', 'carrot snapper', 'carrot snappers', 'caublasian', 'caublasians', 'charva', 'charvas', 'chigger', 'chiggers', 'chili shitter', 'chili shitters', 'chinaman',
    'chinc', 'chinese wetback', 'chinese wetbacks', 'ching chong', 'ching chongs', 'chinig', 'chinigs', 'chink', 'chinks', 'chinky', 'chonkies', 'chonky', 'christ killer', 'christ killers',
    'chug', 'chugs', 'clamhead', 'clamheads', 'clog wog', 'coolie', 'coolies', 'coon', 'coondog', 'coons',
    'cow kisser', 'cow kissers', 'cowboy killer', 'cowboy killers', 'cracker', 'crackers', 'cunteyed',
    'curry', 'cushi', 'cushis', 'cushite', 'cushites',
    'dago', 'dagos', 'darkey', 'darkie', 'darkies', 'darky', 'dego', 'degos', 'diaper head', 'diaper heads',
    'dinge', 'dinges', 'dogun', 'doguns', 'dot head', 'dot heads', 'eskimo', 'eyetie', 'eyeties', 'fob', 'fobs', 'fresh off the boat', 'fresh off the boats', 'gator bait', 'gator baits', 'gerudo', 'gerudos',
    'gew', 'gews', 'ghetto hamster', 'ghetto hamsters', 'gin jockey', 'gin jockies', 'ginzo', 'ginzos', 'gipp',
    'gippo', 'gippos', 'gipps', 'gipsy', 'golliwog', 'golliwogs', 'gook', 'gook eye', 'gook eyes', 'gookies',
    'gooks', 'gooky', 'goy', 'goyim', 'greaser', 'greasers', 'gringo', 'groid', 'groids', 'guala guala',
    'guala gualas', 'gub', 'gubba', 'gubbas', 'gubs', 'guido', 'guidos', 'gurrier', 'gurriers', 'gwat', 'gwats',
    'gyppie', 'gyppies', 'gyppy', 'gypsy', 'hairyback', 'hairybacks', 'half-breed', 'half-caste', 'halfrican',
    'halfricans', 'haole', 'hapa', 'hebe', 'hebes', 'hebro', 'hebros', 'heeb', 'heebs', 'heinie', 'heinies',
    'higger', 'higgers', 'hindoo', 'hodgie', 'honyak', 'honyaks', 'honyock', 'honyocks', 'hoosier', 'hoosiers',
    'hun', 'hunkie', 'hunkies', 'hunky', 'huns', 'hunyak', 'hunyaks', 'hunyock', 'hunyocks', 'hymie', 'hymies',
    'ice monkey', 'ice monkies', 'ike', 'ikes', 'ikey', 'ikey mo', 'ikey mos', 'ikies',
    'iky', 'injun', 'injuns', 'jant', 'jants', 'jap', 'japie', 'japies', 'japs',
    'jewbacca', 'jewbaccas', 'jhant', 'jhants', 'jig', 'jiga', 'jigaboo', 'jigarooni', 'jigaroonis', 'jigg',
    'jigga', 'jiggabo', 'jiggabos', 'jiggas', 'jigger', 'jiggers', 'jiggs', 'jigs', 'jijjiboo', 'jijjiboos',
    'jimfish', 'jockie', 'jockies', 'jocky', 'junglebunny', 'kaffir', 'kafir', 'khazar', 'khazars', 'kike', 'kikes',
    'kotiya', 'kotiyas', 'kraut', 'krauts', 'kushi', 'kushis', 'kushite', 'kushites', 'kyke', 'kykes', 'latrino',
    'latrinos', 'lawn jockey', 'lawn jockies', 'leb', 'lebbo', 'lebbos', 'lebs', 'lemonhead', 'lemonheads',
    'leprechaun', 'leprechauns', 'ling ling', 'ling lings', 'lowlander', 'lowlanders', 'lubra', 'lubras', 'lugan',
    'lugans', 'makwerekwere', 'mammy', 'mangia cake', 'mangia cakes', 'mick', 'micks', 'mockey', 'mockie',
    'mockies', 'mocky', 'moke', 'mokes', 'mokies', 'moky', 'mook', 'mooks', 'mooncricket', 'moss eater',
    'moss eaters', 'mosshead', 'mossheads', 'moulie', 'moulies', 'moulignon', 'moulignons', 'moulinyan',
    'moulinyans', 'mud person', 'mud persons', 'mud shark', 'mud sharks', 'muk', 'muks', 'muktuk', 'muktuks',
    'mulato', 'mulatos', 'mulatto', 'mulignan', 'mulignans', 'mutt', 'mutts', 'n1gga', 'n1gger', 'negress', 'negro',
    'negroes', 'negroid', 'negros', 'net head', 'net heads', 'nichi', 'nichis', 'nichiwa', 'nichiwas', 'nig',
    'nigaboo', 'nigar', 'nigars', 'niger', 'nigers', 'nigette', 'nigettes', 'nigg', 'nigg3r', 'nigg4h', 'nigga',
    'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niggor', 'niggors', 'niggur', 'niglet', 'nignog', 'nigor',
    'nigors', 'nigr', 'nigra', 'nigras', 'nigre', 'nigres', 'nitchee', 'nitchees', 'nitchie', 'nitchies', 'nitchy',
    'nlgger', 'nlggor', 'northern monkey', 'northern monkies', 'ocker', 'ockers', 'octaroon', 'octaroons', 'ofaies',
    'ofay', 'oriental', 'orientals', 'paddies', 'paddy', 'pakeha', 'paki', 'pakis', 'pancake face', 'pancake faces',
    'papist', 'papists', 'picaninny', 'pickaninnies', 'pickaninny', 'piker', 'pikers', 'pikies', 'piky', 'ping pang', 'ping pangs', 'pocho', 'pocohantas', 'pogue', 'pogues',
    'pohm', 'polack', 'polacks', 'pollock', 'pommy', 'popolo', 'popolos', 'poppadom', 'poppadoms', 'porch monkey',
    'porchmonkey', 'proddy dog', 'proddy dogs', 'proddywhoddies',
    'proddywhoddy', 'proddywoddies', 'proddywoddy', 'pygmy', 'quadroon', 'quadroons', 'raghead', 'red indian',
    'redlegs', 'redskin', 'redskins', 'rhine monkey', 'rhine monkies', 'roofucker', 'roofuckers', 'roundeye',
    'roundeyes', 'ruski', 'sambo', 'sambos', 'sand niggerette', 'sand niggerettes', 'sandnigger', 'scallie',
    'scallies', 'scally', 'scanger', 'scangers', 'semihole', 'semiholes', 'senga', 'sengas', 'seppo',
    'shanty irish', 'shanty irishes', 'sheister', 'sheisters', 'sheltas', 'shylock', 'shylocks', 'shyster',
    'shysters', 'sideways pussies', 'sideways pussy', 'skanger', 'skangers', 'slant', 'slant eye', 'slant eyes',
    'slants', 'slopehead', 'slopeheads', 'slopies', 'smoke jumper', 'smoke jumpers', 'snownigger', 'sooties',
    'sooty', 'soup taker', 'soup takers', 'southern fairies', 'southern fairy', 'spaghettibender',
    'spaghettinigger', 'spic','spick', 'spickaboo', 'spickaboos', 'spicks',
    'spics', 'spide', 'spides', 'spig', 'spigger', 'spiggers', 'spigotties', 'spigotty', 'spigs', 'spik', 'spiks',
    'spink', 'spinks', 'spiv', 'spivs', 'spook', 'spooks', 'squaw', 'squaws', 'steek', 'steeks', 'stump jumper',
    'stump jumpers', 'taffy', 'teabagger', 'teabaggers', 'thicklips',
    'timbernigger', 'tinkard', 'tinkards', 'touch of the tar brush', 'touch of the tar brushes', 'towel head',
    'towel heads', 'towelhead', 'tree jumper', 'tree jumpers', 'tunnel digger', 'tunnel diggers', 'tyncar',
    'tyncars', 'tynekere', 'tynekeres', 'tynkard', 'tynkards', 'tynkare', 'tynkares', 'tynker', 'tynkere',
    'tynkeres', 'tynkers', 'uncircumcised baboon', 'uncircumcised baboons', 'uncle tom', 'velcro head',
    'velcro heads', 'wagon burner', 'wagon burners', 'wetback', 'wexican', 'wexicans', 'whigger', 'wiggerette', 'wiggerettes', 'wog', 'wogs', 'wop', 'wops', 'yellowman', 'yid',
    'zigabo', 'zigabos', 'zipperhead', 'zipperheads', 'zippohead', 'zippoheads', 'zog',
    'zogs', 'pepe', 'immigrants', 'goy', 'goyslop', 'blacks'])

print(category_six)


#7

category_seven = lexicon.create_category("high_divergence_incel_lexicon", ['blackops2cel',
    'blackpill', 'chad', 'cope', 'cuck', 'currycel', 'fakecel', 'friendless', 'fuel', 'gymcel',
    'handholdless', 'heightcel', 'hugless', 'hypergamy', 'incel', 'jbw', 'jfl', 'kissless', 'kthhfv', 'ldar',
    'looksmatch', 'looksmaxx', 'meeks', 'mogs', 'redpill', 'ricecel', 'rope', 'touchless', 'truecel', 'tyrone',
    'volcel', 'wagecel', 'wristcel','women', 'incel', 'incels', 'chad', 'gt', 'men', 'ugly', 'jfl', 'cope', 'foids', 'chads', 'normies', 'blackpill', 'iq', 'normie', 'cuck', 'foid', 'volcel', 'attractive', 'sex', 'girls', 'roastie', 'cucks', 'fakecel', 'femoids', 'manlet', 'personality', 'height', 'woman', 'tinder', 'roasties', 'cucked', 'females', 'virgin', 'chadlite', 'inceltears', 'subhuman',
    'blackpilled', 'faggot', 'gigachad', 'based', 'fakecels', 'fakecel', 'redpill', 'redpillers', 'ascension', 'ascend', 'mogged', 'lifemogged', 'normies', 'chad', 'brocel', 'mentalcel', 'volcel', 'truecel', 'escortmaxxing'], model="reddit")

category_seven = lexicon.cats['high_divergence_incel_lexicon']

lexicon.cats['high_divergence_incel_lexicon'].extend(['blackops2cel', 'blackpill', 
   'chad', 'cope', 'cuck', 'currycel', 'fakecel', 'friendless', 'fuel', 'gymcel',
    'handholdless', 'heightcel', 'hugless', 'hypergamy', 'incel', 'jbw', 'jfl', 'kissless', 'kthhfv', 'ldar',
    'looksmatch', 'looksmaxx', 'meeks', 'mogs', 'redpill', 'ricecel', 'rope', 'touchless', 'truecel', 'tyrone',
    'volcel', 'wagecel', 'wristcel','women', 'incel', 'incels', 'chad', 'gt', 'men', 'ugly', 'jfl', 'cope', 'foids', 'chads', 'normies', 'blackpill', 'iq', 'normie', 'cuck', 'foid', 'volcel', 'attractive', 'sex', 'girls', 'roastie', 'cucks', 'fakecel', 'femoids', 'manlet', 'personality', 'height', 'woman', 'tinder', 'roasties', 'cucked', 'females', 'virgin', 'chadlite', 'inceltears', 'subhuman',
    'blackpilled', 'faggot', 'gigachad', 'based', 'fakecels', 'fakecel', 'redpill', 'redpillers', 'ascension', 'ascend', 'mogged', 'lifemogged', 'normies', 'chad', 'brocel', 'mentalcel', 'volcel', 'truecel', 'escortmaxxing', 'maxxing'])

print(category_seven)




#8 - Exact terms, no empath suggestions 

category_eight = lexicon.create_category('martyrdom',["martyr", "martyrdom", 
 "inspired", "ER", 'er', 'elliot rodger', 'rodger', 'manifesto',
'supreme gentleman', 'saint', 'orlando_harris', 'harris', 'orlando', 'shooting', 'jake davison', 'davison', 'aaron long', 'hernandez',
'scott paul beierle', 'beierle', 'scott paul', 'scott beirele', 'tallahassee', 'alek minassian', 'minassian', 'william atchison', 'atchison',
'chris harper-mercer', 'harper-mercer', 'harper mercer', 'sodini', 'hennard', 'marc lepine', 'lepine', 'seung-hui cho', 'hui cho', 'cho'], model="reddit", size=1)

category_eight = lexicon.cats['martyrdom']


lexicon.cats['martyrdom'].extend(["martyr", "martyrdom", 
 "inspired", "ER", 'er', 'elliot rodger', 'rodger', 'manifesto',
'supreme gentleman', 'saint', 'orlando_harris', 'harris', 'orlando', 'shooting', 'jake davison', 'davison', 'aaron long', 'hernandez',
'scott paul beierle', 'beierle', 'scott paul', 'scott beirele', 'tallahassee', 'alek minassian', 'minassian', 'william atchison', 'atchison',
'chris harper-mercer', 'harper-mercer', 'harper mercer', 'sodini', 'hennard', 'marc lepine', 'lepine', 'seung-hui cho', 'hui cho', 'cho'])

print(category_eight)



#9 

category_nine = lexicon.create_category("sex_sexuality", ['sex', 'sexual', 
    'sexuality', 'gangbang',
    'gangbangs', 'gay', 'straight', 'wank', 'masturbate'], model="reddit")

category_nine = lexicon.cats['sex_sexuality']

lexicon.cats['sex_sexuality'].extend(['sex', 'sexual', 'sexuality', 
    'cherry popper', 'clitfuck', 'cock block', 'cock carousel', 'cock tease', 
    'gangbang', 'gangbanged',
    'gangbangs', 'incest', 'infiltrate', 'insest', 'lolita', 'molest', 'molestation', 'pound', 'rape', 'raped', 'raping', 'sodomise', 'sodomize', 'spank', 'unclefucker', 'virginbreaker', 
    'gangrape', 'gay', 'straight', 'wank', 'masturbate', 'masterbated', 'pump', 'prostitute', 'escort', 'nofap', 'fap', 'fleshlight', 'fuck', 'fucks', 'fucked', 'virgin', 'escortcel', 'escortceled', 'pussy'])

print(category_nine)



#10

category_ten = lexicon.create_category("appearance", ['height', 'weight','fat', 
'thin', 'skinny', 'hair', 'face', 'body', 'short', 'ugly', 'posture', 'unattractive', 'attractive', 'fat', 'obese'], model="reddit")

category_ten = lexicon.cats['appearance']

lexicon.cats['appearance'].extend(['height', 'weight','fat', 'thin', 'skinny', 'ugly', 'looksmax', 'looksmaxx', 'mog', 'mogging', 'looksmatched', 'heightmatched'])

print(category_ten)








#startWordslibrary = 
{ 
 
#1: 
['b00bs', 'becky', 'big ass', 'bint', 'bints', 'bird', 'birds', 'boob', 'boobies', 'boobs', 'booobs', 'boooobs',
'booooobs', 'booooooobs', 'camel toe', 'chesticles', 'cock waffle', 'dumb', 'dumbass', 'f4nny', 'failure',
'fanny', 'fannyflaps', 'female', 'femoid', 'fho', 'fugly', 'funfuck', 'muff', 'pearlnecklace', 'peehole',
'pissflaps', 'poon', 'poonani', 'poontang', 'pornprincess', 'pua', 'puntang', 'puss', 'pussylips', 'roastie',
'shit heel', 'shit heels', 'short fuck', 'skin flute', 'smv', 'snowflake', 'spermhearder', 'spermherder',
'stacy', 't1tt1e5', 't1tties', 'tittie', 'titties', 'titty', 'tittyfuck', 'unfuckable', 'va-j-j', 'ass-hat', 'assbag', 'assbite', 'asscock', 'assface', 'asshat', 'asshead', 'asshole', 'assshit', 'asswipe',
'awalt', 'b!tch', 'b17ch', 'b1tch', 'bad fuck', 'balls', 'banging', 'bastard', 'beastiality', 'beat', 'beaver',
'bi+ch', 'biatch', 'big butt', 'bitch', 'bitch ass', 'bitcher', 'bitchers', 'bitches', 'bitchtits', 'bite me',
'blockhead', 'blockheads', 'boang', 'bogan', 'bogans', 'bottom-feeder', 'brotherfucker', 'butterhead',
'butterheads', 'buttface', 'byatch', 'cause pain', 'chav', 'chavs', 'cheese eating surrender monkey',
'cheese eating surrender monkies', 'clitface', 'cock knob', 'cockbite', 'cockblocker', 'cockhead', 'cockmaster',
'cockmongler', 'cocknose', 'cocknugget', 'conchuda', 'conchudas', 'coochie', 'coochy', 'crotchrot',
'cum bubble', 'cum guzzler', 'cum jockey', 'cum tart', 'cumdumpster', 'cumquat', 'cumqueen', 'cumslut', 'cunt',
'cunt rag', 'cuntass', 'cuntface', 'cuntfuck', 'cunthole', 'cuntlick', 'cunts', 'cuntslut', 'demonrats',
'dick beaters', 'dick for brains', 'dick weasel', 'dick wod', 'dickbag', 'dickbrain', 'dickface',
'dickless', 'dicktickler', 'dickwad', 'dickweed', 'dingo fucker', 'dingo fuckers', 'dipshit', 'dipstick',
'douche', 'douchebag', 'dum ass', 'dumb fuck', 'dumbass', 'dumbbitch', 'dumbfuck', 'eat me', 'eat pussy',
'entrap', 'ewalt', 'extort', 'fastfuck', 'fatass', 'felcher', 'feltcher', 'finger fucker', 'fingerfuckers',
'fist fuck', 'fistfucker', 'footfucker', 'fucka', 'fuckable', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain',
'fuckbuddy', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead',
'fuckher', 'fuckina', 'fuckingbitch', 'fuckit', 'fuckknob', 'fuckpig', 'fucktard', 'fuckup',
'fuckwhore', 'fuckyou', 'gangbanger', 'gash', 'gashes', 'greaseball', 'harm', 'hate', 'hayseed', 'hick',
'hicks', 'hillbilly', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'hoes', 'honkey', 'honky', 'hoodrat', 'hoodrats',
'hore', 'hos', 'hurt', 'hussy', 'idiot', 'idiots', 'intimidate', 'jackass', 'kunt', 'l3i+ch', 'l3itch',
'lardass', 'libtards', 'limpdick', 'menace', 'milf', 'minge', 'mock',
'mocks', 'moron', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker',
'mothafuckers', 'mothafucks', 'mother fucker', 'motherfuck','motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckings',
'motherfuckka', 'motherfucks', 'muthafecker', 'muthafuckker', 'mutherfucker', 'nutsack', 'paleface',            'palefaces', 'panooch', 'peckerwood', 'pindick', 'pohm', 'pohms', 'poor white trash', 'pu55i', 'pu55y',
'punish', 'pusse', 'pussi', 'pussie', 'pussies', 'pussy', 'pussys', 'pusy', 'queerhole', 'redneck', 'rednecks',
'rentafuck', 'retard', 'retarded', 'russellite', 'russellites', 'scag', 'scags', 'scumbag', 'seppo', 'seppos',
'sheepfucker', 'sheepfuckers', 'shit kicker', 'shit kickers', 'shitface', 'shithead', 'shitspitter',
'skag', 'skags', 'skank',
'skank bitch', 'skank fuck', 'skank whore', 'skanky', 'skanky bitch', 'skanky whore', 'skullfuck', 'slag',
'slags', 'slit', 'slits', 'slut', 'slut wear', 'slut whore', 'slutbag', 'sluts', 'slutt', 'slutting', 'slutty',
'slutwhore', 'smear', 'snatch', 'son-of-a-bitch', 'spermbag', 'sub human', 'sub humans', 'suckme', 'suckmytit',
'tard', 'terrorize', 'threaten', 'thrust', 'titfucker', 'titfuckin', 'trailertrash', 'trisexual', 'turd',
'tw4t', 'twat', 'twathead', 'twats', 'twatty', 'twatwaffle', 'twobitwhore', 'twunt', 'twunter', 'wanker',
'wasp', 'wasps', 'waspy', 'white trash', 'whitey', 'whities', 'whoar', 'whore', 'whore from fife',
'whore from fifes', 'whorefucker', 'whores', 'williewanker', 'wuss', 'yankee'],
#2: 
['beta', 'mgtow', 'mra', 'normie', 'overthrow', 'prevail', 'vanquish', 'gynocracy', 
    'hypergamy', 'hypergamous', 'amog', 'betabuxx', 'compel', 'oblige', 'omega', 
    'overwhelm', 'subjugate', 'suppress', 'mistreatment', 'subhuman'],
#3: 
['analannie', 'ass cowboy', 'ass jacker', 'ass whore', 'ass-assinate', 'ass-jabber', 'ass-pirate', 'assbandit',
'assbanger', 'assblaster', 'assfuck', 'assfucker', 'asshopper', 'assklown', 'asslick', 'asslicker', 'assman',
'asspacker', 'asspuppy', 'assranger', 'asssucker', 'backdoor man', 'ball licker', 'bulldike', 'bulldyke',
'bunny fucker', 'butchdyke', 'butt fucker', 'butt pirate', 'buttbang', 'buttfuck', 'buttfucka', 'buttpirate',
'c0cksucker', 'carpet muncher', 'cock cowboy', 'cock jockey', 'cock licker', 'cock smoke', 'cock suck',
'cock-sucker', 'cockmunch', 'cockmuncher', 'cockqueen', 'cockrider', 'cocksman', 'cocksmith', 'cocksmoker',
'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka',
'cokmuncher', 'coksucka', 'cuntfucker', 'cuntlick', 'cuntlicker', 'cuntlicking', 'dick licker', 'dickfuck',
'dickfucker', 'dicklick', 'dickman', 'dickmonger', 'dicksucker', 'dyke', 'dyke jumper', 'dyke jumpers', 'dykes',
'fag', 'fagfucker', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny fucker',
'fannyfucker', 'fingerfucker', 'fingerfuckers', 'fistfucker', 'fistfuckers', 'fudge packer', 'fudgepacker',
'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'homo',
'muffdive', 'muffindiver', 'mufflikcer', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'penisbanger',
'penisfucker', 'penispuffer', 'polesmoker', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylicking',
'pussylover', 'pussypounder', 'queer', 'queers', 'rimjaw', 'sodomite', 'lez', 'lezbo', 'lezz', 'lezzie', 'lezzo'],
#4: 
['annihilate', 'assail', 'assassinate', 'assault', 'attack', 'bang', 'batter', 'blast', 'block', 'bring down',
'bruise', 'brutalise', 'burn', 'bust', 'butcher', 'carry off', 'choke', 'clobber', 'concuss', 'constrain',        'crack', 'crush', 'cut', 'decimate', 'demolish', 'destroy', 'dispose of', 'drown', 'enslave', 'er',
'exterminate', 'finish off', 'flagellate', 'force', 'gag', 'hit', 'jump', 'kick', 'kill', 'lock up', 'maul',
'murder', 'obliterate', 'pelt', 'plunk', 'pounce upon', 'pummel', 'punch', 'raid', 'ram', 'shake', 'shake down',
'shoot ', 'shove', 'slam', 'slap', 'slaughter', 'slog', 'smack', 'smash', 'smother', 'stab', 'strangle',
'strike', 'strong-arm', 'thrash', 'thresh', 'thwack', 'trample', 'trounce', 'vaporize', 'wallop', 'whip', 'ER', 'elliot rodgers', 'kill', 'rope', 'kys', 'roping', 'shoot', 'shooting', 'kill', 'killed', 'killing', 'nuke', 'rape', 'raped', 'raping', 'beating', 'hang', 'hanged', 'attack', 'attacks', 'gun', 'guns', 'assault', 'hurt', 'shot', 'punch', 'revenge', 'murder', 'behead'],
#5: 
['cherry popper', 'clitfuck', 'cock block', 'cock carousel', 'cock tease', 'conquer', 'gangbang', 'gangbanged'
'gangbangs', 'incest', 'infiltrate', 'insest', 'lolita', 'molest', 'molestation', 'pound', 'rape', 'sodomise',
'sodomize', 'spank', 'unclefucker', 'virginbreaker'],
#6: 
['abbo', 'abbos', 'abo', 'abos', 'african catfish', 'african catfishes', 'african forklift', 'africoon',
'africoons', 'afro-saxon', 'afro-saxons', 'albino', 'albinos', 'alligator bait', 'alligator baits', 'americoon',
'americoons', 'amo', 'amos', 'anglo', 'anglos', 'arab', 'argie', 'argies', 'armo', 'armos', 'assnigger',
'aunt jemima', 'aunt jemimas', 'banana bender', 'banana benders',
'banana lander', 'banana landers', 'banjo lips', 'bans and cans', 'beach nigger', 'beach niggers',
'bean dipper', 'bean dippers', 'beaner', 'beaner shnitzel', 'beaner shnitzels', 'beaners', 'beaney', 'beanies',
'bhrempti', 'bhremptis', 'bigger', 'bix nood', 'bix noods', 'black', 'black barbie', 'black barbies',
'black dago', 'black dagos', 'blaxican', 'blaxicans', 'bluegum', 'bluegums', 'bog hopper', 'bog hoppers',
'bog irish', 'bog irishes', 'bog jumper', 'bog jumpers', 'bog trotter', 'bog trotters', 'bohunk', 'booner',
'booners', 'boong', 'boonga', 'boongas', 'boongs', 'boonie', 'boonies', 'border bunnies', 'border bunny',
'border hoppers', 'border nigger', 'border niggers', 'buckethead', 'bucketheads', 'buckra', 'buckras',
'buckwheat', 'buckwheats', 'buddhahead', 'buddhaheads', 'buffie', 'buffies', 'bug eater', 'bug eaters',
'buk buk', 'buk buks', 'bung', 'bunga', 'bungas', 'bungs', 'burrhead', 'burrheads', 'cab nigger', 'cab niggers',
'camel cowboies', 'camel cowboy', 'camel fucker', 'camel fuckers', 'camel humper', 'camel humpers',
'camel jacker', 'camel jackers', 'camel jockey', 'can eater', 'can eaters', 'canuck', 'carpet pilot',
'carpet pilots', 'carrot snapper', 'carrot snappers', 'caublasian', 'caublasians', 'cave nigger',
'cave niggers', 'charva', 'charvas', 'chigger', 'chiggers', 'chili shitter', 'chili shitters', 'chinaman',
'chinc', 'chinese wetback', 'chinese wetbacks', 'ching chong', 'ching chongs', 'chinig', 'chinigs', 'chink',
'chink a billies', 'chink a billy', 'chinks', 'chinky', 'chonkies', 'chonky', 'christ killer', 'christ killers',
'chug', 'chugs', 'clamhead', 'clamheads', 'clog wog', 'coolie', 'coolies', 'coon', 'coondog', 'coons',
'cow kisser', 'cow kissers', 'cowboy killer', 'cowboy killers', 'cracker', 'crackers', 'cunteyed',
'curry slurper', 'curry slurpers', 'curry stinker', 'curry stinkers', 'cushi', 'cushis', 'cushite', 'cushites',
'dago', 'dagos', 'darkey', 'darkie', 'darkies', 'darky', 'dego', 'degos', 'diaper head', 'diaper heads',
'dinge', 'dinges', 'dogun', 'doguns', 'dot head', 'dot heads', 'dune coon', 'dune coons', 'dune nigger',
'dune niggers', 'eskimo', 'eyetie', 'eyeties', 'fob', 'fobs', 'fog nigger',
'fog niggers', 'fresh off the boat', 'fresh off the boats', 'gator bait', 'gator baits', 'gerudo', 'gerudos',
'gew', 'gews', 'ghetto hamster', 'ghetto hamsters', 'gin jockey', 'gin jockies', 'ginzo', 'ginzos', 'gipp',
'gippo', 'gippos', 'gipps', 'gipsy', 'golliwog', 'golliwogs', 'gook', 'gook eye', 'gook eyes', 'gookies',
'gooks', 'gooky', 'goy', 'goyim', 'greaser', 'greasers', 'gringo', 'groid', 'groids', 'guala guala',
'guala gualas', 'gub', 'gubba', 'gubbas', 'gubs', 'guido', 'guidos', 'gurrier', 'gurriers', 'gwat', 'gwats',
'gyppie', 'gyppies', 'gyppy', 'gypsy', 'hairyback', 'hairybacks', 'half-breed', 'half-caste', 'halfrican',
'halfricans', 'haole', 'hapa', 'hebe', 'hebes', 'hebro', 'hebros', 'heeb', 'heebs', 'heinie', 'heinies',
'higger', 'higgers', 'hindoo', 'hodgie', 'honyak', 'honyaks', 'honyock', 'honyocks', 'hoosier', 'hoosiers',
'hun', 'hunkie', 'hunkies', 'hunky', 'huns', 'hunyak', 'hunyaks', 'hunyock', 'hunyocks', 'hymie', 'hymies',
'ice monkey', 'ice monkies', 'ice nigger', 'ice niggers', 'ike', 'ikes', 'ikey', 'ikey mo', 'ikey mos', 'ikies',
'iky', 'injun', 'injuns', 'island nigger', 'island niggers', 'jant', 'jants', 'jap', 'japie', 'japies', 'japs',
'jewbacca', 'jewbaccas', 'jhant', 'jhants', 'jig', 'jiga', 'jigaboo', 'jigarooni', 'jigaroonis', 'jigg',
'jigga', 'jiggabo', 'jiggabos', 'jiggas', 'jigger', 'jiggers', 'jiggs', 'jigs', 'jijjiboo', 'jijjiboos',
'jimfish', 'jockie', 'jockies', 'jocky', 'junglebunny', 'kaffir', 'kafir', 'khazar', 'khazars', 'kike', 'kikes',
'kotiya', 'kotiyas', 'kraut', 'krauts', 'kushi', 'kushis', 'kushite', 'kushites', 'kyke', 'kykes', 'latrino',
'latrinos', 'lawn jockey', 'lawn jockies', 'leb', 'lebbo', 'lebbos', 'lebs', 'lemonhead', 'lemonheads',
'leprechaun', 'leprechauns', 'ling ling', 'ling lings', 'lowlander', 'lowlanders', 'lubra', 'lubras', 'lugan',
'lugans', 'makwerekwere', 'mammy', 'mangia cake', 'mangia cakes', 'mick', 'micks', 'mockey', 'mockie',
'mockies', 'mocky', 'moke', 'mokes', 'mokies', 'moky', 'mook', 'mooks', 'mooncricket', 'moss eater',
'moss eaters', 'mosshead', 'mossheads', 'moulie', 'moulies', 'moulignon', 'moulignons', 'moulinyan',
'moulinyans', 'mud person', 'mud persons', 'mud shark', 'mud sharks', 'muk', 'muks', 'muktuk', 'muktuks',
'mulato', 'mulatos', 'mulatto', 'mulignan', 'mulignans', 'mutt', 'mutts', 'n1gga', 'n1gger', 'negress', 'negro',
'negroes', 'negroid', 'negros', 'net head', 'net heads', 'nichi', 'nichis', 'nichiwa', 'nichiwas', 'nig',
'nigaboo', 'nigar', 'nigars', 'niger', 'nigers', 'nigette', 'nigettes', 'nigg', 'nigg3r', 'nigg4h', 'nigga',
'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niggor', 'niggors', 'niggur', 'niglet', 'nignog', 'nigor',
'nigors', 'nigr', 'nigra', 'nigras', 'nigre', 'nigres', 'nitchee', 'nitchees', 'nitchie', 'nitchies', 'nitchy',
'nlgger', 'nlggor', 'northern monkey', 'northern monkies', 'ocker', 'ockers', 'octaroon', 'octaroons', 'ofaies',
'ofay', 'oriental', 'orientals', 'paddies', 'paddy', 'pakeha', 'paki', 'pakis', 'pancake face', 'pancake faces',
'papist', 'papists', 'picaninny', 'pickaninnies', 'pickaninny', 'piker', 'pikers', 'pikies', 'piky',
'pineapple nigger', 'pineapple niggers', 'ping pang', 'ping pangs', 'pocho', 'pocohantas', 'pogue', 'pogues',
'pohm', 'polack', 'polacks', 'pollock', 'pommy', 'popolo', 'popolos', 'poppadom', 'poppadoms', 'porch monkey',
'porchmonkey', 'prairie nigger', 'prairie niggers', 'proddy dog', 'proddy dogs', 'proddywhoddies',
'proddywhoddy', 'proddywoddies', 'proddywoddy', 'pygmy', 'quadroon', 'quadroons', 'raghead', 'red indian',
'redlegs', 'redskin', 'redskins', 'rhine monkey', 'rhine monkies', 'roofucker', 'roofuckers', 'roundeye',
'roundeyes', 'ruski', 'sambo', 'sambos', 'sand niggerette', 'sand niggerettes', 'sandnigger', 'scallie',
'scallies', 'scally', 'scanger', 'scangers', 'semihole', 'semiholes', 'senga', 'sengas', 'seppo',
'shanty irish', 'shanty irishes', 'sheister', 'sheisters', 'sheltas', 'shylock', 'shylocks', 'shyster',
'shysters', 'sideways pussies', 'sideways pussy', 'skanger', 'skangers', 'slant', 'slant eye', 'slant eyes',
'slants', 'slopehead', 'slopeheads', 'slopies', 'smoke jumper', 'smoke jumpers', 'snownigger', 'sooties',
'sooty', 'soup taker', 'soup takers', 'southern fairies', 'southern fairy', 'spaghettibender',
'spaghettinigger', 'spic', 'spice nigger', 'spice niggers', 'spick', 'spickaboo', 'spickaboos', 'spicks',
'spics', 'spide', 'spides', 'spig', 'spigger', 'spiggers', 'spigotties', 'spigotty', 'spigs', 'spik', 'spiks',
'spink', 'spinks', 'spiv', 'spivs', 'spook', 'spooks', 'squaw', 'squaws', 'steek', 'steeks', 'stump jumper',
'stump jumpers', 'taffy', 'teabagger', 'teabaggers', 'thicklips', 'timber nigger', 'timber niggers',
'timbernigger', 'tinkard', 'tinkards', 'touch of the tar brush', 'touch of the tar brushes', 'towel head',
'towel heads', 'towelhead', 'tree jumper', 'tree jumpers', 'tunnel digger', 'tunnel diggers', 'tyncar',
'tyncars', 'tynekere', 'tynekeres', 'tynkard', 'tynkards', 'tynkare', 'tynkares', 'tynker', 'tynkere',
'tynkeres', 'tynkers', 'uncircumcised baboon', 'uncircumcised baboons', 'uncle tom', 'velcro head',
'velcro heads', 'wagon burner', 'wagon burners', 'wetback', 'wexican', 'wexicans', 'whigger', 'white nigger',
'white niggers', 'whitenigger', 'wiggerette', 'wiggerettes', 'wog', 'wogs', 'wop', 'wops', 'yellowman', 'yid',
'zigabo', 'zigabos', 'zipperhead', 'zipperheads', 'zippohead', 'zippoheads', 'zog', 'zog lover', 'zog lovers',
'zogs', 'sideways cooter', 'sideways cooters', 'sideways vagina', 'sideways vaginas'],
#7: 
['blackops2cel', 'blackpill', 'chad', 'cope', 'cuck', 'currycel', 'fakecel', 'friendless', 'fuel', 'gymcel',
'handholdless', 'heightcel', 'hugless', 'hypergamy', 'incel', 'jbw', 'jfl', 'kissless', 'kthhfv', 'ldar',
'looksmatch', 'looksmaxx', 'meeks', 'mogs', 'redpill', 'ricecel', 'rope', 'touchless', 'truecel', 'tyrone',
'volcel', 'wagecel', 'wristcel','women', 'incel', 'incels', 'chad', 'gt', 'men', 'ugly', 'jfl', 'cope', 'foids', 'chads', 'normies', 'blackpill', 'iq', 'normie', 'cuck', 'foid', 'volcel', 'attractive', 'sex', 'girls', 'roastie', 'cucks', 'fakecel', 'femoids', 'manlet', 'personality', 'height', 'woman', 'tinder', 'roasties', 'cucked', 'females', 'virgin', 'chadlite', 'inceltears', 'subhuman', 'blackpilled', 'faggot'],
#8: 
["martyr", "martyrdom", "inspired", "ER", 'er', 'elliot rodger', 'rodger', 'manifesto',
'supreme gentleman', 'saint', 'orlando_harris', 'harris', 'orlando', 'shooting', 'jake davison', 'davison', 'aaron long', 'hernandez',
'scott paul beierle', 'beierle', 'scott paul', 'scott beirele', 'tallahassee', 'alek minassian', 'minassian', 'william atchison', 'atchison',
'chris harper-mercer', 'harper-mercer', 'harper mercer', 'sodini', 'hennard', 'marc lepine', 'lepine', 'seung-hui cho', 'hui cho', 'cho'],
#9: 
['sex', 'sexual', 'sexuality', 'gangbang','gangbangs', 'gay', 'straight', 'wank', 'masturbate'],
#10: 
['height', 'weight','fat', 'thin', 'skinny', 'hair', 'face', 'body', 'short', 'ugly', 'posture', 'unattractive', 'attractive', 'fat', 'obese']

}

