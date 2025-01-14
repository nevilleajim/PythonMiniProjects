import random

lowerDigit = int(input("Enter the lower range: "))
upperDigit = int(input("Enter the upper range: "))

num = random.randint(lowerDigit, upperDigit)
flag = False

print("G\n")
print(f"Random number has been generated which ranges from {lowerDigit} to {upperDigit}.\nThe user gets 10 chances to guess the number correctly.")

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