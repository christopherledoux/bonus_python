import random
import numpy as np

cards_type = ["♠","♣","♥","♦"]
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
cards = []

for value in values:
    for card_type in cards_type:
        cards.append([value,card_type])

cards_array = np.array(cards,dtype=object)
random.shuffle(cards_array)

player,bot = np.split(cards_array,2)

print(cards_array)

