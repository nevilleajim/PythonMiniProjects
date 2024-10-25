#data structures 
students = {} #we use a dictionary because it stores values in key - value pairs

while True:
      print("Student Grade Tracker")
      print("1. Add a student and their grade.")
      print("2. Update Student's grade.")
      print("3. Show all students grades.")
      print("4. Calculate average grade of class.")
      print("5. Exit\n")

      choice = int(input("Enter your choice: "))

      if choice == 1:
            name = input("Enter student's name: ")
            grade = float(input("Enter student's grade: "))
            students[name] = grade
            print("Student added successfully.\n")
      
      elif choice == 2:
            name = input("Enter student's name: ")
            if name in students:
                  newGrade = float(input("Enter the student's new grade: "))
                  students[name] = grade
                  print("Student grade updated successfully.\n")
            else:
                  print("Student not found!!")
      
      elif choice == 3:
            if students:
                  print("Students : Grades")
                  for index in students:
                        print(index, " : ", students[index], "\n")
            else: 
                  print("Dictionary is Empty.")
      
      elif choice == 4:
            if students:
                  totalGrade = sum(students.values())
                  avgGrade = totalGrade / len(students)
                  print("Average grade of the class: \n", avgGrade)
            else: 
                  print("Dictionary is Empty.")
      
      elif choice == 5:
            break

      else:
            print("Invalid Choice!!!")