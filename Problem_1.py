#-------------------------------------------------
#                  Zack Snoen
#              ZackSnoen@gmail.com
# Copyright 2022, Zack Snoen, All rights reserved.
#-------------------------------------------------

# Problem 1 description
#--------------------------------------------------------------------------
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#--------------------------------------------------------------------------

# Brute force solution hacked together in minutes
# Takes two numbers to find multiples of below integer max
# Returns the sum of all those multiples
def quickSolution(multOne, multTwo, max):

    # Assign iterator and sum variables
    i = 1
    sum = 0

    # Loop through all ints one to max
    # Check if that int is a multiple of 3 or 5 and adds to sum if so
    for i in range(1, max):
        if i % multOne == 0:
            sum += i
        elif i % multTwo == 0:
            sum += i

    return sum

# Let's make it more efficient
# Rather than looping through all integers 1-max, we only check multiples of the two given ints
# 
def alrightSolution(multOne, multTwo, max):

    # Assign iterators and sum variables
    multOneIter = multOne
    multTwoIter = multTwo
    sum = 0

    # Add all multiples from 1-max of 1st input in O(max/multOne) time
    while (multOneIter < max):
        sum += multOneIter
        multOneIter += multOne

    # Add all multiples from 1-max of 2nd input in O(max/multTwo) time
    while (multTwoIter < max):

        # Excludes adding common multiples of 1st and 2nd inputs since they were already added
        if multTwoIter % multOne != 0:
            sum += multTwoIter
        multTwoIter += multTwo
    
    return sum

# I still see room to improve
# Lets try some math
# n has max/n multiples in range(1, max)
# summing range(1, max/n) * 3 would give you sum of all multiples n in range(1, max)
# can do the same for 2nd input
# Now we would just need to subtract all common multiples of the 2 numbers
# If we can get the lowest common multiple we can get the set of common multiples to subtract from
#def solution(multOne, multTwo, max):


if __name__ == "__main__":
    print(quickSolution(3, 5, 1000))
    print(alrightSolution(3, 5, 1000))
    