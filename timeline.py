#!/usr/bin/python3
from twython import Twython, TwythonError
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-t', '--target', required=True, help='Their @')
args = vars(ap.parse_args())
target = args["target"]

APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def timeline(x):
	try:
		timeline = t.get_user_timeline(screen_name=x)

		for tweet in timeline: #for each tweet
			for i in range(len(tweet['entities']['urls'])): #check how many links per tweet and iterate over them
				link = tweet['entities']['urls'][i]['expanded_url'] #saves the link for future use
				if ('facebook' in link) or ('instagram' in link) or ('tumblr' in link) or ('snap' in link):  #keywords
					print ("[*] Potencial profile found: %s" % (link))

	except TwythonError as e:
		print(e)

def bio(x):
	try:
		info = t.show_user(screen_name=x)
                urlBio = info['entities']['url']['urls'][0]['expanded_url']
		if ('facebook' in urlBio) or ('instagram' in urlBio) or ('tumblr' in urlBio) or ('snap' in urlBio):
			print("[*] Potencial profile found in bio: %s" % (urlBio))

		bio = info['description']
		if ('facebook' in bio) or ('instagram' in bio) or ('tumblr' in bio) or ('snap' in bio):
			print ("[*] Potencial profile found in bio: %s" % (link))

		if ('url' in bio):
			link = info['entities']['url']['urls'][0]['expanded_url']
			if ('facebook' in link) or ('instagram' in link) or ('tumblr' in link):
				print ("[*] Potencial profile found in bio's URL: %s" % (link))
	except TwythonError as e:
		print(e)

def main():
	os.system("clear")
	print("Looking for links...")
	timeline(target)
	bio(target)

if __name__ == '__main__':
	main()
