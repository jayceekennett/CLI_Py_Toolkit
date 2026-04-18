# input_handler_usage.py

from input_handler import InputHandler

# ---------------------------- EXAMPLE USAGE ----------------------------------

# function examples for command map
# ---------- basic command 
def print_words():
    print("Printed test command!")

# ---------- example of lambda use
x = 3
def double_value(x):
    print(3*2)
    
# ---------- create command map
command_map = {":print_words" : print_words,
               ":double_three" : lambda: double_value(x)}

# ---------- initialise class
ih = InputHandler(command_map)

# ---------- run conditional accept
colour_choice = ih.conditional_accept(["blue", "red"], prompt = "Enter blue or red: ")

'''
Examples:
> Enter blue or red: green
Possible options are:
  blue
  red

> Enter blue or red: blue
blue


> Enter blue or red: :false command
[system message: invalid command, try again]

> Enter blue or red: :print_words
Printed test command!


> Enter blue or red: :double_three
6

'''

# ---------- run conditional type
int_required = ih.conditional_type("int", prompt = "Enter an integer: ")

'''
Examples
> Enter an integer: string
[system message: input of type int required, please try again]

> Enter an integer: 1
1


> Enter an integer: :print_words
Printed test command!

'''




