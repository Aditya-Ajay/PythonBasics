import sys
# input (): This function first takes the input from the user and converts it
# into a string. The type of the returned object always will be <type ‘str’>.
#  It does not evaluate the expression it just returns the complete statement as
#  String. For example, Python provides a built-in function called input which takes
#  the input from the user. When the input function is called it stops the program and
#  waits for the user’s input. When the user presses enter, the program resumes and
#  returns what the user typed.

a = int(input("Name : "))
print(a)
print(type(a))

print("HELLO")


# \n ---> newline  ---> It causes a line break
name = input('What is your name?\n')
print(name)

# The text or message displayed on the output screen to ask a user to enter an input
#  value is optional i.e. the prompt, which will be printed on the screen is optional.
# Whatever you enter as input, the input function converts it into a string. if you
# enter an integer value still input() function converts it into a string. You need to
# explicitly convert it into an integer in your code using typecasting.


num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# # Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))


# To Print a statement without a line break .
sys.stdout.write('hello  ')
sys.stdout.write('Bye ')


#    Python formatting
# -------------------------

print("hello", "bro", "hi", "bye", sep="-",  end="@")
