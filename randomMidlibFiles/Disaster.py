def disaster():
    funnyName=input("Funny Name: ")
    planetName=input("Planet Name: ")
    adj1=input("Adjective: ")
    noun1=input("Noun: ")
    verb1=input("Verb Ending in ING: ")
    noun2=input(" Plural Verb: ")
    sport = input(" Sport Name: ")
    food = input(" Food Name: ")
    midLib=(f"I boarded a spaceship named {funnyName} to explore the planet {planetName}.\n"
            f"My mission was to find the legendary {adj1} alien who supposedly controls the universe with a {noun1}.\n"
            f" Everything was going well until my robot assistant started {verb1} uncontrollably. Suddenly, three {noun2} appeared outside the window and challenged me to a game of {sport}. \n"
            f"I lost badly, so the aliens forced me to eat {food} for breakfast, lunch, and dinner for the rest of my life.")
    print(midLib)

if __name__ == '__main__':
    disaster()
