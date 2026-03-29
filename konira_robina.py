# Name: Konira Robina
# Course: Certificate in Software Engineering with Python
# Assignment: Python Terminologies

# 1. Computer programming
# computer programing is telling a computer what to do using instructions.
# it is like giving a recipe for food or instructions on how a particular food can be cooked. If the instructions are clear, the food comes out right
#example:
print("Konra") 
"""
this statement tells the computer to display/show the message "konra" on the screen.
it shows how programming is giving instructions to the computer.
"""

# 2. memory partitioning
# memory partitioning means dividing memory into sections/parts.
# it is like dividing a cupboard into shelves where each part stores different items like a part for cups only, another one for only plates and so on.
# example:
a = 10
b = 20
"""
the computer stores 10 and 20 in diffferent memory locations
this shows how memory is divided so each variable has its own spaces.
"""

# 3. memory address
# memory address is the exact location where data/information is stored.
# it is like a house address that helps you find a specific home among many houses
# example 
x = 5
print(id(x))
"""
the variable x stores the values 5
the id(x) shows the memory address where 5 is stored. id means address
this proves that every value has a unique location in memory.
"""

# 4. how RAM connects the CPU and the hard disk
# first of all, let us define what a RAM and a CPU is.
# RAM is ramdom access memory and it a short-term memory which means it stores information temporaly.
# CPU is central processing unit and it is like tha brain of a computer and therefore, it controls the computer.
# let us now see how the RAM connects the CPU and the hard disk.
# RAM helps the CPU quickly access or get data/ information from the hard disk.
# the hard disk is like a store , RAM is like the basket used for collecting and carring items from the store and the CPU is like you.
# u do not carry the whole store, u pick what you need into the basket.
#example
name = "konra"
print(name)
# this data is loaded into RAM when the program runs 
print(name)
"""
# the CPU reads it from RAM and displays it.
# when this program runs, it is first taken from the hard disk to RAM 
# the CPU then uses RAM to quicking read the values "konra" and print it.
"""

# 5. what is avariable
# a varaible is a name used to store data.
# it is like labeling containers for example the one having sugar labeled as sugar and the one having salt labeled as salt
container = sugar
print(container)
"""
the variable container stores sugar
when we print it,the computer displays "sugar"
this shows how variables store and use data.
"""

# 6. what is a statement
# a statement is a single complete instruction.
# it is like one command for eaxample "sit down" 
# example
print("python terminologies")
"""
this is one instruction telling the computer to display or show text
it is a single statement because it performs one action
"""

# 7. what is a code
# code is a set of instructions written together.
# two or more statements make up a code.
# it is like a full food recipe that is to say for eaxample in order to cook a particular food, there are steps that you need to follow.
# example:
x = 1
y= 2
print("x+y")
"""
this is a group of instructions(code)
first, values are stored in x and y, then they are added and printed.
it shows how multiple or many statements work together
"""

# 8. what is a block of code
# a block of code is a group of statements that work together
"""
two or more related statements make up a block of code.
group of statements that are related.
"""
# example
if True:
    print("line 1")
    print("line 2")
"""
the two lines form a block of code 
they run together when the condition is true.
this shows how Python groups relate instructions     
"""

# 9. list any four syntax of variables
# syntax is the correct way of writting code
# if the syntax is wrong, the program will not run
# syntax is like grammer in English or the rules that tell us about how English should be spoken or written correctly.
# syntax for variables is the rules used to create and assign values to variables.
# rules of variables and examples

# rule 1
# a variable must start with a letter or underscore(_)
name = "Robina"
_age = 21
# these are correct because they start with a letter or underscore(_)

# rule 2
# a variable can not have spaces.
#  In Python, a variable name cannot have spaces because the interpreter uses spaces to separate different parts of code, such as keywords and variable names. A space inside a variable name (e.g. my name) confuses Python, causing it to treat it as two separate, invalid/ non existing statements rather than one single label. 
my_name = "Janet"
# underscore(_) is used instead of space.

# rule 3
# a variable can contain letters, numbers and underscores
name1 = "Irene"
my_age = "19"
# these values are valid because they follow naming rules

# rule 4
# avoid using capital letters while writing varaiable names eg NAME, AGE, instead, use small leters for example name, age etc.

# extra examples of syntax variables
x = 5
# a variable x is assigned the value 5
name = "Robina"
# a variable name stores text
a,b = 1,2
# two variables are assigned values at the same time.
x=y=10
# two variables share the same value.

# 10. what is declaring
# declaring means creating a variable.
# the process of creating a variable is called declaring.
# example
score = 100
print(score)
"""
the variable score is created and given the value 100
printing it shows the value
this desmonstrates declaring and assigning a variable
"""

# 11. initialising
# is the process of giving a name to a variable.
# it means giving a variable its first value when u create it
# it is like assigning a starting value to a variable.
# for example when you buy a brand new phone and then you start setting it up for the first time, that is initialising.
# example
score = 0
# the variable score is initialised with 0.
