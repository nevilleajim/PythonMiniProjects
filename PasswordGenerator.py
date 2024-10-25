import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Python Password Generator.")

nrLetters = int(input("Enter the number of letters you require in your password: "))  #3
nrSymbols = int(input("Enter the number of symbols you require in your password: "))  #4
nrNumbers = int(input("Enter the number of numbers you require in your password: "))  #2

Password = []

for i in range(nrLetters):
      Password.append(letters[random.randint(0, len(letters))])

for i in range(nrNumbers):
      Password.append(numbers[random.randint(0, len(numbers))])

for i in range(nrSymbols):
      Password.append(symbols[random.randint(0, len(symbols))])

random.shuffle(Password)
sPassword = ''
for i in Password:
      sPassword = sPassword + i

print("Your password is ", sPassword)