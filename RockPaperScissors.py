import random

print("Welcome to Rock Paper and Scissors Game!!!")

while True:
      userChoice = input("Enter your choice(rock/paper/scissors): ")
      computerChoice = random.choice(['rock', 'paper', 'scissors'])

      print("User Choice: ", userChoice)
      print("Computer Choice: ", computerChoice)

      if userChoice == computerChoice:
            print("Game Tied!")
      
      elif (userChoice == 'paper' and computerChoice == 'rock')or\
      (userChoice == 'rock' and computerChoice == 'scissors')or\
      (userChoice == 'scissors' and computerChoice == 'paper'):
            print("User Wins!")
      
      else:
            print("Computer Wins!!!")

      playAgain = input("Do you wish to play again(yes/no): ")
      if (playAgain != "yes"):
            print("Thank You for playing!!!")
            break