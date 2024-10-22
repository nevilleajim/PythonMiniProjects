# A Program to check if a string is a palindrome or not
my_str = input("Enter a word: ")

#Make it suitable for caseless comparison
my_str = my_str.casefold()

#Reverse the string
rev_str = reversed(my_str)

#Check if the String is equal to its reverse
if list(my_str) == list(rev_str):
      print("It is a Palindrome.")
else:
      print("It is not a Palindrome.")