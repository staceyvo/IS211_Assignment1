#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check if numbers in a list are divisible by another value."""

def listDivide(numbers, divide=2):
    #take a list and divide each number by divide
    #find values with no remainder

    """Return numbers that are evenly divisible by divide.

            Args:
                numbers is a list
                divide is used to divide numbers


            Returns:
                Returns a number if it is divisible evenly.


            Examples:
                listDivide([5, 8, 6, 4, 9], 3):
                2

                listDivide([18, 23, 100, 6, 22], 8):
                0

            """

    count = 0

    for x in numbers:
        if x%divide==0:
            count += 1
    return count

class ListDivideException(Exception):
    pass

def testListDivide():
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException
    if listDivide([]) != 0:
        raise ListDivideException
    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

if __name__ == '__main__':
     testListDivide()