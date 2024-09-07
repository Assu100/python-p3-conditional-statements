#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if(username=="admin" or username=="ADMIN") and password=="12345":
        return "Access granted"

    else:
        return "Access denied"
    
admin_login("sudo", "1234")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature >= 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    
hows_the_weather(33)

def fizzbuzz(number):
    # your code here
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    
fizzbuzz(15)

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return None
    else:
        print("Invalid operation!")
        return None
    
calculator("+", 3, 5)
