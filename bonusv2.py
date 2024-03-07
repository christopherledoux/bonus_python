import random
import numpy as np
# import emoji
# print(emoji.emojize(f"{value} {type}"))
# cards = [["♠","♣","♥","♦"]["As","Roi","Dame","Valet","10","9","8","7","6","5","4","3","2"]]
# types = ["♠","♣","♥","♦"]
# values = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]

cards = [["2","♠"],["3","♠"],["4","♠"],["5","♠"],["6","♠"],["7","♠"],["8","♠"],["9","♠"],["10","♠"],["Valet","♠"],["Dame","♠"],["Roi","♠"],["As","♠"],["2","♣"],["3","♣"],["4","♣"],["5","♣"],["6","♣"],["7","♣"],["8","♣"],["9","♣"],["10","♣"],["Valet","♣"],["Dame","♣"],["Roi","♣"],["As","♣"],["2","♥"],["3","♥"],["4","♥"],["5","♥"],["6","♥"],["7","♥"],["8","♥"],["9","♥"],["10","♥"],["Valet","♥"],["Dame","♥"],["Roi","♥"],["As","♥"],["2","♦"],["3","♦"],["4","♦"],["5","♦"],["6","♦"],["7","♦"],["8","♦"],["9","♦"],["10","♦"],["Valet","♦"],["Dame","♦"],["Roi","♦"],["As","♦"],]

# print("liste originale : ")
# for card in cards:
#     print(card)
# random.shuffle(cards)
# print("La nouvelle liste : ")
# for card in cards:
#     print(card)

cards_array = np.array(cards)
random.shuffle(cards_array)
player,bot = np.split(cards_array,2)

print("joueur")
print(player)
print("bot")
print(bot)