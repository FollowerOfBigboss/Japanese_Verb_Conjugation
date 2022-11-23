# 28/10/2022
# Add plain and plain negative form
# Add te form
# Add polite forms for some conjugations
# Add past form


from verbs import ichidan_verbs, godan_verbs

class IchidanVerb:
    
    def removeLastThenAdd(self, suffix): 
        return self.verb[:-1] + suffix

    def __init__(self, dictionary_form): 
        self.verb = dictionary_form

    def plain(self): 
        return self.verb
    
    def plain_negative(self): 
        return self.removeLastThenAdd("ない")

    def masu(self): 
        return self.removeLastThenAdd("ます")
        
    def masen(self): 
        return self.removeLastThenAdd("ません")

    def past(self): 
        return self.removeLastThenAdd("た")

    def negative_past(self): 
        return self.removeLastThenAdd("なかった")
    
    def mashita(self):
        return self.removeLastThenAdd("ました")
    
    def masendeshita(self):
        return self.removeLastThenAdd("ませんでした")
    
    def te(self): 
        return self.removeLastThenAdd("て")
        
    def negative_te_nakute(self): 
        return self.removeLastThenAdd("なくて")
    
    def negative_te_naide(self): 
        return self.removeLastThenAdd("ないで")

    def te_mashite(self):
        return self.removeLastThenAdd("まして")

    # Use it as reference only
    # Used rarely as far as I understand
    # Not worth to add tests
    def te_masende(self):
        return self.removeLastThenAdd("ませんで")
    
    def progressive(self):
        return self.removeLastThenAdd("ている")
        
    def volitional(self):
        return self.removeLastThenAdd("よう")
        
    def imperative(self):
        return self.removeLastThenAdd("ろ")

    def request(self):
        end = self.te() + "ください"
        return end
    
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

    def past(self):
    
        pastLUT = {
            "う":"っ",
            "く":"い",
            "ぐ":"い",
            "す":"し",
            "つ":"っ",
            "ぬ":"ん",
            "む":"ん"
        }
        
        taLUT = {
            "う":"た",
            "く":"た",
            "ぐ":"だ",
            "す":"た",
            "つ":"た",
            "ぬ":"だ",
            "む":"だ"            
        }
        end = pastLUT[self.verb[-1]] + taLUT[self.verb[-1]]
        return self.verb[:-1]+end
        
    def negative_past(self):
        
        pastLUT = {
            "う":"わ",
            "く":"か",
            "ぐ":"が",
            "す":"さ",
            "つ":"た",
            "ぬ":"な",
            "む":"ま"
        }
        
        end = pastLUT[self.verb[-1]] + "なかった"
        return self.verb[:-1] + end
        
    def mashita(self):
        pastLUT = {
            "う":"い",
            "く":"き",
            "ぐ":"ぎ",
            "す":"し",
            "つ":"ち",
            "ぬ":"に",
            "む":"み"
        }
        
        end = pastLUT[self.verb[-1]] + "ました"
        return self.verb[:-1] + end    
    
    def masendeshita(self):
        pastLUT = {
            "う":"い",
            "く":"き",
            "ぐ":"ぎ",
            "す":"し",
            "つ":"ち",
            "ぬ":"に",
            "む":"み"
        }
        
        end = pastLUT[self.verb[-1]] + "ませんでした"
        return self.verb[:-1] + end    
    
    def te(self):
        teLUT = {
            "う":"っ",
            "く":"い",
            "ぐ":"い",
            "す":"し",
            "つ":"っ",
            "ぬ":"ん",
            "む":"ん" 
        }
        
        deLUT = {
            "う":"て",
            "く":"て",
            "ぐ":"で",
            "す": "て",
            "つ":"て",
            "ぬ":"で",
            "む":"で" 
        }
        
        end = teLUT[self.verb[-1]] + deLUT[self.verb[-1]]
        return self.verb[:-1] + end
         
    def negative_te_nakute(self):
        teLUT = {
            "う":"わ",
            "く":"か",
            "ぐ":"が",
            "す":"し",
            "つ":"た",
            "ぬ":"な",
            "む":"ま" 
        }
        
        end = teLUT[self.verb[-1]] + "なくて"
        return self.verb[:-1] + end
        
    def negative_te_naide(self):
        teLUT = {
            "う":"わ",
            "く":"か",
            "ぐ":"が",
            "す":"さ",
            "つ":"た",
            "ぬ":"な",
            "む":"ま" 
        }
        
        end = teLUT[self.verb[-1]] + "ないで"
        return self.verb[:-1] + end

    def te_mashite(self):
        teLUT = {
            "う":"い",
            "く":"き",
            "ぐ":"ぎ",
            "す":"し",
            "つ":"ち",
            "ぬ":"に",
            "む":"み" 
        }
        
        end = teLUT[self.verb[-1]] + "まして"
        return self.verb[:-1] + end

    # Use it as reference only
    # Used rarely as far as I understand
    # Not worth to add tests
    # Implementation is not expected
    def te_masende(self):
        return None
    
    def progressive(self):
        return self.te() + "いる"
        
    def volitional(self):
        volLUI = {
            "う":"お",
            "く":"こ",
            "ぐ":"ご",
            "す":"そ",
            "つ":"と",
            "ぬ":"の",
            "む":"も" 
        }
        
        end = volLUI[self.verb[-1]] + "う"
        return self.verb[:-1] + end
        
    def imperative(self):
        return "Not implemented!"
        
    def request(self):
        return "Not implemented!"