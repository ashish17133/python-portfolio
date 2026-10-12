
def Hotel():
    hotelName = input("Hotel name: ")
    animal = input("Animal: ")
    roomNumber = input("Room number: ")
    food1 = input("Food: ")
    verb1 = input("Verb ending with ING: ")
    adj1 = input("Adjective: ")
    noun1 = input("Noun: ")
    guestNumber = input("Number of guests: ")
    pluralNoun = input("Plural noun: ")
    food2 = input("Another food: ")

    midlib = (
        f"Last night, I checked into a hotel called {hotelName}, "
        f"where the receptionist looked suspiciously like a {animal}.\n"
        f"Room number {roomNumber} smelled like {food1}, and the curtains "
        f"kept {verb1} by themselves.\n"
        f"At midnight, a ghost wearing a {adj1} hat appeared beside my bed "
        f"and whispered, \"Please give me your {noun1}!\"\n"
        f"I screamed so loudly that {guestNumber} guests ran into the "
        f"hallway carrying {pluralNoun}.\n"
        f"It turned out the ghost was just hungry and wanted someone "
        f"to order {food2} from the hotel restaurant."
    )

    print(midlib)


if __name__ == '__main__':
    Hotel()
