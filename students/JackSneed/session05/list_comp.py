def count_evens(nums):
    """
    Using a list comprehension, return the number
    of even ints in the given array.
    """
    return len([even for even in nums if even % 2 == 0])

if __name__ == '__main__':
    print "The number of evens is: {}".format(count_evens([2, 1, 2, 3, 4]))
    print "The number of evens is: {}".format(count_evens([2, 2, 0]))
    print "The number of evens is: {}".format(count_evens([1, 3, 5]))
