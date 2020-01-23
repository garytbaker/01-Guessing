import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

playing = True

while playing:
    
    minimum = None
    while minimum == None:
        try:
            minimum = int(input("what is the smallest integer you want to guess between? "))
        except ValueError:
            print("that is not an int. Try again.\n")

    
        
    
    maximum = None
    while maximum == None:
        try:
            maximum = int(input("what is the largest integer you want to guess between? "))
        except ValueError:
            print("that is not an int. Try again.\n")
        else:
            if maximum < minimum:
                print("maximum needs to be bigger than minimum\n")
                maximum = None
                
    number = random.randint(minimum,maximum)

    guess = None
    count = 0
    while (guess != number):
        guess = int(input("Now guess the number! "))
        count+=1
        if (guess<number):
            print("It is bigger than that!")
        if (guess>number):
            print("It is smaller than that!")
        if (abs(guess-number)>(maximum-minimum)/4):
            print("you're not even close!")
        if (abs(guess-number)<(maximum-minimum)/4):
            print("you're getting closer!")
        if (abs(guess-number) == 1):
            print("you're 1 off!")
    print("Wow you got it! It only took you {tries} tries!\n".format(tries=count))
    playagain = input("Type YES to keep playing. Otherwise type something else. ")
    if (playagain.lower().strip()!= 'yes'):
        playing = False     