import random
response = open("soundclips/shrekquotes", "r").readlines()
while True:
    answer = input('What would you like to ask: ')
    respond = random.choice(response)
    print(respond)