def Work():
    company = input("Company name: ")
    pluralNoun = input("Plural noun: ")
    adj1 = input("Adjective: ")
    funnyPhrase = input("Funny phrase: ")
    verb1 = input("Verb ending with ING: ")
    adj2 = input("Another adjective: ")
    noun1 = input("Noun: ")

    midLib = (
        f"On my first day working at {company}, my manager asked me "
        f"to organize {pluralNoun} before noon.\n"
        f"I confidently said, \"That sounds {adj1}!\" even though "
        f"I had absolutely no idea what I was doing.\n"
        f"I accidentally sent an email containing \"{funnyPhrase}\" "
        f"to the entire company.\n"
        f"My coworkers began {verb1}, and the manager invited me "
        f"into the office to discuss my {adj2} performance.\n"
        f"Somehow, I got promoted to Chief Executive of {noun1} "
        f"because nobody else wanted the job."
    )

    print(midLib)


if __name__ == '__main__':
    Work()
