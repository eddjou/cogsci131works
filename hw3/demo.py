import re
import random
import sys

def strangefood():
    return random.choice(["Tuna Eyeballs","Surstromming","Grasshoppers","Wasp Crackers","Fried Spider","Witchetty Grub","Beondegi","Escargots à la Bourguignonne"])

def tellmemore():
    return "Tell me more"

def question():
    country=["Chinese","Japanese","Korean","Mexican","Indian","Swedish","Norwegian","French","English"]
    taste=["spicy","sweet","salty","strong taste"]
    generaltype=["staple food","noodle","meat","seafood","vegetables"]
    foodlist=["fried rice","chicken soup",
              "stewed beef","chicken breast","dumplings",
              "dough stick","pasta","pizza","hamburger","fries","pancake"]
    ques=["What "+random.choice(country)+" food do you like best?",
          "What "+random.choice(country)+" food do you hate most?",
          "What is your opinion on "+random.choice(foodlist)+"?",
          "Do you have any idea on strange "+random.choice(country)+" food?",
          "What kind of "+random.choice(generaltype)+" do you like most?",
          "Do you like "+random.choice(taste)+" food?",
          "Do you like "+strangefood()+"?"]
    return random.choice(ques)

def farewell():
    weather=["raining","windy","sunny","cloudy"]
    fare=["Oops! I have to go now! My plane will take off in thirty minutes!","Oops! Something goes wrong with my kids, I have to go now!","Oops! Someone is waiting for me! Bye me friend!""Can we say goodbye now? I am in a hurry!","Excuse me, but I fell a bit ill now...","It's "+random.choice(weather)+" outside, let's just enjoy the nature. Stay silent man."]
    return random.choice(fare)

def panacea():
    backup=["Yeah!","Absolutely!","Definitely!","That's okay.","Oho!","Zzz...","Oops!","Wow!","Ah!","Yipe!","Got it!","I do.","I agree."]
    rt=random.choice(backup)
    return rt

def chatbot(inp):
    if re.search('thank',inp) or re.match('ty',inp) or re.search('bye',inp) or re.search("that"r"all",inp):
        print("Jarvis :: See you! I will miss you!")
        sys.exit()
    elif len(inp)<15 and not re.match("i",inp):
        reply=panacea()+"And "+question()
    elif re.match("what\?",inp) or re.match("\?",inp):
        reply="I mean I like it."
    elif re.search("why\?",inp) or re.search("how\?",inp):
        quess=" But "+question().lower()
        reply=random.choice(["For some reason I cannot explain.",
                            "Beyond your imagination."])+random.choice(["",quess])
    elif re.match("and you",inp) or (re.match("what",inp) and (re.search("like",inp) or re.search("love",inp))):
        if re.search("what (.+?) do",inp):
            keyans=re.search("what (.+?) do",inp).groups()[0]
            reply = "The " + keyans + " I like most is " + strangefood().lower() + "."
        else:
            reply="I like "+strangefood()+"."
    elif (re.search("idea",inp) or re.search("how",inp) or re.search("what",inp) or (re.match("do",inp) and re.search("like",inp))) and re.search("\?",inp):
            if re.match("do",inp) and re.search("like",inp):
                key = re.search(r"like (.+)\?", inp).groups()[0]
            elif re.search("what about",inp):
                key = re.search(r"what about (.+)\?", inp).groups()[0]
            elif re.search("how about",inp):
                key = re.search(r"how about (.+)\?", inp).groups()[0]
            elif re.search("do you think of", inp):
                key = re.search(r"think of (.+)\?", inp).groups()[0]
            elif re.search("opinion on", inp) and re.search("\?", inp):
                key = re.search(r"opinion on (.+)\?", inp).groups()[0]
            elif re.search("idea",inp) and re.search("\?", inp):
                key=re.search(r"idea (.+) (.+)\?",inp).groups()[1]
            else:
                key="it"
            if not key:
                reply=panacea()
            else:
                likedic=["I really like "+key+".",
                     "I love "+key+".",
                     "I used to love "+key+", but I do not like it now.",
                     ""]
                reply=random.choice(likedic)
    elif (re.search("i like",inp) or re.search("i love",inp)) and not (re.search("\?",inp)):
        if re.search("i like ",inp):
            likekey=re.search("i like (.+).",inp).groups()[0]
        else:
            likekey=re.search("i love (.+).",inp).groups()[0]
        likereply=[tellmemore()+" about "+likekey+"!",
                   "I love "+likekey+" too!",
                   "What a incidence! I love it too!",
                   "Why do you love "+likekey+"?"]
        reply=random.choice(likereply)
    elif re.search("think",inp) or re.search("assume",inp) or re.search("suppose",inp):
            reply="Why think so?"
    elif (re.search("n't",inp) or re.search("hate",inp)) and not re.search("\?",inp):
        inp1 = inp.replace("my ", "your ")
        inp2 = inp1.replace("i ", "you ")
        famlist=["mom","dad","grandmother","sister","brother","daughter","son"]
        if re.search("hate ",inp2):
            keykey = re.search(r"hate (.+).", inp2).groups()[0]
        if re.search("hates ",inp2):
            keykey = re.search(r"hates (.+).", inp2).groups()[0]
        if re.search("n't ",inp2):
            keykey = re.search(r"n't (.+?) (.+).", inp2).groups()[1]
        reply1="What a coincidence! My "+random.choice(famlist)+\
                  " doesn't enjoy "+keykey+" too!"
        reply2="I am really sorry to hear that "+inp2+" Tell me why!"
        reply3="Why not "+keykey+"?"
        reply=random.choice([reply1,reply2,reply3])
    else:
        rand=random.random()
        if rand>0.6:
            reply=panacea()+" "+random.choice(["Hmmm... "+question(),"And "+question().lower()])
        elif rand<=0.6 and rand>=0.5:
            reply=tellmemore()+"!"
        elif rand<0.10:
            reply=farewell()
        else:
            reply=panacea()

    print("Jarvis :: "+reply)



print("Jarvis :: Morning, Tony.")
inp=input("Tony :: ").lower()

while not (re.search('hello',inp) or re.search('hi',inp) or re.search('morning',inp)):
    chatbot(inp)
    inp=input("Tony :: ").lower()


if re.search('hello',inp) or re.search('hi',inp) or re.search('morning',inp):
    print("Jarvis :: Do you enjoy food?")

while 1==1:
    inp=input("Tony :: ").lower()
    chatbot(inp)

