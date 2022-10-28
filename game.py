import random
from verbs import ichidan_verbs, godan_verbs
from conjugation import IchidanVerb, GodanVerb

def game():
    while True:
        SelectVerbType = random.randint(0,1)
        
        if SelectVerbType == 0:
            SelectedVerbTypeString = "Ichidan Verb"
            RandomSelectedVerb = random.choice(ichidan_verbs)
            Verb = IchidanVerb(RandomSelectedVerb)
        else:
            SelectedVerbTypeString = "Godan Verb"
            RandomSelectedVerb = random.choice(godan_verbs)
            Verb = GodanVerb(RandomSelectedVerb)
        
        RandomForm = random.randint(0,1)
        if RandomForm == 0:
            RandomFormString = "Plain Negative"
            Conjugated = Verb.plain_negative()
        else:
            RandomFormString = "Masu"
            Conjugated = Verb.masu()
        
        print(f"Conjugate the verb to {RandomFormString} form")
        print(f"{RandomSelectedVerb}")
        print(f"{SelectedVerbTypeString}")
        UserInput = input("Enter the answer: ")
        
        if UserInput == Conjugated:
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"Answer is: {Conjugated}")
        print()

if __name__ == "__main__":
    game()
