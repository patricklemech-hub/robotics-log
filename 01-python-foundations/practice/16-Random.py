#random library is used to generate random numbers, select random items from a list, and perform other random operations. It is commonly used in games, simulations, and other applications where randomness is desired.
import random 

coin = random.choice(["Heads", "Tails"]) #This command will randomly select either "Heads" or "Tails" from the list. The random.choice() function is used to choose a random item from the given list. In this case, it simulates a coin flip by randomly selecting one of the two options.
print(coin) #This command will print the result of the coin flip, which will be either "Heads" or "Tails" based on the random selection made in the previous line.

for i in range(5): #This loop will generate 5 random lottery numbers.
    lotery = random.randint(1,100)
    print(lotery) #This command will generate a random integer between 1 and 100 (inclusive) using the random.randint() function. The generated number will be printed to the console, simulating a lottery number selection.



card = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #This command creates a list of cards representing a standard deck of playing cards. The list contains the numbers 1 to 10, as well as the face cards J (Jack), Q (Queen), and K (King). Each card is represented as a string in the list.

for j in range(5): #This loop will shuffle the list of cards 5 times.
    random.shuffle(card) #This command will shuffle the list of cards randomly using the random.shuffle() function. The order of the cards in the list will be rearranged randomly each time this line is executed.
    print(f"{card}", sep="") #This command will print the shuffled list of cards to the console, allowing you to see the new order of the cards after each shuffle.
