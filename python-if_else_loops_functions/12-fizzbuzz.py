#!/usr/bin/python3
def fizzbuzz():
    """
    Prints numbers from 1 to 100 separated by a space.
    Multiples of 3 are replaced with 'Fizz', multiples of 5 with 'Buzz',
    multiples of both 3 and 5 with 'FizzBuzz'.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
