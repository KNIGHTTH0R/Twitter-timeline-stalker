from twitter import *
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--target', required=True, help='Their @')
args = vars(ap.parse_args())
alvo = args["target"]

con_secret = ''
con_secret_key = ''
token = ''
token_key = ''

#auth
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key), retry=True) 

def timeline(x):
#get the timeline
	timeline = t.statuses.user_timeline(screen_name=x, include_rts=False, count=200) 

	for tweet in timeline: #for each tweet
		for i in range(len(tweet['entities']['urls'])): #check how many links per tweet and iterate over them
			link = tweet['entities']['urls'][i]['expanded_url'] #saves the link for future use
			if ('facebook' in link) or ('instagram' in link) or ('tumblr' in link): 
				print "[*] Potencial profile found: %s" % (link)

def main():
	os.system('clear')
	timeline(target)

if __name__ == '__main__':
	main()
