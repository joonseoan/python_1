# Write your code below this line 👇

# ------------------- print function -------------------------

# 0) space (indentation) error
# (space)  print("Hello World!") ===> IndentaionError

# 1) String
print("Hello World!")  # Double quotes
print("Hello World!" + ' in Python')  # Single quote
print("Hello World!" + " in Python")  # + operator
print("Hello World!", " in Python")  # comma ==> another space
print("Hello World!"
      " in Python")  # no space
print("Hello World!"
      ' in Python')  # Single quote

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
input("What is your name?")
print("Hello " + input("What is the programmer name?"))
# Get length of string (It start with index 1, not 0)
# Also must think about the space. The space should be relfected for the start poistion
# of the returned value.
print( len( input("What is your name? ") ) )
