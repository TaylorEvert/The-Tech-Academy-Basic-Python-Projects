#
# Python 3.7.5
# Author: Taylor Evert
# Purpose: Creating my first python program along with the Tech Academy Instructor
# Instructor: Daniel A. Christie
#


def start(nice=0,mean=0,name=""):
    # get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get users name.
        otherwise, thank player for playing again
        and continue with game
    """
    # if we do not already have this users name, then they are new and we need their name
    
    if name != "":
        print("\nThank You for playing again, {}!".format(name))
    # get user info, describe game if new
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA strainger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables for use
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # Call again function and pass our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again> (Y/N):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)


if __name__ == "__main__":
    start()
