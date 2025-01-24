
#The variables must be initialized with a random number therefore we must import the random module into our program
import random
#Next we must initialize the variables for Player 1, Player 2, and Player 3 with numbers using the random module within the range of 1 to 6 
playerOne = random.randint(1,6)
playerTwo = random.randint(1,6)
playerThree=random.randint(1,6)
#Now that we have initialized the variables with random numbers we must print the result of each players initalization
print("Player One Rolled:  "+str(playerOne))
print("Player Two Rolled:  "+str(playerTwo))
print("player Three Rolled:  "+str(playerThree))
#Next we must compare each result with one another to find out wich player has the highest value
highValue = max(playerOne,playerTwo,playerThree)
#Finally we must print the highest value
print("The Highest value is "+str(highValue))




