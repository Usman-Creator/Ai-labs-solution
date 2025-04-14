# Question no 1
numbers = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(numbers)

# Question no 2
def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    print("Temperature in Fahrenheit is:", fahrenheit)

def fahrenheit_to_celsius(f):
   celsius=(f - 32) * 5/9
   print("Temperature in Celcius is:", celsius)

celsius_to_fahrenheit(60)
fahrenheit_to_celsius(45)

# Question no 3

import random

number = random.randint(1, 9)
while True:
    guess = int(input("Guess a number (1-9): "))
    if guess == number:
        print("Well guessed!")
        break
    
# Question no 4

for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)
    
# Question no 5
word = input("Enter a word: ")
print(word[::-1])

# Question no 6

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = len([num for num in numbers if num % 2 == 0])
odd_count = len(numbers) - even_count

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

# Question no 7

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
    print(f"Item: {item}, Type: {type(item)}")
    
# Question no 8

for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num, end=" ")
    
# Question no 9

a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
    
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)    
        
        
# Question no 10  

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    result.append(row)

print("Generated 2D array:")
print(result)

# Question no 11

print("Enter lines of text (press Enter on an empty line to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line.lower())

print("\nOutput:")
for l in lines:
    print(l)


# Question no 12
binary_input = input("Enter comma-separated 4-digit binary numbers: ")

binary_numbers = binary_input.split(',')

for b in binary_numbers:
    if len(b) != 4 or any(char not in '01' for char in b):
        print(f"Invalid input: '{b}' is not a 4-digit binary number.")
        exit()
        
divisible_by_5 = []
for b in binary_numbers:
    decimal = int(b, 2)
    if decimal % 5 == 0:
        divisible_by_5.append(b)

print("Numbers divisible by 5:")
print(','.join(divisible_by_5))

# Question no 13

user_input = input("Enter a string: ")

letters = 0
digits = 0

for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)
  
  
# Question no 14
import re

password = input("Enter your password: ")

if len(password) < 6 or len(password) > 16:
    print("Invalid password: Length must be between 6 and 16 characters.")
elif not re.search(r"[a-z]", password):
    print("Invalid password: Must include at least one lowercase letter.")
elif not re.search(r"[A-Z]", password):
    print("Invalid password: Must include at least one uppercase letter.")
elif not re.search(r"[0-9]", password):
    print("Invalid password: Must include at least one digit.")
elif not re.search(r"[$#@]", password):
    print("Invalid password: Must include at least one special character ($, #, @).")
else:
    print("Password is valid.")