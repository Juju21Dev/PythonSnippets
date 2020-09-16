# Program Card Game
# card game
# date : 12/08/2020
# author : Julien Violette

from random import *

# array with ten cells containing the card numbers
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# loop for shuffling the cards
for k in range(0, 49):
    i = randint(0, 9)
    j = randint(0, 9)
    deck[i], deck[j] = deck[j], deck[i]
    k += 1

# creation of the two sub-decks
deckA = []
deckB = []
for k in range(0, 9, 2):
    deckA.append(deck[k])
    deckB.append(deck[k + 1])

# displays the two sub-decks
print("deckA = ", deckA)
print("deckB = ", deckB)

# game part : comparison and point calculation
scoreA = 0
scoreB = 0
for k in range(0, 5):
    if deckA[k] > deckB[k]:
        print(f"trick number {k + 1} : {deckA[k]} > {deckB[k]} so A wins one point.")
        scoreA += 1
    else:
        print(f"trick number {k + 1} : {deckA[k]} < {deckB[k]} so B wins one point.")
        scoreB += 1

# displays the score
print("score : A =", scoreA, "et B =", scoreB)
