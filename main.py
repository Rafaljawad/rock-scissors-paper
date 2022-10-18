
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


my_choice=int(input("what do you choose? type 0 for rock and 1 for paper and 2 for scissors :"))
print(type(my_choice))
computer_choice=random.randint(0,2)
print(type(computer_choice))
image_option=[rock,paper,scissors]
if(computer_choice and my_choice>=len(image_option)):
    print("invalid number, you lose")

elif(my_choice == computer_choice):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n drwa")
elif(my_choice==0 and computer_choice==1):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")
elif(my_choice==1 and computer_choice==0):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n you win")
elif(my_choice==2 and computer_choice==1):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n you win")
elif(my_choice==0 and computer_choice==2):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\ nyou win")
elif(my_choice==1 and computer_choice==2):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")
elif(my_choice==2 and computer_choice==0):
    print(f"computer chose:{image_option[computer_choice]}\n your choice is:{image_option[my_choice]}\n computer wins")