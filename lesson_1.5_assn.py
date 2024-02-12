## Task 1 Original Code ##

''' 
weather = "sunny"

if weather == "sunny":
print("Wear sunglasses!")
else:
print("Take an umbrella!")
'''

## Corrected Code ##

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!") #needed indent
else:
    print("Take an umbrella!") #needed indent

## Task 2 Code ##
    
user_input = ["happy", "sad"] # Using a list to note binary options. 

user_input[0] #Example for input happy
if user_input[0]:
    print("That's great to hear!")
if user_input[1]:
    print("I hope your day gets better!")

user_input[1] #Example for input sad.
if user_input[0]:
    print("That's great to hear!")
if user_input[1]:
    print("I hope your day gets better!")

## Task 3 Original Code ##

''' 
mood = "excited"

#if mood == "excited":
    print("Yay! Let's have fun.")
   else:
print("Let's find something fun to do!")
'''
    
## Task 3 Correted Code ##
    
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

## Task 1 Poem ##

# Python will you be my valentine
# Let's get some Java
# And run barefoot in the rain
# My valentine, my only language
# You are better than a taco supreme
    
## Task 2 Multi Line Poem ##

''' 
Oh Python, my Python
hallow be thy name
thy kingdom come
thy world be done
on Earth and in Heavan 
'''

## Task 3 Combo Poem ##

# This is my single line poem
    # Python will you be my valentine
''' This is my multi-line poem
        hallow be thy name
        thy kingdom come
'''

## Task 1 Naming Convention ##

# Corrected Code #

PI_VALUE = 3.14
user_age = 25
user_location = "New York"
MAX_LIMIT = 1000

## Task 1 Data Types ##

variable_a = "Hello, World!" #string
print(type(variable_a))
variable_b = 23 #interger
print(type(variable_b))
variable_c = 3.14 #float
print(type(variable_c))
variable_d = True #bool
print(type(variable_d))

## Task 1 Dynamic Typing ##

dynamic_variable = "This is a string"
print(type(dynamic_variable))
dynamic_variable = 100
print(type(dynamic_variable))
dynamic_variable = 25.5
print(type(dynamic_variable))

## Task 1 Grocery Math ##

cereal = 3
wine = 20 
coffee = 5
total = cereal + wine + coffee
print(total) # = 28

## Task 2 Bank Math ##

savings = 100
interest = 1.02 # 2% interest
annual_gain = savings * interest
print(annual_gain) # = 102

## Task 3 Rectangle Math ##
side1 = 10
side2 = 4
area = side1 * side2
print(area) # = 40
permiter = (side1 * 2) + (side2 *2)
print(permiter) # = 28

## Task 1 Value Swap ##
var1 = 2
var2 = 1
compare = var2 > var1
print(compare) #False

var1 = 1
var2 = 2
compare = var2 > var1
print(compare) #True

## Task 2 Perfect Sq ##

number = 9 # enter number here
exp = number ** .5
print(exp)
if type(exp) == int: 
    print("The number is a perfect square")
else: 
    print("The number in not a perfect square")

## Task 1 Simple Logic Puzzzle ##
    
warm_day = True
cloudy_day = True 
go_outside = warm_day and not cloudy_day
print(go_outside)

## Task 2 Validate Math ##

number1 = 5 * 3 + 2
number2 = 2 + (3 * 5)
check = number1 == number2
print(check)

## Task 3 Mix and Match ##

number3 = 7 
number4 = 6
number5 = number3 + number4
check2 = number5 > 12
if check2 == True:
    print("The check is over budget.") #This shoul be true and should print. 

if number4 < number3 and check2 == True and 5 + 5 == 10: 
    print("success!") # This should print

