# for accessing json arrays
import json
# for random numbers, choices
import random
# for output delay,
import time
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep

# clears output depending on os
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    # print out some text
    print('hello geeks\n'*10)

    # sleep for 2 seconds after printing output
    sleep(2)

    # now call function we defined above
    clear()

# class storing body aspects
class char_body:
    def height_mixer (self):
        randheight = random.randint(58,80)
        inches = randheight % 12
        sub = randheight - inches
        feet = sub / 12

        feet = int(feet)
        inches = int(inches)

        finalheight = (str(feet) + "' " + str(inches) + "\" ")
        return finalheight
    

# class storing character backstory
class char_backstory:
    def __init__ (self, family, heritage, birthplace, language):
        self.family = family
        self.heritage = heritage
        self.birthplace = birthplace
        self.language = language

# gets name for character
class char_name:
    def __init__ (self, name):
        self.name = name

    def recieve_name (self):
        print("Welcome " + self.name)

# opens traits from json
class trait_receiver:
    def good_trait(self):
        formatted_good_traits = {}
        with open('goodtraits.json') as goodtraits:
            data = json.load(goodtraits)
            formatted_good_traits = data['good_traits']
            # for a in range(len(formatted_good_traits)):
            #     print(formatted_good_traits[a])
        return formatted_good_traits

    def bad_trait(self):
        formatted_bad_traits = {}
        with open('badtraits.json') as badtraits:
            data = json.load(badtraits)
            formatted_bad_traits = data['bad_traits']
            # for a in range(len(formatted_bad_traits)):
            #     print(formatted_bad_traits[a])
        return formatted_bad_traits

# receives and randomizes traits
class trait_mixer:
    def __init__ (self, traitone, traittwo):
        self.traitone = traitone
        self.traittwo = traittwo

    def trait_randomizer(self):
        rand_trait_one = random.choice(list(self.traitone))
        rand_trait_two = random.choice(list(self.traitone))
        rand_trait_three = random.choice(list(self.traittwo))

        while rand_trait_one == rand_trait_two:
            rand_trait_one = random.choice(list(self.traitone))

        final_traits = [rand_trait_one, rand_trait_two, rand_trait_three]

        return final_traits

# prompts user for name
def getname():
    my_name = input("What's your name?\n")

    time.sleep(1)
    name_passer = char_name(my_name)
    name_passer.recieve_name()

    print (my_name + "'s traits:")

# retrieves traits into local variables
def gettraits():
    time.sleep(1)

    good_traits = trait_receiver()
    good_traits = good_traits.good_trait()

    print("---------------------")

    bad_traits = trait_receiver()
    bad_traits = bad_traits.bad_trait()

    # passes traits from json file to be used in mixer
    trait_passer = trait_mixer(good_traits, bad_traits)
    trait_passer.trait_randomizer()

    temp = trait_mixer(good_traits, bad_traits)
    randomized_traits = temp.trait_randomizer()
    print(randomized_traits)

def getbody():
    x = char_body()
    finalweight = x.height_mixer()

    print(finalweight)

# Called Functions

getname()

gettraits()

getbody()