# Now the question arises how to assign the variable

from operator import length_hint


a = 5

name = "Aditya"

# We can also assign multiple values

c, d, e = "A", "B", "C"


# NOW HOW CAN WE SEE THE OUTPUT IN THE TERMINAL  ? Ans- With the help of print command


print(a, name, c, d, e)


# TERNARY OPERATION IN PYTHON . SYNTAX OF TERNARY OPEARTOR

# [on_true] if [expression] else [on_false]

print("Yes") if len(name) == 6 else print("NO")
