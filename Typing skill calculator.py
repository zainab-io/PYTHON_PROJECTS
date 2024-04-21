from time import *
import random as r

#for counting mistake
def mistake(paragraphtest,usertest):
    error = 0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest[i] != usertest[i]:
                error= error +1
        except :
            error= error +1
    return error

#for speed counting
def time_speed(time_start,time_end,userinput):
    time_delay = time_end-time_start
    time_round = round(time_delay,2)
    speed = len(userinput)/ time_round
    return round(speed)
    


while True:
    ck = input(" Ready to test : YES / NO : ")
    if ck == "YES":
        test = ["Love is a complex and multifaceted emotion that transcends cultural boundaries and defies easy definition. Love has the power to inspire, uplift, and connect us with others on a profound level, enriching our lives in countless ways. It is a force that drives us to act with kindness, compassion, and understanding, fostering empathy and unity within communities and across the globe.",
        "Friendship is like a garden that needs nurturing and care. It's a bond that grows with shared experiences, trust, and understanding . In the tapestry of life, friendship is one of the most vibrant threads, weaving its way through our happiest moments and our darkest days, reminding us that we're never alone on this journey.","Your love is the anchor that steadies my soul, and your presence, the light that guides me home. In your arms, I've found my sanctuary, and in your heart, my forever home."]

        test1 = r.choice(test)
        print("          **** Typing speed ****")
        print(test1)
        print()
        print()
        print()

        #for counting time
        time1 = time()
        testinput = input("  Enter : ")
        time2 = time()

        print(" Speed : " ,time_speed(time1,time2,testinput),"w/sec")
        print(" Error : " ,mistake(test1,testinput))
    elif ck == "NO" :
        print(" THANK YOU ")
        break
    else:
        print( "WRONG INPUT")