import random

quiz = {
      "What is the capital of France?" : {
            "options" : ["A. London", "B. Paris", "C. Washington", "D. New York"],
            "answer" : "B"
      },
      "Who wrote 'Romeo and Juliet'?" : {
            "options" : ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
            "answer" : "A"
      },
      "What is the Chemical symbol for water?" : {
            "options" : ["A. Wa", "B. H2O", "C. O2", "D. H2O2"],
            "answer" : "B"
      } 
}

questions = list(quiz.keys())
random.shuffle(questions)

score = 0
for question in questions:
      data = quiz[question]
      print(question)

      for option in data["options"]:
            print(option)
      
      ans = input("Enter your Choice (A/B/C/D): ")
      ans = ans.upper()

      if ans == data["answer"]:
            score += 1
      
print("Quiz has been completed. You have scored ", score, " out of ", len(quiz))