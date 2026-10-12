def Zombie():
    adj1 = input("Adjective: ")
    food = input("Food: ")
    noun1 = input("Noun: ")
    place = input("Place: ")
    funnyPhrase = input("Funny phrase: ")
    clothingItem = input("Clothing item: ")
    musicalInstrument = input("Musical instrument: ")
    number = input("Number of survivors: ")
    pluralNoun = input("Plural noun: ")
    noun2 = input("Another noun: ")
    liquid = input("Liquid: ")
    cityName = input("City name: ")

    midLib = (
        f"One morning, I woke up to discover that my entire city had been "
        f"invaded by {adj1} zombies who loved eating {food} instead of brains.\n"
        f"I grabbed my trusty {noun1} and escaped through a {place} "
        f"while shouting \"{funnyPhrase}!\"\n"
        f"My neighbor, who was wearing {clothingItem}, insisted that the "
        f"zombies could be defeated by playing {musicalInstrument} very loudly.\n"
        f"We gathered {number} survivors and formed a team called "
        f"the {pluralNoun}.\n"
        f"Our final plan was to lure every zombie into a giant {noun2} "
        f"and cover them with {liquid}.\n"
        f"Surprisingly, it worked, and we became the heroes of {cityName}!"
    )

    print(midLib)


if __name__ == '__main__':
    Zombie()
