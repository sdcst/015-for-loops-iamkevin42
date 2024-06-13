#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

a =int(input("Enter a number smaller than 10: "))
term = 1
series_sum = 0
for i in range(a):
    if a > 10:
        print("This number is bigger than 10. Try again")
        exit()
    elif a < 0:
        print("This number is in the negatives. Try again")
    elif a == "0":
        print("Invalid")

series_sum += term
term = term * 10 + 1  
print(term)

print(f"Sum of the series is {series_sum}")