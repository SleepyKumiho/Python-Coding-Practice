# Based on the codeacademy 8-ball project

import random
import time

name = input("What is your name?\n").strip()
question = input("What is your question?\n").strip()

if name != "":
  print(f"{name} asks: {question}?")
else:
  print(question + "?")

time.sleep(random.randint(1,5))

random_number = random.randint(1, 9)
match random_number:
  case 1: 
    print("Yes - definitely")
  case 2: 
    print("It is decidedly so")
  case 3: 
    print("Without a doubt")
  case 4:
    print("Reply hazy, try again")
  case 5: 
    print("Ask again later")
  case 6: 
    print("Better not tell you now")
  case 7: 
    print("My sources say no")
  case 8: 
    print("Outlook not so good")
  case 9: 
    print("Very doubtful")
  case _:
    print("Error")