print("-------------------------------------------   QUIZ TIME   --------------------------------------------------")

print("Hii User!....Welcome to My quiz Code.")

play = input("\nDo you want to play a Quiz of 4 Questions?:  ")

if play.lower() != "yes":
    quit()
num=input("\nPlease Enter Your Name: ")
print("\nOkay!",num,".... Let's play :)")
score = 0
print("--------------------------------------------------------------------------------------------------------------------------------")
print("There are 4 Questions in this quiz and You'll get 1 Marks for each Correct Answer.")
print("--------------------------------------------------------------------------------------------------------------------------------\n")

print("(1.) What does CPU stands for? \n")
print("(A) Center Process Unit.\n(B) Central Processing Unit.\n(C) Combined Processed Unit.\n(D) Computer Processing Unit.\n")
ans=input("Your Answer: ")
if ans.lower() == "b":
    print("Wow..that's Correct!\n\n")
    score += 1
else:
    print("Incorrect.. Right Option* is:-  B \n\n")

print("(2.) What does GPU stand for?\n ")
print("(A) Global Processing Unit\n(B) General Processed Unit\n(C) Graphics Processing Unit\n(D) Global Perameter Unit")
ans=input("\nYour Answer:")
if ans.lower() == "c":
    print("Wow..that's Correct!\n\n")
    score += 1
else:
    print("Incorrect..  Right Option* is:-  C \n\n")

print("(3.) What does RAM stand for?\n ")
print("(A) Random Access Memory.\n(B) Read Access Memory.\n(C) Random Assigned Memory.\n(D) All of These.")
ans=input("\nYour Answer:")
if ans.lower() == "a":
    print("Wow..that's Correct!\n\n")
    score += 1
else:
    print("Incorrect..Right Option* is:-  A\n\n ")

print("(4.) What does PSU stand for? ")
print("(A) Power Supply Unit.\n(B) Power Switching Unit.\n(C) Provider Specific Unit.\n(D) None Of these.")
ans=input("\nYour Answer:")
if ans.lower() == "a":
    print("Wow..that's Correct!\n\n")
    score += 1
else:
    print("Incorrect..Right Option* is:-  A \n\n")
print("----+----+-----+-----+-----+-----+----+----+----+----+----+----+----+----+----+----+----+")
print("Hey!",num,"Your"  + str( score ) + " questions are correct.")
print("You got " + str((score / 4) * 100) + "%.")
