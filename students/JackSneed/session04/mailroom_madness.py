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



donors = dict = {u"Rodney Dangerfield": [9478.12],
                u"Margret Thatcher": [23477.13],
                u"William Shakespeare": [5382.01],
                u"Harriet Tubman": [20020.88]}


def safe_input(key):
    try:
        input_error = raw_input(key)
    except (EOFError, KeyboardInterrupt):
        input_error = None
    return input_error


def start_program():

    menu = raw_input(u'Enter "Send a Thank You", "Create a Report" or "Ouit":')

    while True:
        if menu == u"Send a Thank You":
            thank_you()
        elif menu == u"Create a Report":
            donor_report()
        else:
            quit()


def thank_you():

    thank_you.gotmail = raw_input(u"Enter donor's full name or type (list): ")

    for i in donors:
        if thank_you.gotmail in donors.keys():
            add_donation()
        else:
            thank_you.gotmail == u"list"
            print donors.keys()
            thank_you()


def add_donation():

    add_donation.amount = (float(raw_input(u"Enter donation amount Ex:\n\
    25.00: ")))

    if type(add_donation.amount) == float:
        donors[thank_you.gotmail].append([add_donation.amount])
        letter()
    else:
        print(u"Please enter a number.")
        add_donation()

def letter():

    welcome =  u"\n\nDear {},\n \n\nThank you for the donation, of ${}!\n\
    \nYour continued support is greatly appreciated.\n\
    \nPlease retain this letter for tax pruposes.\n\n\
    \nYours truly,\n\
    \nThe Foundation".format(thank_you.gotmail,\
    add_donation.amount)

    print(welcome)
    start_program()

def donor_report():
    pass


start_program()
