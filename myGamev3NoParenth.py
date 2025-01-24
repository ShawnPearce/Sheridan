#The variables must be initialized with a random number therefore we must import the random module into our program
import random

#Next we must initialize the variables for Player 1, Player 2, and Player 3 with numbers using the random module within the range of 1 to 6
#We must do this for two roles for each player 
playerOneRollOne = random.randint(1,6)
playerOneRollTwo = random.randint(1,6)

playerTwoRollOne = random.randint(1,6)
playerTwoRollTwo = random.randint(1,6)

playerThreeRollOne = random.randint(1,6)
playerThreeRollTwo = random.randint(1,6)

#next we have to calculate the sum of each players rolls
playerOneScore = playerOneRollOne+playerOneRollTwo
playerTwoScore = playerTwoRollOne+playerTwoRollTwo
playerThreeScore = playerThreeRollOne+playerThreeRollTwo

#Now that we have initialized the variables with random numbers for each players rolls and calculated the sum
# we must print the result of each players initalization and their sum
print("Player One rolled: "+ str(playerOneRollOne) +" and "+str(playerOneRollTwo)+" Score: "+str(playerOneScore))
print("Player Two rolled: "+ str(playerTwoRollOne) +" and "+str(playerTwoRollTwo)+" Score: "+str(playerTwoScore))
print("Player Three rolled: "+ str(playerThreeRollOne) +" and "+str(playerThreeRollTwo)+" Score: "+str(playerThreeScore))

#Next we must compare the sum of each result with one another to find out the highest value
highScore=max(playerOneScore,playerTwoScore,playerThreeScore)

#Finally we must print the highest score
print("The highest score is: " +str(highScore))

scoreAverageA=playerOneScore+playerTwoScore+playerThreeScore/3
scoreAverageB=playerOneScore+playerTwoScore+playerThreeScore//3

print("The average score using the '/' operator is: "+str(scoreAverageA))
print("The average score using the '//' operator is: "+str(scoreAverageB))

