import random

num = random.randint(1, 100)
flag = False

print("Guess the Number Game\n")
print("Random number has been generated which ranges from 1 to 100.\nThe user gets 10 chances to guess the number correctly.")

for i in range(10):
      number = int(input("Guess the number: "))

      if number == num:
            print("Congratulations!! You have guessed the number correctly...\n")
            flag = True
            break

      if number > num:
            print("The number should be lesser than the enter number...\n")

      if number < num:
            print("The number should be greater than the entered number...\n")

if flag == False:
      print("Game Over! The correct answer was ", num)