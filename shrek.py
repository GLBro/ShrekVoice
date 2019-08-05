import random
response = open("soundclips/shrekquotes", "r").readlines()
while True:
    answer = input('What would you like to ask: ')
    if "song" in answer:
        respond = "We will play a song"
    else:
        respond = random.choice(response)
    print(respond)