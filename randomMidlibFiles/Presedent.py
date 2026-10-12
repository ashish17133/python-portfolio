def Presedent():
    country= input("Country: ")
    pluralNoune = input("Plural Noune:  ")
    noun1 = input("Noun: ")
    adj1 = input("Adjective: ")
    noun2 = input(" Plural Verb: ")
    verb1 = input(" Verb ending with ed: ")
    verb2 = input(" Verb Ending with ING:")
    adj3=input("Adjestive: ")
    food = input(" Food: ")
    animal=input("Animal: ")
    midlib=(f"Yesterday, I unexpectedly became the president of {country}.\n"
            f" My first decision was to replace all the cars with {pluralNoune}.\n"
            f" I appointed my best friend as the Minister of {noun1} because they are extremely {adj1}.\n"
            f" During my first speech, I accidentally {verb1} on stage while holding a giant {noun2}. \n"
            f"The audience started {verb2}, and the news reporters called me the most {adj3} president in history. \n"
            f"By the end of the day, I had declared {food} the national treasure and made every citizen dance like a {animal} every Monday.")
    print(midlib)


if __name__ == '__main__':
    Presedent()
