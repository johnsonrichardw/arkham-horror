#!/usr/bin/python3

import random
import argparse

#List of known token types, used later to validate tokens added by command line
tokens = ['+1','0','-1','-2','-3','-4','-5','-6','-8','Skull','Cultist','Tablet','Elder Thing','Elder Sign','Tentacle']
#List of supported campaigns/scenarios
campaigns = ['notz','tdl','coh','cotr']
#List of supported difficulties
difficulties = ['easy','standard','hard','expert']

#Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('campaign',help='Which campaign to use for token pool', choices=campaigns)
parser.add_argument('difficulty',help='Which difficulty the scenario is being played at', choices=difficulties)
parser.add_argument('--tokens', nargs='+', help='Add additional tokens to token pool',choices=tokens)
args = parser.parse_args()

#Initialize our token pools indexed by 'campaign-difficulty'
token_sets = {}
#Night of the Zealot token pools
token_sets['notz-easy'] = ['+1','+1','0','0','0','-1','-1','-1','-2','-2','Skull','Skull','Cultist','Tablet','Tentacle','Elder Sign']
token_sets['notz-standard'] = ['+1','0','0','-1','-1','-1','-2','-2','-3','-4','Skull','Skull','Cultist','Tablet','Tentacle','Elder Sign']
token_sets['notz-hard'] = ['0','0','0','-1','-1','-2','-2','-3','-3','-4','-5','Skull','Skull','Cultist','Tablet','Tentacle','Elder Sign']
token_sets['notz-expert'] = ['0','-1','-1','-2','-2','-3','-3','-4','-4','-5','-6','-8','Skull','Skull','Cultist','Tablet','Tentacle','Elder Sign']
#The Dunwich Legacy token pools
token_sets['tdl-easy'] = ['+1','+1','0','0','0','-1','-1','-1','-2','-2','Skull','Skull','Cultist','Tentacle','Elder Sign']
token_sets['tdl-standard'] = ['+1','0','0','-1','-1','-1','-2','-2','-3','-4','Skull','Skull','Cultist','Tentacle','Elder Sign']
token_sets['tdl-hard'] = ['0','0','0','-1','-1','-2','-2','-3','-3','-4','-5','Skull','Skull','Cultist','Tentacle','Elder Sign']
token_sets['tdl-expert'] = ['0','-1','-1','-2','-2','-3','-3','-4','-4','-5','-6','-8','Skull','Skull','Cultist','Tentacle','Elder Sign']
#Carnevale of Horrors token pools
token_sets['coh-standard'] = ['+1','0','0','0','-1','-1','-1','-2','-2','-3','-4','-6','Skull','Skull','Skull','Cultist','Tablet','Elder Thing','Tentacle','Elder Sign']
token_sets['coh-hard'] = ['+1','0','0','0','-1','-1','-3','-4','-5','-6','-7','Skull','Skull','Skull','Cultist','Tablet','Elder Thing','Tentacle','Elder Sign']
#Curse of the Rougarou
token_sets['cotr-standard'] = ['+1','+1','0','0','0','-1','-1','-1','-2','-2','-3','-3','-4','-4','-5','-6','Skull','Skull','Cultist','Cultist','Tablet','Elder Thing','Tentacle','Elder Sign']
token_sets['cotr-hard'] = ['+1','0','0','0','-1','-1','-1','-2','-2','-3','-3','-4','-4','-5','-5','-6','-8','Skull','Skull','Skull','Cultist','Cultist','Tablet','Elder Thing','Tentacle','Elder Sign']

#Get token set to use
set = args.campaign + '-' + args.difficulty
if set not in token_sets.keys():
    raise ValueError('Unknown token set: ' + set)
token_list = token_sets[set]

#Add specified new tokens to set
if args.tokens != None:
    for tok in args.tokens:
        if tok not in tokens:
            raise ValueError('Unknown token type: ' + tok)
        token_list.append(tok)

#Randomly choose a token from the list and print it out
print(random.choice(token_list))

