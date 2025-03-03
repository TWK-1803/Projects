from random import randint

from constants import *

def generateName():
    return BIRTHNAMES[randint(0,99)] + " " + MATRINAMES[randint(0,19)]
#Enter unadjusted result on dice
def lookupName(d100, d20):
    return BIRTHNAMES[d100-1] + " " + MATRINAMES[d20-1]

def generateBackground():
    return BACKGROUNDS[randint(0, 5)][randint(0, 5)]
#Enter unadjusted result on dice
def lookupBackground(d6_1, d6_2):
    return BACKGROUNDS[d6_1-1][d6_2-1]

def generateBirthsign():
    return " ".join(BIRTHSIGNS[randint(0,5)])
#Enter unadjusted result on dice
def lookupBirthsign(d6):
    return " ".join(BIRTHSIGNS[d6-1])

def generateCoat():
    return COATPATTERNS[randint(0,5)] + " " + COATCOLORS[randint(0,5)]
#Enter unadjusted result on dice
def lookupCoat(d6_1, d6_2):
    return COATPATTERNS[d6_1-1] + " " + COATCOLORS[d6_2-1]

def generateDetail():
    return PHYSICALDETAILS[randint(0,5)][randint(0,5)]
#Enter unadjusted result on dice
def lookupDetail(d6_1, d6_2):
    return PHYSICALDETAILS[d6_1-1][d6_2-1]

def generateBricaBrac():
    return BRICABRACS[randint(0,5)][randint(0,7)]
#Enter unadjusted result on dice
def lookupBricaBrac(d6, d8):
    return BRICABRACS[d6-1][d8-1]

def generateAttribute():
    temparr = [randint(1,6),randint(1,6),randint(1,6)]
    temparr.sort()
    return str(temparr[1] + temparr[2])

def generateMice(numMice):
    for n in range(numMice):
        name = generateName()
        attributes = " ".join([generateAttribute(), generateAttribute(), generateAttribute()])
        hp = randint(1,6)
        pips = randint(1,6)
        background = lookupBackground(hp, pips)
        equipment = ", ".join(["Torches","Rations","Weapon of choice",background[1],background[2]])
        occupation = background[0]
        birthsign_disposition = generateBirthsign()
        coat = generateCoat()
        physicaldetail = generateDetail()
        bricabrac = generateBricaBrac()
        print("Mouse # {}\n--------------\nName: {}\nAttributes: {}\nHP: {}\nPips: {}\nEquiment: {}\nBric-a-brac: {}\nBackground: {}\nBirthsign and Disposition: {}\nCoat: {}\nPhysical Details: {}\n".format(n+1,name,attributes,hp,pips,equipment,bricabrac,occupation,birthsign_disposition,coat,physicaldetail))

generateMice(1)