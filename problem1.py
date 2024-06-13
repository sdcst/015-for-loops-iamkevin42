#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""

height=int(input("Enter the height of the box\n"))
width=int(input("Enter the width of the box\n"))

if height > 10:
    print('Too number must be 10 or under')
elif height <= 0:
    print('Too small, Number must be 1 or higher')


if width > 10:
    print('Too big')
elif width <=0:
    print("Too small")

for i in range(height):
    print("*" * width)
    



