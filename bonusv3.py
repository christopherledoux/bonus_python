import random

cards_type = ["♠","♣","♥","♦"]
values = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]
cards = []

for card_type in cards_type:
    for value in values:
        cards.append([value,card_type])

random.shuffle(cards)

player = []
bot = []

while len(player) < 25:
    player.extend(cards)
    print(player)