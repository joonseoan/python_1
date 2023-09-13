print("")
print("====================== Day 13 =================")
print("")

print("")
print("------- Debugging --------")
print("")

############DEBUGGING#####################

# Describe Problem
# def my_function():
#     for i in range(1, 21):
#         # i cannot be 20
#         if i == 20:
#             print("You got it")

# my_function()

# Reproduce the Bug
# from random import randint

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # Because it is random. The previous 1, 6 is out of range.
# # because 6 is inclusive
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer. When we enter 1994 as an input, nothing printed
# We skept 1994 in range.
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# Fix the Errors
# 1) Indentation Error
# 2) Omitted f script
# age = int(input("How old are you?"))

# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # == means word_per_page is still 0
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# #Use a Debugger: we can use phython tutor
# https://pythontutor.com/python-debugger.html#mode=edit
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)

    # [IMPORTANT!]
    # b_list.append(new_item) // its output is [26] because python does not have a scope

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


print("")
print("====================== Day 12 =================")
print("")

print("")
print("------- Challenge --------")
print("")

# https://replit.com/@JoonAn1/guess-the-number-start
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# text art site : http://patorjk.com/software/taag/#p=display&f=Basic&t=Guess%20the%20Number

from random import randint
# from logo import art_logo

# ---------------- Teacher solution ------------------
# EASY_LEVEL_ATTEMPS = 10
# HARD_LEVEL_ATTEMPS = 5


# def getAttemps():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")

#     if level == 'easy':
#         turns = EASY_LEVEL_ATTEMPS
#     else:
#         turns = HARD_LEVEL_ATTEMPS

#     return turns


# def check_answer(answer, guess, turns):
#     """checks answer against guess. Returns the number of turns retmaining"""
#     if guess > answer:
#         print("Too High")
#         return turns - 1
#     elif guess < answer:
#         print("Too Low")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {answer}")


# def game():
#     # including both 1, 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I am thinking of a number between 1 and 100")
#     answer = randint(1, 100)
#     print(f"anser: {answer}")

#     turns = getAttemps()

#     # Please make sure!!!
#     # while loop is able to control global variable!
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attemps remaining to guess the number")
#         # In while loop, we can change the global variable
#         guess = int(input("Make a guess: "))
#         # Update turns
#         turns = check_answer(answer, guess, turns)

#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             break  # or return
#         elif guess != answer:
#             print("Guess again.")


# game()

# ---------------- My Sloution ------------------

# print(art_logo)
print("Welcome to 'Guess the Number' game!")
print("I'am thinking of a number between 1 and 100.")
selected_number = randint(1, 100)
user_guess = 0

game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if game_difficulty == "easy":
    number_of_chances = 10
else:
    number_of_chances = 5


def play_number(user_guess):
    if user_guess > selected_number or user_guess < selected_number:
        if user_guess > selected_number:
            print("Too high")
        else:
            print("Too low")
    else:
        print("You got it!")
        print(f"The selected number is {selected_number}")

while user_guess != selected_number:
    print(
        f"You have {number_of_chances} attempts remaiing to guess the number")

    user_guess = int(input("Make a guess: "))
    play_number(user_guess)
    
    number_of_chances -= 1

    if number_of_chances == 0:
        print("You've run out of guesses, you lose.")
        print(f"The selected number is {selected_number}")
        break
    elif user_guess != selected_number:
        print("Guess again!")


print("")
print("------- Constant --------")
print("")

# Naming convention
PI = 3.14159
URL = 'http://www.python.ca'
TWITTER_HANDLE = "@yu_angela"



print("")
print("------- Scope 2 --------")
print("")

enemies2 = 1
enemies3 = 1

# [IMPORTANT!] Better example. Use the `return!`
def increase_enemies3():
    return enemies3 + 1

enemies3 = increase_enemies3()
print(f"global enemies3 inside function: {enemies3}")


# An example of modifying the global variable within function
# [IMPORTANT]!!!
# However, if we use this global variable modification, it will be confusing us. Therefore, we should minimize the modification
def increase_enemies2():
    # [IMPORATNT]
    # How can we handle this?
    # enemies2 = 0; # Must define to use "+="
    # enemies2 += 2 # Without the new variable declarlation within the function scope, it will generate an error. How should we handle this to increase the value for global `enemies2`?

    # In order to tap into the global variable and then change it,
    # we actually have to explicitly say that we have a global variable
    # that is defined somewhere outside of this function.
    global enemies2

    # [IMPORATANT!!!] for the global variable, not defined in upside,
    # the kind of hoisting DOES NOT works
    # The global variable should be defined upside first
    # global enemies
    # print(f"global variable enemies not in defined {enemies}")

    enemies2 += 1
    
    # [IMPORATNT] It generates the undefined nameErrors the a
    # enemies += 2

    print(f"global enemies2 inside function: {enemies2}") # 2 now

    # [IMPORTANT] 
    # print(f"global enemies inside function {enemies}")


increase_enemies2()
print(f"global enemies2 outside function: {enemies2}")

# [IMPORTANT] Not working because it is the same global scope!!
# print(f"global enemies1 outside function: {enemies1}")


print("")
print("------- Scope 1 --------")
print("")

enemies = 1


# Example that I am confused with in Python
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")  # 2


increase_enemies()
print(f"enemies outside function: {enemies}")  # Still 1


# ---- Local Scope ----
# The local scope exists within functions!
def drink_potion():
    # This variable is only accessible inside of this function
    potion_strength = 2
    print('potion_strength', potion_strength)


drink_potion()
# print(potion_strength)  # Error: 'NameError': name 'potion_strength' is not defined

# --- Global Scope ----
# The only difference between Local scope and Global scope is where we define or
# where we create variables

player_health = 10


def drink_potion2():
    potion_strength = 2
    # It can access to Global Scope `player_health`
    print('player_health inside: ', player_health)


# [IMPORTANT!!!]: it works fine before function call.
# player_health = 10

drink_potion2()
# player_health = 10 # Generate Error

print('player_health outside: ', player_health)

# --- This concept of global and local scope does not apply to variables. It applies to functions and anything else we name. This concept called `Namespace` ---

# For instance, `drink_potion`, `player_health`, `potion_strength`, and etc...any thing we give name to ahs a namespace and that name space is valid in certain scope.


def play():

    def drink_potion3():
        potion_strength = 2
        # It can still access to Global Scope `player_health`
        print('player_health inside: ', player_health)


# We can't call the nested function because each namespace has valid scope.
# drink_potion3()

# --- There is no block scope in Python ---
# What this means is that if we were to create an if statement, for, while and etc.

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

# Important!!
# We can still access to `new_enemy` created in if statement block
print("new_enemy: ", new_enemy)


def create_enemy():
    if game_level < 5:
        new_enemy_2 = enemies[0]


# [IMPORTANT!]
# Now it does not work because the variable inside function becomes the local scope
# print("new_enemy_2: ", new_enemy_2)

print("")
print("====================== Day 11 =================")
print("")

print("")
print("------- Capstone 1: Simple Blackjack --------")
print("")

# project site
# https://replit.com/@JoonAn1/blackjack-start#main.py

# ----------------------- Teacher Solution --------------------------
import random
# from replit import clear
# from art import logo

def deal_card():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Oponent Went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # [Important]: With one argument, it `stop` argument from 0
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        """ Receive the current cards and return the calculated score"""
        # Better way but need to learn "in"
        # if sum(cards) == 21 and len(cards) == 2:
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            # IMPORTANT: we can remove the element by using element value
            # IMPORTANT!!!!!: manipulate the outside variable with utilizing the parameters
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get anohter card, type 'n' to pass: ")
            if user_should_deal.lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # After while loop above
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    your final hands: {user_cards}, and final score: {user_score}")
    print(
        f"    computer final hands: {computer_cards}, and final score: {computer_score}"
    )

    # A big question. How can we call user_score and computer_score defined in another while loop above?
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Enter 'y' or 'no': "
            ).lower() == "y":
    # clear()
    # print(logo)
    play_blackjack()

# ---------------- My solution ---------------------
# import art
import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# [IMPORTANT!!!!!!!!]
# Should not be used
# because in python, it is  always these values even after manipulation
# in the function.
# user_cards = []
# user_cards_sum = 0
# computer_cards = []
# computer_cards_sum = 0

repeat = True


def get_cards_sum(current_cards):
    hasEleven = False
    indexFound = 0
    manual_sum = 0

    # In python, len should not add "-1"
    for index in range(0, len(current_cards)):
        if current_cards[index] == 11:
            hasEleven = True
            indexFound = index
            continue
        else:
            manual_sum += current_cards[index]

    if hasEleven == True and (manual_sum + 11) > 21:
        current_cards[indexFound] = 1

    return {"current_cards": current_cards, "sum": sum(current_cards)}


def print_current_cards(_user_cards, _user_cards_sum, _computer_cards):
    print(f"    Your cards: {_user_cards}, current score: {_user_cards_sum}")
    print(f"    Computer's first card: {_computer_cards[0]}")


def play_computer_cards(_computer_cards, _computer_cards_sum):
    if _computer_cards_sum < 17:
        _computer_cards.append(random.choice(cards))
        _computer_cards_sum = get_cards_sum(_computer_cards)

        return play_computer_cards(_computer_cards_sum["current_cards"],
                                   _computer_cards_sum["sum"])
    else:
        # It can be an list
        return {
            "final_computer_cards": _computer_cards,
            "final_computer_cards_sum": _computer_cards_sum,
        }


def do_user_black_jack(
    _user_cards,
    _user_cards_sum,
    _computer_cards,
    _computer_cards_sum,
):

    final_computer_result = {}

    continue_question = input(
        "Type 'y' to get another card, type 'n' to pass: ").lower()

    if continue_question == "n":
        final_computer_result = play_computer_cards(_computer_cards,
                                                    _computer_cards_sum)

        return {
            "user_final_cards":
            _user_cards,
            "user_final_sum":
            _user_cards_sum,
            "computer_final_cards":
            final_computer_result["final_computer_cards"],
            "computer_final_sum":
            final_computer_result["final_computer_cards_sum"],
        }
    else:
        _user_cards.append(random.choice(cards))
        _user_cards_sum = get_cards_sum(_user_cards)
        print_current_cards(_user_cards_sum["current_cards"],
                            _user_cards_sum["sum"], _computer_cards)

        if _user_cards_sum["sum"] <= 21:
            return do_user_black_jack(_user_cards_sum["current_cards"],
                                      _user_cards_sum["sum"], _computer_cards,
                                      _computer_cards_sum)

        elif _user_cards_sum["sum"] > 21:
            final_computer_result = play_computer_cards(
                _computer_cards, _computer_cards_sum)

            return {
                "user_final_cards":
                _user_cards_sum["current_cards"],
                "user_final_sum":
                _user_cards_sum["sum"],
                "computer_final_cards":
                final_computer_result["final_computer_cards"],
                "computer_final_sum":
                final_computer_result["final_computer_cards_sum"],
            }


def compare(result):
    user_final_cards = result["user_final_cards"]
    user_final_sum = result["user_final_sum"]
    computer_final_cards = result["computer_final_cards"]
    computer_final_sum = result["computer_final_sum"]

    print(
        f"    Your final hand: {user_final_cards}, final score: {user_final_sum}"
    )
    print(
        f"    Computer's final hand: {computer_final_cards}, final score: {computer_final_sum}"
    )

    if user_final_sum > 21:
        print("You lose")
    elif user_final_sum == 21:
        if computer_final_sum == 21:
            print("You draw")
        else:
            print("You win")
    else:
        if computer_final_sum > 21:
            print("You win")
        elif computer_final_sum == 21:
            print("You lose")
        else:
            user_diff = 21 - user_final_sum
            computer_diff = 21 - computer_final_sum

            if user_diff > computer_diff:
                print("You lose")
            elif user_diff == computer_diff:
                print("You draw")
            else:
                print("You win")


def init_blackjack():
    system('clear')
    # print(art.logo)

    _user_cards = random.sample(cards, 2)
    _user_cards_sum = get_cards_sum(_user_cards)
    _computer_cards = random.sample(cards, 2)
    _computer_cards_sum = get_cards_sum(_computer_cards)

    print_current_cards(_user_cards_sum["current_cards"],
                        _user_cards_sum["sum"],
                        _computer_cards_sum["current_cards"])

    return {
        "User_Cards": _user_cards_sum["current_cards"],
        "User_Cards_Sum": _user_cards_sum["sum"],
        "Computer_Cards": _computer_cards_sum["current_cards"],
        "Computer_Cards_Sum": _computer_cards_sum["sum"],
    }


while (repeat):
    repeat_question = input(
        "Do you want to play a balckjack? type 'y' for yes, or 'n' for no. "
    ).lower()

    if repeat_question == "n":
        repeat = False
        print("BYE!!!!!")
    else:
        initial_values = init_blackjack()

        if initial_values["User_Cards_Sum"] == 21 or initial_values[
                "Computer_Cards_Sum"] == 21:
            compare(initial_values)
        else:
            result = do_user_black_jack(initial_values["User_Cards"],
                                        initial_values["User_Cards_Sum"],
                                        initial_values["Computer_Cards"],
                                        initial_values["Computer_Cards_Sum"])
            compare(result)

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.




print("")
print("====================== Day 10 =================")
print("")

print("")
print("------- Challenge --------")
print("")

# Full web site: https://replit.com/@JoonAn1/calculator-start#main.py

def add(a, b):
    return a + b

def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    result_number = float(input("Please enter the first number: "))
    repeat = True

    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide,
    }

    while repeat:
        for operator_symbol in operations:
            print(operator_symbol)

        operator = input("Please enter an operator: ")
        following_number = float(input("Please enter the following number: "))
        result_number = operations[operator](result_number, following_number)
        print(f"The result is {result_number}")

        # Continue from the current result number
        repeat_ask = input("y: calculate with the current result\n" +
                           "r: calculate from the scratch\n" +
                           "n: exit\n").lower()

        if repeat_ask == "r":
            # Should False because the current calculator() call is still True.
            # Otherwise it will repeat again when the user enters "n"
            repeat = False
            calculator()
        elif repeat_ask == "n":
            repeat = False


calculator()

print("")
print("------- Docstrings --------")
print("")
'''
Docstrings is to create a documentation as we are coding along in our
functions or in our other blocks of code. [Important] when we hover in the function call, Docstring will show up as tool tips
'''

def format_name_2(f_name, l_name):
    # Docstrings
    """
     Take a first and last name and format it to return the title
     case version of name.
    """
    if f_name == "" or l_name == "":
        return

    return f"{f_name} {l_name}".title()


print(
    format_name_2(input("What is your first name? "),
                  input("What is your last name? ")))

print("")
print("------- Function ouptput --------")
print("")

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year.")
        return True
      else:
        # print("Not leap year.")
        return False
    else:
    #   print("Leap year.")
      return True
  else:
    # print("Not leap year.")
    return False

def days_in_month(year, month):
  if year < 0:
    return
  
  if month > 12 or month < 1:
    return

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap(year):
      month_days[1] = 29

  return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return  # return "None" means that it returns nothing

    # [Important]
    # Capitalize Strings "title()"
    # f_name.title()
    # l_name.title()
    return f"{f_name} {l_name}".title()


print(
    format_name(input("What is your first name? "),
                input("What is your last name? ")))
# print(format_name("Angela", "fdafaf"))

print("")
print("====================== Day9 =================")
print("")

# [IMPORTANT!!! Please review!!!]
# Print List for loop: https://developers.google.com/edu/python/lists#range
# Print List: https://docs.python.org/3/tutorial/datastructures.html

print("")
print("------- Final Challenge --------")
print("")

# https://replit.com/@JoonAn1/blind-auction-start#main.py

print("")
print("------- Nesting Dictionaries --------")
print("")
"""
{
    "Key1": {}, # Dictionary
    "Key2": [], # List
}
"""

# Nesting List in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a dictionary
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a list
travel_log3 = [{
    "countries": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
}, {
    "countries": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 33,
}]

def add_new_country(country, visits, cities):
    new_element = {}
    new_element["country"] = country
    new_element["visits"] = visits
    new_element["cities"] = cities

    # new_element = {
    #     "country": country,
    #     "visits": visits,
    #     "cities": cities,
    # }

    travel_log.append(new_element)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)

print("")
print("------- Python Dictionaries --------")
print("")

# It is a kind of object in java or javascript
# Dictionary is useful because they allow us to group together and tag related
# pieces of information.

# The dictionary has key and value => {key: value}
# The key should be capitalized and used with "".

# example:
# { "Bug": "An error in a program that prevents the program ...",
#   "Function": "A piece of code that we can easily call ... ",
#   "Loop": "The action of ..."
# }

programming_dictionary = {
    "Bug": "An error in a program that prevents the program ...",
    "Function": "A piece of code that we can easily call ... ",
    "Loop": "The action of ...",
    123: "number key works!",
}

# print all
print(programming_dictionary)
# print a property.
print(programming_dictionary["Bug"])

# [IMPORTANT!!!] => number key works.
print(programming_dictionary[123])  # Then it points the same memory location.

## Adding a property into a dictionary
programming_dictionary["Symbol"] = "Python has symbol?"
print(programming_dictionary)

## edit value (overriding)
programming_dictionary["Bug"] = "Bug is a bug"  # Object Mutability
print(programming_dictionary)

## create empty dictionary
empty_dictionary = {}
empty_dictionary[0] = "The first element"
print(empty_dictionary)

## make empty dictionary
programming_dictionary = {}  # Fully different dictionary from the one above!!!
print(programming_dictionary)

# Loop through a dictionary
programming_dictionary["Bug"] = "A moth in computer"
programming_dictionary["Babry"] = "A cute people"
programming_dictionary["House"] = "A space to live"

# Same as javascript
for key in programming_dictionary:
    print(key, ":", programming_dictionary[key])

#### Coding Challenge ######
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    grade = ""

    if score > 90:
      grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)
# ======================= Day 8 ==============================
print("====================== Day8 =================")

print("")
print("------- Chellnge - Cyphering and Decyphering final --------")
print("")

# import there so can't add into this component.
# https://replit.com/@JoonAn1/caesar-cipher-4-start#main.py

print("")
print("------- Chellnge - Cyphering and Decyphering part 2 (Refactoring) --------")
print("")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_amount, input_direction):
    result = ""

    if input_direction == "decode":
        shift_amount *= -1

    for letter in input_text:
        index = alphabet.index(letter)
             
        result += alphabet[index + shift_amount]

    print(f"The {input_direction}d text is {result}")

caesar(input_text=text, shift_amount=shift, input_direction=direction)

print("")
print("------- Chellnge - Cyphering and Decyphering part 1 (encode and decode) --------")
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

def decrypt(plain_text, shift_amount):
    decrypted_text = ""

    for letter in plain_text:
        new_index = alphabet.index(letter) - shift_amount
        # We do not need any alphabet reorganization like `encrypt`
        decrypted_text += alphabet[new_index]
    print(decrypted_text)

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
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(plain_text=text, shift_amount=shift)

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
