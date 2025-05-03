"""Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""

# numbers = []
# for number in range(2000, 3201):
#     if (number % 7 == 0) and (number % 5 != 0):
#         numbers.append(str(number))

# print(','.join(numbers))


"""Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)

number = int(input('pick a number'))
print(fact(number))