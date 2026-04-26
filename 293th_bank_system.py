import os
import json
import random
import sys
transition = {}
def bank():
    print("Choose one of the options below")
    print("1) Create account")
    print("2) Log in")
    print("3) Exit")

def user_choice():
     while True:
         user = input("Enter your choice between 1 - 3: ")
         if(user == "1" or user == "2" or user == "3"):
             return user

def exit(user_decision):
    if(user_decision == "3"):
        print("Thanks for trying")
        sys.exit()

def register(user_decision):
    if(user_decision == "1"):
        print("Please fill the forum bellow")
        user_name = input("Enter your name: ")
        user_account_number = random.randint(10000000, 99999999)
        print(f"Your account number is {user_account_number}")
        user_pin = input("Create your pin: ")
        user_balance = 0
        print(f"Please remember your acc number: {user_account_number} and pin: {user_pin} or take screen shot")
        user_dict = {}
        user_dict["Name"] = user_name
        user_dict["Account number"] = user_account_number
        user_dict["Pin"] = user_pin
        user_dict["Balance"] = user_balance
        with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{user_account_number}_{user_pin}.txt", "w") as file:
             json.dump(user_dict, file, indent = 4)
             print("Successfully account created, For transitions please log in")
        sys.exit()

def Login(user_decision, filename):
  if(user_decision == "2"):
      print("For logging in fill the things below")
      acc_number = input("Enter acc_number: ")
      pin = input("Enter pin: ")
      try:
          with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc_number}_{pin}.txt", "r") as file:
              print("Successfully logged in")
              return acc_number, pin
      except:
           print("Incorrect account number or pin please re-consider")
     
           
           sys.exit()

def tasks():
  print("Please choose one of the tasks below")
  print("1) Deposit money")
  print("2) Withdraw money")
  print("3) Check balance")
  print("4) Check transactions")
  print("5) Exit")

def task_choice():
  user_task_choice = input("Enter your choice between 1 - 4: ")
  return user_task_choice

def end(task_decision):
  if(task_decision == "5"):
      print("Thanks for coming to our bank")
      sys.exit()

def deposit_money(acc, pin, task_decision):
  if(task_decision == "1"):
      
      try:
          deposit = int(input("Enter money deposit amount: "))
      except:
          print("Please enter a valid number")
      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}.txt", "r") as file:
                      data = json.load(file)
                      data["Balance"] += deposit
      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}.txt", "w") as file:
                      json.dump(data, file, indent = 4)
                      print("Updated balance:", data["Balance"])
      try:
                   with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}_transaction.txt", "r") as file:
                       data = json.load(file)
      except:
              data = {"Deposit": [], "Withdrawn": []}
      data["Deposit"].append(deposit)
      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}_transaction.txt", "w") as file:
              json.dump(data, file, indent = 4)

def withdraw_money(acc, pin, task_decision):
  if(task_decision == "2"):
      
      try:
          withdrawn = int(input("Enter money withdraw amount: "))
      except:
          print("Please enter a valid number")
      with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}.txt", "r") as file:
                      data = json.load(file)
                      if(data["Balance"] < withdrawn):
                          print("Insufficient balance")
                      else:
                          data["Balance"] -= withdrawn
                          with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}.txt", "w") as file:
                              json.dump(data, file, indent = 4)
                              print(f"Withdrawn: {withdrawn}, Now your balance is:", data["Balance"])
                              try:
                                  
                                  with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}_transaction.txt", "r") as file:
                                      
                                      data = json.load(file)
                              
                              except:
                                 
                                 data = {"Deposit": [], "Withdrawn": []}
                                 data["Withdrawn"].append(withdrawn)
                                 
                                 with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}_transaction.txt", "w") as file:
                                      
                                      json.dump(data, file, indent = 4)


def check_balance(acc, pin, task_decision):
  if(task_decision == "3"):
              with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}.txt", "r") as file:
                  data = json.load(file)
                  print(f"Your balance is:", data["Balance"])
def check_transaction(acc, pin, task_decision):
  if(task_decision == "4"):
              with open(f"/storage/emulated/0/Python learning/things made by Siddharth/{acc}_{pin}_transaction.txt", "r") as file:
                  data = json.load(file)
                  print("Your transactions of deposit are:", data["Deposit"])
                  print("Your transactions of withdraws are:", data["Withdrawn"])
              
  
bank()
user_decision = user_choice()
exit(user_decision)
filename = register(user_decision)
acc, pin = Login(user_decision, filename)
tasks()
task_decision = task_choice()
end(task_decision)
deposit_money(acc, pin, task_decision)
withdraw_money(acc, pin, task_decision)
check_balance(acc, pin, task_decision)
check_transaction(acc, pin, task_decision)