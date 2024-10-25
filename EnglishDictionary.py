myDict = {}

while True:
      print("\nENGLISH DICTIONARY")
      print("\n 1. Add a word and it's definition.")
      print("\n 2. Find the definition of a word")
      print("\n 3. Exit")

      choice = int(input("Enter your choice: "))

      if choice == 1:
            word = input("Enter the word:")
            definition = input("Enter the definition: ")
            myDict[word] = definition
            print(word, " has been added to to dictionary.\n")

      elif choice == 2:
            word = input("Enter the word:")
            if word in myDict:
                  print("The definition is: ", myDict[word], "\n")
            
            else: 
                  print(word, " not found.\n")
      
      elif choice == 3:
            break

      else:
            print("Invalid Choice!!!")