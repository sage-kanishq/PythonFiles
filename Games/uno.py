import random
import os
import datetime


class Card:
    def __init__(self, *args, **kwargs):
        colour = ['blue','yellow','green','red','special']
        type_ = [0,1,2,3,4,5,6,7,8,9,'reverse','skip','+2']
        a = colour[random.randint(0,10)%5]
        b = type_[random.randint(0,20)%5]
        if a =='special':
            self.colour = 'special'
    
        else:
            self.colour = a 
            self.type = b


def functionality(card : Card):
    if card.colour != 'special':
        if type(card.type) != int:
            

    
a = Card()
functionality(a)

# def chooseDeck():


# class Player:
#     def __init__(self):
#         self.cards = 
        
    