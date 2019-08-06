import random,time 
response = open("soundclips/shrekquotes", "r").readlines()
while True:
    answer = input('What would you like to ask: ')
    if "song" in answer:
        respond = "We will play a song"
    elif "swamp" in answer:
        rad = "Get out of my swamp!", "that would be my home"
        respond = random.choice(rad)
    elif "book" in answer:
        respond = "i read a book once"
    elif "annoying" in answer:
        rad = "could you be quiet just FOR 5 MINUTES!", "two things ok?Shut..up"
        respond = random.choice(rad)
    elif "story" in answer: 
        respond= "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love, and true love's first kiss."
    elif "remind" in answer:
        respond = "its on my to do list"
    elif "princess" in answer or 'fiona' in answer:
        respond = "the princess will be up in the stairs in the highest room in the tallest tower"
    elif "hate" in answer or "mean" in answer:
        respond = "well,thats not very nice."
    elif "ogre" in answer:
        respond = "ogres are like onions. onions have layers. ogres have layers"
    elif "will" in answer:
        respond = "yeah right before they burst into flame"
    elif "smart" in answer:
        respond = "well ER That explains a lot!"
    elif "sad" in answer:
        respond = "oh would you look at that!"
    elif "house" in answer:
        respond = "sure it big enough...but look at the location!"
    elif "animal" in answer:
        respond = "its just a donkey"
    elif "loud" in answer:
        respond = "could you be quiet for 5 minutes FOR 5 MINUTES"
    elif "dinner" in answer:
        respond = "dead broad.. OFF THE TABLE!"
    elif "lonley" in answer:
        respond = "well its no wonder you have no friends!"
    elif "Could" in answer:
        respond = "NO!"
    elif "do" in answer:
        respond = "Yes.NO!"
    elif "scary" in answer: 
        respond = "this is the part where you run away"

    elif "why" or "look" in answer:
        respond = "i like my privacy"

    else:
        respond = random.choice(response)
    
 
    time.sleep(random.randint(0,3))

    print(respond)