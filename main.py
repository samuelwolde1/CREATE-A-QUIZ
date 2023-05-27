# Create a Quiz By Samuel Wolde

print("WELCOME TO THE WAR HISTORY QUIZ")

quiz_score = 0

#Question 1
print("\nWhose death lead to the start of WW1?")
answer1 = input("Q1 Answer: ").lower()

if answer1 == "archduke franz ferdinand" or answer1 == "franz ferdinand" or answer1 == "archduke ferdinand":
    print("CORRECT")
    quiz_score+= 1
else:
    print("\nINCORRECT. The answer is Archduke Franz Ferdinand")

#Question 2
print("\nWhat side was the United States on in WW1?")
answer2 = input("Q2 Answer: ").lower()

if answer2 == "allies" or "the allied powers" or "allied powers":
    print("CORRECT")
    quiz_score+= 1
else:
    print("INCORRECT. The answer is the Allied powers")

#Question 3
print("\nWhich country did Germany invade to start WW2?")
answer3 = input("Q3 Answer: ").lower()

if answer3 == "poland":
    print("CORRECT")
    quiz_score+= 1
else:
    print("INCORRECT. The answer is Poland")

#Question 4 
print("\nWho was the British Prime Minister during World War II?")
answer4 = input("Q4 Answer: ").lower()

if answer4 == "winston" or "churchill" or "winston churchill":
    print("Correct")
    quiz_score+= 1
else:
    print("Incorrect. The answer is Winston Churchill")

#Question 5 
print("\nWhich country dropped the atomic bomb on Hiroshima?")
answer5 = input("Q5 Answer: ").lower()

if answer5 == "united states" or answer5 == "us" or answer5 == "u.s.a" or answer5 == "usa" or answer5 == "america":
    print("Correct")
    quiz_score+= 1
else: 
    print("Incorrect. The answer is the United States")

#Question 6 
print("\nWhat year did WW2 end?")
answer6 = input("Q6 Answer: ").lower()

if answer6 == "1945":
    print("Correct")
    quiz_score+= 1
else:
    print("Incorrect. The answer is 1945")

print("Your Results:")
print(str(quiz_score) + "/6")


#Calculate Quiz Scores and output feedback 
if quiz_score == 6:
    print("(100%) Congratulations! You aced the quiz!")
elif quiz_score == 5:
    print("(83%) Your performance is impressive; just a little more effort for a perfect score.")
elif quiz_score == 4:
    print("(67%) Keep up the good work and aim for even higher scores in the future.")
elif quiz_score == 3:
    print("(50%) Good effort, but there's still more to learn.")
elif quiz_score == 2:
    print("(33%) You're making progress, but there is still room for improvement.")
elif quiz_score == 1:
    print("(17%) You need to study more to improve your understanding.")
else:
    print("(0%) Keep studying and reviewing the material.")