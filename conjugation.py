# 28/10/2022
# Add plain and plain negative form
# (TODO) polite form 



from verbs import ichidan_verbs, godan_verbs

class IchidanVerb:
    
    def removeLastThenAdd(self, word, suffix):
        return word[:-1]+suffix

    def __init__(self, dictionary_form):
        self.verb = dictionary_form

    def plain(self):
        return self.verb
    
    def plain_negative(self):
        return self.removeLastThenAdd(self.verb, "ない")

    def masu(self):
        return self.removeLastThenAdd(self.verb, "ます")
        
    def masen(self):
        return self.removeLastThenAdd(self.verb, "ません")

#
#    def mashita(self):
#         return removeLastThenAdd(self.verb, "ました")
#    def past(self):
#        return removeLastThenAdd(self.verb, "た")

class GodanVerb:

    def __init__(self, dictionary_form):
        self.verb = dictionary_form

    def plain(self):
        return self.verb
        
    def plain_negative(self):
        NegativeLUT = {
            "う": "わ",
            "く": "か",
            "ぐ": "が",
            "す": "さ",
            "つ": "た",
            "ぬ": "な",
            "む": "ま",
            
            # Exceptions
            "る": "ら"
        }
        end = NegativeLUT[self.verb[-1]] + "ない"
        return self.verb[:-1]+end
    
    def masu(self):
        masuLUT = {
            "う":"い",
            "く":"き",
            "ぐ":"ぎ",
            "す":"し",
            "つ":"ち",
            "ぬ":"に",
            "む":"み",
            
            # Exceptions
            "る":"り"
        }
        end = masuLUT[self.verb[-1]] + "ます"
        return self.verb[:-1]+end

    def masen(self):
        masuLUT = {
            "う":"い",
            "く":"き",
            "ぐ":"ぎ",
            "す":"し",
            "つ":"ち",
            "ぬ":"に",
            "む":"み",
            
            # Exceptions
            "る":"り"
        }
        end = masuLUT[self.verb[-1]] + "ません"
        return self.verb[:-1]+end
        

