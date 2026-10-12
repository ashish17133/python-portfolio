# This is a sample Python script.

from randomMidlibFiles import Disaster,Hotel,Presedent,SuperHero,Wedding,Work,Zombie

import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listOfMadlib=[Disaster.disaster,Presedent.Presedent, SuperHero.superHero,Work.Work,Hotel.Hotel,Wedding.wedding,Zombie.Zombie]
    randNumber=random.randint(0,len(listOfMadlib)-1)
    listOfMadlib[randNumber]()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
