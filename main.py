print("")
# ======================= Day 8 ==============================
print("====================== Day8 =================")

print("")
print("------- Chellnge - Cyphering and Decyphering part 1 --------")
print("")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text, shift):
    # [Lecture]
    encrypted_word = ""

    for ordered_char in text:
        new_index = shift + alphabet.index(ordered_char)

        if new_index >= len(alphabet):
            new_index = new_index - len(alphabet)

        encrypted_word += alphabet[new_index]

    print(encrypted_word)

    # [My way]
    # encrypting_alphabet = alphabet[shift:] + alphabet[:shift];
    # encrypted_word = ""

    # for order_char in text:
    #     index = alphabet.index(order_char)
    #     encrypted_word += encrypting_alphabet[index]

    # print(f"The encoded text is {encrypted_word}")


# https://www.learnbyexample.org/python-list-slicing/

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)

print("")
print("------- Practice 2 --------")
print("")

#Write your code below this line 👇

def prime_checker(number):
    prime_message = "It's a prime number."
    no_prime_message = "It's not a prime number."

    if number == 1:
        print(no_prime_message)
        return

    for divider in range(2, number):
        if number % divider == 0:
            print(no_prime_message)
            return

    print(prime_message)


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


print("")
print("------- Practice 1 --------")
print("")

import math

def paint_calc(height, width, cover):
    total = math.ceil(height * width / cover)
    print(f"You'll need {total} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

print("")
print("------- More than 1 inputs --------")
print("")

def greet_with(name, location):
    print(f"Your name is {name}")
    print(f"Your location is {location}")

# 2) "Keyword arguments": do not need to follow the parameter position
greet_with(location="New Jersey", name="Andrew")

# 1) Need to follow positional argument rule
greet_with("Tom", "Toronto")

print("")
print("------- Inputs: Parameter vs Argument --------")
print("")

# "name" is Parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# "Micaheal, 123, False" are Arguments
greet_with_name("Michael")
greet_with_name(123)
greet_with_name(False)

print("")
# ======================= Day 7 ==============================
print("====================== Day 7 =================")

print("")
print("------- hangman step 5 --------")
print("")

# [Final Result]
# https://replit.com/@JoonAn1/Day-7-Hangman-5-Start#main.py
# Need to review List section from the lecture and compare to https://developers.google.com/edu/python/lists#range

print("")
print("------- hangman step 4 --------")
print("")

import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # guessIsIncluded = False

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            # guessIsIncluded = True
            display[position] = letter

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."

    # 2) better. It works for String
    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("Sorry, you lost!!!")

    # 1) [Mine]
    # if guessIsIncluded == False:
    #     lives -= 1
        # if lives == 0:
        #     end_of_game = True
        #     print("Sorry, you lost!!!")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # It works for List
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

print("")
print("------- hangman step 3 --------")
print("")

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

def printGuess():
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
    
        if letter == guess:
            display[position] = letter

# [IMPORTANT!!!]
# "_" in display: if "_" exist in list
# "_" not in display: if "_" does not exist in list

# 2)
while "_" in display:
    
# 1) mine
# while display.count("_") > 0:
    printGuess()
    print(display)

print("Success!! You won")

print("")
print("------- hangman step 2 --------")
print("")

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

word_length = len(chosen_word)

# 2)
for _ in range(word_length):

# 1)
# for _ in chosen_word:
    display += '_'
    # 1) mine
    # letter_list.append('_')

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


for position in range(word_length):
    if chosen_word[position] == guess:
        display[position] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

print("")
print("------- hangman step 1 --------")
print("")

# Review List
# https://developers.google.com/edu/python/lists#for-and-in

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = (input("guess a letter in the word: ")).lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for ch in chosen_word:
    if ch == guess:
        print("right")
    else:
        print("wrong")


print("")
# ======================= Day 6 ==============================
print("====================== Day6 =================")

print("")
print("------- while loop challenge --------")
print("")

# Challenge
# Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left();
#     turn_left();
#     turn_left();

# It is for to prevent the infinite loop in some position.
# while front_is_clear():
#     move();
# It is same as the one below
# turn_left();
              
# while not at_goal():
#     if right_is_clear():
#         turn_right();
#         move();
#     elif front_is_clear():
#         move();
#     else:
#         turn_left();


# [4] hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left();
#     turn_left();
#     turn_left();
#     move();
#     while wall_on_right():
#         if front_is_clear():
#             move();
#         else:
#             break;
          
# def runHurdle():
#     turn_left();
#     while wall_on_right():
#         move();
#     turn_right();
#     turn_right();
#     turn_left();
    
# while not at_goal():
#     if front_is_clear():
#         move();
#     else:
#         runHurdle();


# [3] hurdle 3 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left();
#     turn_left();
#     turn_left();
#     move();

# def runHurdle():
#     turn_left();
#     move();
#     turn_right();
#     turn_right();
#     turn_left();
    
# while not at_goal():
#     if front_is_clear(): move();
#     else: runHurdle()

print("")
print("------- while loop -----------")
print("")

# for vs while
# ----------------------------------
    # 1)
    # for item in list_of_items:
        #Do something to each item

    # 2)
    # for number in range(a, b, c)
    #            or
    # for number in range(a) ---> 0 to a - 1
    #    print(number);

    # Use when condition is avaiable and there is no specific range 
    # while something_is_true:
    #    Do something repeatedly
# -----------------------------------

# [2] hurdle 2
# [My Solution]
# def move_turn_right():
#     move();
#     turn_left();
#     turn_left();
#     turn_left();

# def move_turn_left():
#     move();
#     turn_left();

# def runHurdle():
#     for num in range(0, 4):
#         if num == 0 or num == 3: move_turn_left();
#         else: move_turn_right();

# number_of_hurdles = 6;

# 2)
# while not at_goal():
#     runHurdle();

# 1)
# while number_of_hurdles > 0:
#    runHurdle();
#    number_of_hurdles -= 1;

print("")
print("------- function -----------")
print("")

# built-in functions
# https://docs.python.org/3/library/functions.html

# custom function
# keyword `def` which is defining a function.
# name, for instance, "my_function"
# finishing : which means everything comes after this line and the indented
# belongs with the function.

# def my_function():
# do this
# Then do this
# Finally do this


def my_function():
  print("Hello")
  print("Bye")


# call the function
my_function()

# [1] hurdle 1
# Get reeborg's world in google. And try.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# [My Solution]
# def move_turn_right():
#     move();
#     turn_left();
#     turn_left();
#     turn_left();

# def move_turn_left():
#     move();
#     turn_left();

# def runHurdle():
#     for num in range(0, 4):
#         if num == 0 or num == 3: move_turn_left();
#         else: move_turn_right();

# for num in range(0, 6):
#     runHurdle();
# [ ------------------------ Day 5----------------------------------- ]
# ============= Challenge =============
print("")
print("===== Challenge =====")
print("")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# My SOLUTION
# password_array = [];
password = "";

for num in range(0, nr_letters):
  random_letter = random.choice(letters);
  password += random_letter;

# My SOLUTION
# random_letter = random.randint(0, len(letters) - 1);
# password_array.append(letters[random_letter]);

# [IMPORTANT!!!!!]
# Same as above
# password_array += letters[random_letter];


for num in range(0, nr_symbols):
  random_symbol = random.choice(symbols);
  password += random_symbol;

# My SOLUTION
# random_symbol = random.randint(0, len(symbols) - 1);
# password_array.append(symbols[random_symbol]);

for num in range(0, nr_numbers):
  random_number = random.choice(numbers);
  password += random_number;

# My SOLUTION
# random_number = random.randint(0, len(numbers) - 1);
# password_array.append(numbers[random_number]);

print("".join(random.sample(password, len(password))));

# My SOLUTION
# IMPORTANT `random.shuffle` to shuffle the order of the array elements
# random.shuffle(password_array);

# My SOLUTION
# IMPORTANT `string.join` to make the string from the array!!!
# print(password.join(password_array));
# ============= for in loop with Range =============
print("")
print("===== for in loop with Range =====")
print("")

# [Basic format]
# between a and b (`a` is inclusive, but `b` is not inclusive)
# It works only with `add`
# for number in range(a, b):
#   print(number);

# [Example]
# By default the number increases number++ without the thrid arg.
# If we want to incarease step by 2
for _number in range(0, 10, 2):
  print(_number);

# Opposite way (from the greater number)
for _number in range(10, -2, -2):
  print(_number);

# ============= for in loop =============
print("")
print("for in loop")
print("")

fruits = ["Apple", "Mango", "Peach", " Pear"]

for fruit in fruits:
  print(fruit);
  print(fruit, "pie");
  # indentation is important!
  print(fruits);
print(fruits)

# [ ------------------------ Day4 ----------------------------------- ]
# ============= Final Project =============
print("")
print("===== sum ====")
print("")

numbers = [2, 3, 4, 6];
# [IMPORTANT]
print(sum(numbers));
print(max(numbers));
print(min(numbers));


print("")
print("==== Final Project in Day 4 ====")
print("")

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

#Write your code below this line 👇
import random;

all = [rock, paper, scissors];

user_input = int(input("Select 1: rock, 2: paper or 3: scissors --> "));
print(all[user_input - 1]);

computer_input = random.randint(1, 3);
print(all[computer_input - 1]);

if user_input == computer_input: 
  print('Tie');
elif user_input == 1 and computer_input == 2:
  print("You lost!");
elif user_input == 1 and computer_input == 3:
  print("You won!");
elif user_input == 2 and computer_input == 1:
  print("You won!");
elif user_input == 2 and computer_input == 3:
  print("You lost!");
elif user_input == 3 and computer_input == 1:
  print("You lost!");
else:
  print("You won!");

# ============= List=============
print("")
print(" ====== List ======")

print("")
print(" -- Nested List ---")
fruits = ["Apple", "Pear", "Orange"]
vegetables = ["Tomatoes", "Kale", "Spinach", "Celery"]

sum = [fruits, vegetables]

# IMPORTANT!!!!!!!!!!!!!!!!! : We can cast the list to str!!!
print("sum: " + str(sum))  # [["Apple", "Pear", "Orange"], ["Tomatoes", "Kale", "Spinach", "Celery"]]

# [IMPORTANT]
# Like javascript the type can be mixed up in the List.

stringData = ["New York", "Colorado", "New Jersey"]
print(stringData[0])  # Same as in Javascript

# Negative index
print("")
print(" -- Negative Index ---")
print(stringData[-1])  # New Jersey
print(stringData[-2])  # Colorado
print(stringData[-3])  # New York

# Assign Value
print("")
print(" -- Assign Value ---")
stringData[0] = "Nebraska"
print(stringData)

# Add Value(s) in order (push in javascript)
print("")
print(" -- Add a single value ---")
stringData.append("South Carolina")
stringData.append(1)
print(stringData)

print("")
print(" -- Add a bunch of values ---")
stringData.extend([2, 3, 4])
print(stringData)

print("")
print(" -- Split string ---")
greetings = "Hello, from AskPython".split(", ");
print(greetings)

# Assignment
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random;

last_index = len(names) - 1;
# 2)
chooseIndex = random.randint(0, last_index);
print(f"{names[chooseIndex]} is going to buy the meal today!");
# 1)
choices = random.choice(names);
print(choices + " is going to buy the meal today!");


# ======== Randomization (psuedo random generator) ========
# Python uses 'Mersenne Twister' to generate psudo random number.

# [IMPORTANT]: "askpython.com"
# "askpython.com" and in the search bar, enter "random module".
#  ==> It will show us Python random Module.
print("")
print(" ====== Randomization ======")

# module means the component or lib that are same as javascript.

# [Custom module]
# importing another module created by myself
import my_module

print(my_module.pi)

# [API module]
# importing random module created by the Python team.
import random

# 1) Generating random integer
# - Generating integer between 1 to 10 (inclusive)
random_integer = random.randint(1, 5)
print(random_integer)

# 2) Generateing floating point number
random_float = random.random()
# generates the point number between 0 to 1 (exclusive)
print(random_float)

# 3) Generating floating point number between 0 to 5
print(random_float * 5)
# 1 * 5 = 5. Therefore it can't be 5 because `random_float` can't be 0 or 1.

# FYI
love_score = random.randint(1, 100)
print(f"Your love score {love_score}.")

# [ ------------------------ Day3 ----------------------------------- ]
# ======== Treasure Island ========
# ''' ''': allows the line chnage.
print("")
print(''' 
==== 
Treasure Island
====
''')

left_right = (input("left or right? ")).lower()

if left_right != "left":
    print("Fall into a hole. Game Over.")
else:
    swim_wait = (input("swim or wait? ")).lower()

    if swim_wait != "wait":
        print("Attacked by trout. Game Over.")
    else:
        door = (input("Which door?")).lower()

        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You win!")
        else:
            print("Game Over")

# ======== Love Cal ===============
print("")
print("======= Love Calculator =======")
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = (name1 + name2).lower()
trueCount = name.count("t") + name.count("r") + name.count("u") + name.count(
    "e")
loveCount = name.count("l") + name.count("o") + name.count("v") + name.count(
    "e")
length = int(str(trueCount) + str(loveCount))
prefix = f"Your score is {length}"

if length < 10 or length > 90:
    print(prefix + ", you go together like coke and mentos.")
# must 40 ahead of 50!!!
elif length >= 40 and length <= 50:
    print(prefix + ", you are alright together.")
else:
    print(prefix + ".")

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
    # which means if it satisfies the upper line's "if statement", it automatically breakes.
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
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
num_persons = int(input("How many people to split the bill? "))
pay_per_person = (total_bill * (1 + tip_percent / 100)) / num_persons

# [IMPORTANT] 2) set two digit number with `format`
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${pay_per_person}")

# [IMPORTANT] 1) set two digit number with `round`. It only works whent the digit nubmer like 23.32323232.
# two decimal number does not always work in terms of even 00, 50 etc.
# In this case, it print like 22 or 22.5 (not 22.00 or 22.50)
# print(f"Each person should pay: ${round(pay_per_person, 2)}")

# ======== Mathmatical operator ====
print("======== Number Manipulation ===========")
# [IMPORTANT] Automatically float type
print(8 / 3)  # 2.6666666666666

# [IMPORTANT] 2 because it chops off the decimal numbers without any rounding!
print(int(8 / 3))

# [IMPORTANT!!!!] because of rounding, it automatically integer
print(round(8 / 3))

# 2.67 because 2 is the number of decimal numbers
print(round(8 / 3, 2))

# [IMPORTANT!!!!] directly converting float to integer
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
print(
    f"Your score is {score}, your height is {height}, and your are winning is {isWinning}"
)  # Same thing in Java and javascript

print("======== Math operator ===========")
3 + 5
7 - 4
3 * 2
6 / 3
6 % 2
print(6 / 3)  # [IMPORTANT!!!!] it always returns float type! -> 2.0

# [IMPORTANT]: exponent! to increase power
exp = 2**3  # 8
print(exp)  # 8

# PEMDAS (Prioirty) with LR (left to right)
# ()
# **
# * / (always left one first)
# + - (always left one first)

print(3 / 3 + 3 * 3 -
      3)  # / * have the same priority so that left one "/" first. --> 7.0

#  ======= Data Types: String (str), Integer (int), Float (float), Bloean (bool) ===
print("======== Data type ===========")
# 1) String
print("Hello"[0])
print("Hello"[4])
print("123" + "456")

# 2) Integer
print(123 + 456)
# [JUST REMIND] for large number, we can use "_" intead of ","
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
print(
    a + bb
)  # [IMPORTANT!!!!!] int + float = float. 246.0 because is float has more comprehensive scope

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
