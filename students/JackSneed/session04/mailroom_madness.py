#!/usr/bin/env python
"""Using all you’ve learned so far, complete your mailroom program according
to the pseudocode and flow chart you created last session.
-use dicts where appropriate
-see if you can use a dict to switch between the users selections
-Try to use a dict and the .format() method to do the letter as one big
 template – rather than building up a big string in parts.
-For extra fun, see if you can use a file to preserve the donation list and
changes made to it while the program is running.
"""



donors = dict = {u"Rodney Dangerfield": [9000], u"Margret Thatcher": [23000],\
                u"William Shakespeare": [5000], u"Harriet Tubman": [22000]}


def safe_input(key):
    try:
        input_error = raw_input(key)
    except (EOFError, KeyboardInterrupt):
        input_error = None
    return input_error


def start_program():

    menu = raw_input(u'Enter "Send a Thank You", "Create a Report" or "Ouit":')

    while True:
        if menu == "Send a Thank You":
            thank_you()
        elif menu == "Create a Report":
            donor_report()
        else:
            quit()


def thank_you():

    thank_you.gotmail = raw_input(u"Enter donor's full name or type (list): ")

    for i in donors:
        if thank_you.gotmail in donors.keys():
            add_donation()
        else:
            thank_you.gotmail == "list"
            print donors.keys()
            thank_you()


def add_donation():

    d_amount = round(float(raw_input(u"Enter donation amount Ex: 25.00: ")))
    if type(d_amount) == float:
        donors[thank_you.gotmail].append([d_amount])
        start_program()
    else:
        print("Please enter a number.")
        add_donation()


def donor_report():
    pass


start_program()
