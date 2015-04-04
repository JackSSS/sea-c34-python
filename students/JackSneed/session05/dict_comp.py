def problem1():
    """Print a dict by passing it with a string format method"""

    food_prefs = {u"name": u"Jack",
                  u"city": u"Richmond",
                  u"cake": u"chocolate",
                  u"fruit": u"plum",
                  u"salad": u"arugula",
                  u"pasta": u"linguini"}

    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, \
          {salad} salad, and {pasta} pasta".format(**food_prefs))

problem1()


def problem2():
    """
    Using a list comprehension, build a dictionary of numbers
    from zero to fifteen and the hexadecimal equivalent.

    """

    numbers = range(0, 16)
    result = dict(zip(numbers, [hex(hexadecimal) for hexadecimal in numbers]))
    print(result)

problem2()


def problem3():
    """
    Do the previous entirely with a dict
    comprehension – should be a one-liner.

    """

    print({numbers : hex(numbers) for numbers in range(0, 16)})

problem3()


def problem4():
    """
    Using the dictionary from item 1: Make a dictionary using the same
    keys but with the number of ‘a’s in each value.

    """

    food_prefs = {u"name": u"Jack",
                  u"city": u"Richmond",
                  u"cake": u"chocolate",
                  u"fruit": u"plum",
                  u"salad": u"arugula",
                  u"pasta": u"linguini"}

    print({a : number.count("a") for a, number in food_prefs.items()})

problem4()


def problem5():
    """
    Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    divisible 2, 3 and 4.

    """

    s2 = set(range(0, 21)[::2])
    s3 = set(range(0, 21)[::3])
    s4 = set(range(0, 21)[::4])
    print(s2)
    print(s3)
    print(s4)

problem5()
