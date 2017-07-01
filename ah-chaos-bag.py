#!/usr/bin/python3

import random
import argparse
import json

def get_token_pool(token_pool_json,cam_abbv,difficulty):
    """Take the token pool json object and search for the token pool specified
    by the campaign abbreviation and difficulty"""
    for camp in token_pool_json['campaigns']:
        if camp['abbreviation'] == cam_abbv:
            for camp_pools in camp['tokenPools']:
                if camp_pools['difficulty'] == difficulty:
                    return camp_pools['tokens']
    #didn't find anything
    raise ValueError('Unknown token set: ' + cam_abbv + ' ' + difficulty)


#Open json file specifying campaign token pools
f_tok_pool = open('token_pools.json',mode='r')
token_pool = json.load(f_tok_pool)
#Done with file pointer
f_tok_pool.close()

#List of known token types, used later to validate tokens added by command line
tokens = token_pool['tokens']
#List of supported campaigns/scenarios
campaigns = [x['abbreviation'] for x in token_pool['campaigns']]
#List of supported difficulties
difficulties = ['easy','standard','hard','expert']

#Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('campaign',help='Which campaign to use for token pool', choices=campaigns)
parser.add_argument('difficulty',help='Which difficulty the scenario is being played at', choices=difficulties)
parser.add_argument('--tokens', nargs='+', help='Add additional tokens to token pool',choices=tokens)
args = parser.parse_args()

#Get token set to use
token_list = get_token_pool(token_pool,args.campaign,args.difficulty)

#Add specified new tokens to set
if args.tokens != None:
    for tok in args.tokens:
        if tok not in tokens:
            raise ValueError('Unknown token type: ' + tok)
        token_list.append(tok)

#Randomly choose a token from the list and print it out
print(random.choice(token_list))

