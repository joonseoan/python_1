# [ ------------------------ Day3 ----------------------------------- ]
# ======== Logical operator ========
print("")
print("======= Logical Operators =======")

# and, or, not


height_ = int(input("What is your height in cm? "))

if height_ > 120:
  print("You can ride the rollercoaster!")
  _age = int(input("How old are you? "))
  _bill = 0

  # [IMPORTANT!!!]
  # Python does not need to use "return" even though the condition satisfies the multiple if statement.
  # which means if it satisfies the first if statement, it automatically break.
  if _age < 12:
    bill = 5
  elif _age < 17:
    bill = 8
  elif _age > 45 and _age <= 60:
    bill = 1
  else:
    bill = 12

  _want_photo = input("Do you want photo? ")
  
  if _want_photo == "Y":
    bill += 3
    
  print(f"Your total bill is ${bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")


# ======== Multiple if statements ========
print("")
print("======= multiple if statements =======")

height_ = int(input("What is your height in cm? "))

if height_ > 120:
  print("You can ride the rollercoaster!")
  _age = int(input("How old are you? "))
  _bill = 0

  # [IMPORTANT!!!]
  # Python does not need to use "return" even though the condition satisfies the multiple if statement.
  # which means if it satisfies the first if statement, it automatically break.
  if _age < 12:
    bill = 5
  elif _age < 17:
    bill = 8
  else:
    bill = 12

  _want_photo = input("Do you want photo? ")
  
  if _want_photo == "Y":
    bill += 3
    
  print(f"Your total bill is ${bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")

# ======== if ~ elif ~ else ====
print("")
print("======= if ~ elif ~ else =======")

_height = int(input("What is your height in cm? "))

if _height > 120:
  print("You can ride the rollercoaster!")
  _age = int(input("How old are you? "))
  if _age > 18:
    print("Please pay $15.")
  elif _age > 12:
    print("Please pay $12.")
  else:
    print("Please pay $7.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# ======== if ~ else ====
print("")
print("============= if ~ else ============")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# [IMPORTANT]
# Operators: >, <, >=, <=, ==, !=  (Same as the one in Java)

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# [ ------------------------ Day2 ----------------------------------- ]

# ======= Project ===========
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("")
print("================ project =================")
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_persons = int(input("How many people to split the bill? "))
pay_per_person = (total_bill * (1 + tip_percent / 100)) / num_persons
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${pay_per_person}")

# [IMPORTANT]
# two decimal number does not always work in terms of even 00, 50 etc.
# In this case, it print like 22 or 22.5 (not 22.00 or 22.50)
# print(f"Each person should pay: ${round(pay_per_person, 2)}")

# ======== Mathmatical operator ====
print("======== Number Manipulation ===========")
8 / 3  # 2.6666666666666
print(int(8 / 3))  # [IMPORTANT] 2 because it chops off the decimal numbers without any rounding!
print(round(8 / 3))  # 3 because of rounding
print(round(8 / 3, 2))  # 2.67 because 2 is the number of decimal numbers

# directly converting float to integer
print(8 // 3)  # 2 because it chops off the all decimal numbers
print(type(8 // 3))  # int class

# chaining variables
result = 4 / 2
print(result)  # 2.0

# It is same as 'result = result / 2'
# we can use *=, /=, +=, -=
result /= 2
print(result)  # 1.0

# f-String: chaning all types of value to string.
# We do not need to use str() for casting
score = 0
height = 1.9
isWinning = True
print(f"Your score is {score}, your height is {height}, and your are winning is {isWinning}")  # Same thing in Java and javascript

print("======== Math operator ===========")
3 + 5
7 - 4
3 * 2
6 / 3
6 % 2
print(6 / 3)  # [IMPORTANT] it always returns float type! -> 2.0

# [IMPORTANT]: exponent! to increase power
exp = 2**3  # 8
print(exp)  # 8

# PEMDAS (Prioirty) with LR (left to right)
# ()
# **
# * / (always left one first)
# + - (always left one first)

print(3 / 3 + 3 * 3 - 3)  # / * have the same priority so that left one "/" first. --> 7.0

#  ======= Data Types: String (str), Integer (int), Float (float), Bloean (bool) ===
print("======== Data type ===========")
# 1) String
print("Hello"[0])
print("Hello"[4])
print("123" + "456")

# 2) Integer
print(123 + 456)
# for large number, we can use "_" intead of ","
print(123_456_789)  # "_" will be replaced wit "" in print

# 3) Float
print(3.14334324332523425324346345653563456354653465346
      )  # 3.1433432433252344 (16th decimal digit only)

# 4) Boolean
True  # works!!!
False  # works!!!

# --- type conversion ---

# len works only for String
# len(123) # type error

name_char = len(input("What is your name? "))

# check type
_type = type(
    name_char)  # IMPORTANT type() returns object type, not a String type.
print(_type)  # It cannot concatenated with String

# if it is not the same type, conver it to the correct type.
name_char = str(name_char)

# Without converting type, it will generate an error
# because 'len' returns integer type.
# Then the integer type cannot concatenated with String (it can Java and Javascript)
print("Your name has " + name_char + " characters")

a = int("123")
b = str(123)
bb = float(b)
print(a + bb)  # 246.0 because is float has more comprehensive scope

c = a == b
print(c)
d = float(b)
print(type(d))

# Error
# e = int("afdadfaf")  # invalid literal error

print()
# [ ------------------------ Day1 ----------------------------------- ]
# Write your code below this line 👇

# ------------------- print function -------------------------
print("Print function")
print("--------------")
print("")

# 0) space (indentation) error
# (space)  print("Hello World!") ===> IndentaionError

# 1) String
print("Hello World!")  # Double quotes
print("Hello World!" + ' in Python')  # Single quote
print("Hello World!" + " in Python")  # + operator
print("Hello World!", " in Python")  # comma ==> another space
print("Hello World!"
      " in No Space")  # no space (not different from a single space below)
print("Hello World!"
      ' in Single Space')  # Single space

# 2) Manipulation
# (1) next line
print("hello\nhello\nhello")
# (2) String Concatination
print("Hello", "Angela")
print("Hello" + " " + "Angela")
print("Hello" + " Angela")

# -------------------- input function ------------------------
# Usage: when we need to give some data after `print`
# The user can enter some data from the console.
# After the user enters some data, the input function is replaced with the user input.

print("")
print("input function")
print("--------------")
print("")

input("What is your name?")
print("Hello " + input("What is the programmer name?"))
# Get length of string (It start with index 1, not 0)
# Also must think about the space. The space should be relfected for the start poistion
# of the returned value.
print(len(input("What is your name? ")))

# ---------------------- variable -------------------------------
# store the value assigned to the variable.
print("")
print("variable")
print("--------------")
print("")

name = input(
    "What is your name? ")  # input returns the input value from the user.
print(name)

# variable can be reused
name = "Angela"
print(name)
length = len(name)
print(length)

# ---- Final project ------
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city, pet)
