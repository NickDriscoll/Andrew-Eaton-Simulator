import random

# This method returns a populated dictionary by
# taking each word in a tweet and the following word
# and making those into key-value pairs respectively.
def populate_dictionary_prefix_one(tweets):
	word_dict = {}
	for tweet in tweets:
		if ("http" not in tweet.text) and (tweet.text[0:2] != "RT") and ("@" not in tweet.text):
			words = tweet.text.split(" ")
			for i in range(0, len(words) - 1):
				if words[i] in word_dict:
					word_dict[words[i]].append(words[i + 1])
				else:
					word_dict[words[i]] = [] 
					word_dict[words[i]].append(words[i + 1])
	return word_dict

# This method returns a populated dictionary by
# taking each word in a tweet and the two preceding words
# and making those into key-value pairs with the two words
# being the key and the single word being the value.
def populate_dictionary_prefix_two(tweets):
	word_dict = {}
	for tweet in tweets:
		if ("http" not in tweet.text) and (tweet.text[0:2] != "RT") and ("@" not in tweet.text):
			words = tweet.text.split(" ")
			for i in range(0, len(words)):
				
				#Get the two preceding indices
				precedingIndex = i - 1
				precedingIndex2 = i - 2
				
				#Making sure they're within the list
				if precedingIndex >= 0:
					precedingWord = words[precedingIndex]
				if precedingIndex2 >= 0:
					precedingWord2 = words[precedingIndex2]

				if precedingIndex2 >= 0 and precedingIndex >= 0:
					precedingPhrase = precedingWord2 + " " + precedingWord
					if precedingPhrase in word_dict:
						word_dict[precedingPhrase].append(words[i])
					else:
						word_dict[precedingPhrase] = []
						word_dict[precedingPhrase].append(words[i])

	return word_dict


def generate_seed(dictionary):
	return random.choice(list(dictionary.keys()))

def markov_prefix_length_one(dictionary, minLength):
	i = 0
	seed = generate_seed(dictionary)
	result = seed + " "
	flag = False
	while not flag:
		if seed in dictionary:
			newWord = random.choice(dictionary[seed])
			result = result + newWord + " "
			seed = newWord
			i = i + 1
		else:
			if i > minLength:
				flag = True
			else:
				seed = generate_seed(dictionary)
	if len(result) > 140:
		result = markov_prefix_length_one(dictionary, minLength)
	return result

def markov_prefix_length_two(dictionary, minLength):
	i = 1
	seed = generate_seed(dictionary)
	result = seed + " "
	flag = False
	while not flag:
		if seed in dictionary:
			newWord = random.choice(dictionary[seed])
			result = result + newWord + " "
			seed = seed.split()[1] + " " + newWord
			i = i + 1
		else:
			if i > minLength:
				flag = True
			else:
				seed = generate_seed(dictionary)
	if len(result) > 140:
		result = markov_prefix_length_two(dictionary, minLength)
	return result

def markov_hybrid(dict_one, dict_two, minLength):
	seed = generate_seed(dict_one)
	i = 0
	result = seed + " "
	#Even means one, odd means two
	t = 0
	flag = False
	#print("Entering loop...")
	while not flag:
		if t % 2 == 0:
			print("In branch one...")
			#print(result)
			if seed in dict_one:
				newWord = random.choice(dict_one[seed])
				result = result + newWord + " "
				seed = newWord + result.split()[1]
			else:
				if t > minLength:
					flag = True
				else:
					seed = generate_seed(dict_two)
		else:
			print("In branch two...")
			#print(result)
			if seed in dict_two:
				newWord = random.choice(dict_two[seed])
				result = result + newWord + " "
				seed = seed.split()[1] + " " + newWord
			else:
				if t > minLength:
					flag = True
				else:
					seed = generate_seed(dict_one)
		t = t + 1
	if len(result) > 140:
		print("----------Broke limit.----------")
		result = markov_hybrid(dict_one, dict_two, minLength)
	return result