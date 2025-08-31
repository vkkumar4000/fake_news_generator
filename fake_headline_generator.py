import random

import os
from tkinter import N



subjects = [
    "shahrukh",
    "virat",
    "nirmala",
    "a mumbai cat",
    "a group of monkey",
    "prime minister",
    "auto rikshaw driver from delhi",
]

actions = [
    "launches missile",
    "cancels",
    "dances with",
    "eats",
    "declairs wars on",
    "orders",
]

place_or_things = [
    "at red fort",
    "mumbai local train",
    "ganga ghat",
    "during ipl match",
    "inside parliament",
    "in rewa",
    "on top of hill",
]


#start the head line generation
while True:
    # logic for clearing console everytime;

    def clear_console():
        if os.name == "nt":   # Windows
            os.system("cls")
        else:                 # Linux / Mac
            os.system("clear")

    clear_console()

 

    print("Welcome to my program!")
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    
    headline = f"BREAKING NEWS : {subject} {action} {place_or_thing}"
    print(headline)


    user_input = input("do you want another headline (y/n)").strip().lower()
    if user_input == "n":
        break;
print("thanks for using fake headline generator")
    