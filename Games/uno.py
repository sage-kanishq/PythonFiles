import random
import os
import numpy as np
class Card:
    def __init__(self, *args, **kwargs):
        colour = np.array(['blue','yellow','green','red','special'])
        type_ = np.array([0,1,2,3,4,5,6,7,8,9,'reverse','skip','+2'])
        a = colour[random.randint(0,10)%5]
        b = type_[random.randint(0,14)%13]
        if a =='special':
            self.colour = 'special'
            type_ = np.array(['blank','wild','+4'])
            self.type = type_[random.randint(0,4)%3]
    
        else:
            self.colour = a 
            self.type = b
class Player():
    def __init__(self):
        self.cards = np.array([])
        for i in np.arange(7):
            self.cards = np.append(self.cards,Card())  
            print(self.cards[i].colour,self.cards[i].type)     

player1 = Player()
print(x for x in np.nditer(player1.cards,[],['refs_ok']))

# def next_chance(active:Card):
#     if active = 

# def functionality(card : Card):
#     if card.colour != 'special':
#         if type(card.type) != int:
            

    


# # def chooseDeck():


# # class Player:
# #     def __init__(self):
# #         self.cards = 
        
    