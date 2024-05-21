import random

while True:
  
    airandom = random.randint(1, 6)
    if airandom == 1 or airandom == 2:
        aichoice = "scissors"
    elif airandom == 3 or airandom == 4:
        aichoice = "rock"
    else:
        aichoice = "paper"

  
    playerinput = input("\nRock, Paper or Scissors\n").lower()
    if playerinput == "rock" or playerinput == "scissors" or playerinput == "paper":
        
        if aichoice == playerinput:
            print("\nPlayer:" + playerinput)
            print("Computer:" + aichoice)
            print("It's a tie!")
        elif aichoice == "paper" and playerinput == "rock":
            print("\nPlayer: " + playerinput)
            print("Computer: " + aichoice)
            print("Computer wins!")
        elif aichoice == "scissors" and playerinput == "rock":
            print("\nPlayer: " + playerinput)
            print("Computer: " + aichoice)
            print("Player wins!")
        elif aichoice == "scissors" and playerinput == "paper":
            print("\nPlayer: " + playerinput)
            print("Computer: " + aichoice)
            print("Computer wins!")
        elif aichoice == "rock" and playerinput == "scissors":
            print("\nPlayer: " + playerinput)
            print("Computer: " + aichoice)
            print("Computer wins!")
        elif aichoice == "paper" and playerinput == "scissors":
            print("\nPlayer: " + playerinput)
            print("Computer: " + aichoice)
            print("Player wins!") 
    else:
        print(playerinput + " was not a valid choice, try again!")
