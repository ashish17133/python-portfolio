
def wedding():
    personName = input("Person's name: ")
    adj1 = input("Adjective: ")
    place = input("Place: ")
    pluralNoun1 = input("Plural noun: ")
    animal = input("Animal: ")
    exclamation = input("Exclamation: ")
    verb1 = input("Verb ending with ING: ")
    noun1 = input("Noun: ")
    food = input("Food: ")
    pluralNoun2 = input("Another plural noun: ")
    adj2 = input("Another adjective: ")
    country = input("Country: ")

    midLib = (
        f"My cousin {personName} decided to get married in a {adj1} "
        f"ceremony inside a {place}.\n"
        f"The bride wore a dress made entirely of {pluralNoun1}, "
        f"while the groom arrived riding a {animal}.\n"
        f"During the vows, the priest accidentally shouted "
        f"\"{exclamation}!\", causing everyone to start {verb1}.\n"
        f"The wedding cake was shaped like a giant {noun1}, "
        f"and the DJ played nothing but songs about {food}.\n"
        f"By the end of the night, even the {pluralNoun2} were dancing, "
        f"and everyone agreed it was the most {adj2} wedding "
        f"in {country}!"
    )

    print(midLib)


if __name__ == '__main__':
    wedding()
