import random

cards = ["queen", "king", "jack", "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #This command creates a list of cards representing a standard deck of playing cards. The list contains the face cards queen, king, jack, and ace, as well as the numbered cards from 2 to 10. Each card is represented as a string in the list.

for card in range(3):
    random.shuffle(cards) #This command will shuffle the list of cards randomly using the random.shuffle() function. The order of the cards in the list will be rearranged randomly each time this line is executed.
    print(cards[0]) #This command will print the first card in the shuffled list to the console.