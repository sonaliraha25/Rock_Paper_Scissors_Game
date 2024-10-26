import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
user_choice=int(input("Choose between rock,paper and scissors..choose 0 for rock,1 for paper, 2 for scissors."))
print("User Choice:\n")
if user_choice >= 3:
    print("Invalid number is choosen..")
else:    
    print(game_image[user_choice])
computer_choice=random.randint(0,2)    
print("Computer Choice: \n")    
print(game_image[computer_choice])
if user_choice == computer_choice:
    print("The match is draw.")
elif user_choice == 0 and computer_choice == 1:
    print("Computer Win")    
elif user_choice == 1 and computer_choice == 2:
    print("Computer Win")    
elif user_choice == 0 and computer_choice == 2:
    print("You Win")  
elif user_choice == 1 and computer_choice == 0:
    print("You Win")    
elif user_choice == 2 and computer_choice == 1:
    print("You Win")        
elif user_choice == 2 and computer_choice == 0:
    print("Computer Win")    