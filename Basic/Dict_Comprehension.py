sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence = sentence.split()

dict_list = {word : len(word) for word in sentence}
print(dict_list.items())