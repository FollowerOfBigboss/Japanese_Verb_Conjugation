# fast test
from verbs import ichidan_verbs, godan_verbs
from conjugation import IchidanVerb, GodanVerb

def TestGodan():
    for i in godan_verbs:
        godan = GodanVerb(i)
        print(f"Dictionary form: {i}")
        print(f"Plain form {godan.plain()}")
        print(f"Plain negative form {godan.plain_negative()}")
        print(f"masu form {godan.masu()}")
        print(f"masen form {godan.masen()}")
        print(f"past form {godan.past()}")
        print(f"negative past form {godan.negative_past()}")
        print(f"Te form: {godan.te()}")        
        print()

def TestIchidan():
    for i in ichidan_verbs:
        ichidan = IchidanVerb(i)
        print(f"Dictionary form: {i}")
        print(f"Plain form {ichidan.plain()}")
        print(f"Plain negative form {ichidan.plain_negative()}")
        print(f"Masu form {ichidan.masu()}")
        print(f"Masen form {ichidan.masen()}")
        print(f"Past form {ichidan.past()}")
        print(f"Negative past form {ichidan.negative_past()}")
        print(f"Te form: {ichidan.te()}")
        print()

def banner(text):

    banner_beg = "#-"
    banner_end = "-#\n"
    strlen = len(text)
    
    top_and_bottom = banner_beg + (strlen * "-") + banner_end
    middle = banner_beg + text + banner_end
    banner = top_and_bottom + middle + top_and_bottom
    print(banner)



if __name__ == "__main__":
    banner("hi")    
    banner("Testing godan verbs...")
    TestGodan()
    banner("Testing ichidan verbs...")
    TestIchidan()