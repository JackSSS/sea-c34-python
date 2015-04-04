def problem1():

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

    numbers = range(0, 16)
    result = dict(zip(numbers, [hex(hexadecimal) for hexadecimal in numbers]))
    print(result)

problem2()


def problem3():

    print({numbers : hex(numbers) for numbers in range(0, 16)})

problem3()


def problem4():
    """Using the dictionary from item 1: Make a dictionary using the same
    keys but with the number of ‘a’s in each value.
    """

    new_food_prefs = {}
    food_prefs = {u"name": u"Jack",
                  u"city": u"Richmond",
                  u"cake": u"chocolate",
                  u"fruit": u"plum",
                  u"salad": u"arugula",
                  u"pasta": u"linguini"}
    for a, number in food_prefs.items():
        new_food_prefs[a] = number.count("a")
        print(new_food_prefs)

problem4()
