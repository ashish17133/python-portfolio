
def superHero():
    noun1 = input("Superhero name (noun): ")
    word = input("A word: ")
    pluralNoun = input("Plural noun: ")
    name = input("Villain name: ")
    adj1 = input("Adjective: ")
    noun2 = input("Noun: ")
    food = input("Food: ")
    verb1 = input("Verb ending with ING: ")
    place = input("Place: ")
    adj2 = input("Adjective: ")
    noun3 = input("Noun (plural): ")

    madlib = (
        f"My superhero name is Captain {noun1}, and my special power "
        f"is turning invisible whenever someone says {word}.\n"
        f"Unfortunately, I am also terribly afraid of {pluralNoun}.\n"
        f"One day, a villain named {name} attacked the city using a giant "
        f"{adj1} machine that shoots {food} at innocent people.\n"
        f"I tried to save everyone by {verb1} across the rooftops, "
        f"but I accidentally landed inside a {place}.\n"
        f"The people cheered anyway because I had defeated the villain "
        f"by making them laugh with my terrible {adj2} {noun3} jokes.\n"
        f"From that day on, everyone called me the world's most "
        f"{adj2} superhero!"
    )

    print(madlib)


if __name__ == '__main__':
    superHero()
