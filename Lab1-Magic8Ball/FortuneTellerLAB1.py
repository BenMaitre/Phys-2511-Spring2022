
import random as rm
import time as tm

question = input("What is your question? ")

print("Thinking...")
tm.sleep(3)

num = rm.randint(0,1)
if num:
    answer = "Yes!"
else:
    answer = "No!"

print("Your Question was", question)

print("My answer is...", answer)

