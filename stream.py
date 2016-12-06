import tweepy, random
from keys import keys
from methods import markov_prefix_length_one
from methods import populate_dictionary_prefix_one
from methods import populate_dictionary_prefix_two

#Authenticate with Twitter
auth = tweepy.OAuthHandler(keys["a"], keys["b"])
auth.set_access_token(keys["c"], keys["d"])

#Create an api object
api = tweepy.API(auth)

#Get a reference to @dethandrew
user = api.get_user("@dethandrew")

#Define stream listener class
class SL(tweepy.StreamListener):
	def on_status(self, status):
		#print(status.user.screen_name)
		#Populate the dictionary of prefixes and suffixes
		word_dict_prefix_one = populate_dictionary_prefix_one(api.user_timeline(id=user.id, count=5000))
		response = "@" + status.user.screen_name + " " + markov_prefix_length_one(word_dict_prefix_one, 5)
		print(response)
		print("In response to " + str(status.id))
		api.update_status(response, status.id)

#Create stream listener and subsequently create stream
sl = SL()
stream = tweepy.Stream(auth=auth, listener=sl)

stream.filter(track=["@andrewEatonSim"])