import random
response = open("soundclips/shrekquotes", "r").readlines()
while True:
    answer = input('What would you like to ask: ')
    if "song" in answer:
        respond = "We will play a song"
    elif "swamp" in answer:
        respond = "Get out of my swamp!"
    elif "story" in answer: 
        respond= "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love, and true love's first kiss."
    else:
        respond = random.choice(response)
    
    print(respond)