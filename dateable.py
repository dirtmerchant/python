#!/usr/bin/env python

def dateable():

    yourAge = int(input("How old are you: "))
    theirAge = int(input("How old are they: "))

    dateable = yourAge * .5 + 7

    if theirAge < 18:
        print('pedo')
    elif dateable <= theirAge:
        print('dateable')
    else:
        print('creepy')
