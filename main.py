import tweepy, random
from keys import keys
from methods import markov_prefix_length_one
from methods import populate_dictionary_prefix_one
from methods import populate_dictionary_prefix_two

#Users id
uID = 332088556

#Authenticate with Twitter
auth = tweepy.OAuthHandler(keys["a"], keys["b"])
auth.set_access_token(keys["c"], keys["d"])

#Create an api object
api = tweepy.API(auth)

#Get a reference to user
user = api.get_user(uID)

#Populate the dictionary of prefixes and suffixes
word_dict_prefix_one = populate_dictionary_prefix_one(api.user_timeline(id=user.id, count=5000))
#word_dict_prefix_two = populate_dictionary_prefix_two(api.user_timeline(id=user.id, count=5000))

#Tweet out a tweet generated with a Markov chain
#print(markov_hybrid(word_dict_prefix_one, word_dict_prefix_two, 15))
api.update_status(status=markov_prefix_length_one(word_dict_prefix_one, 5))
