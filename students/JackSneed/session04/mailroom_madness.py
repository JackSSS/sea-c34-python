#!/usr/bin/env python

donors = {u"Rodney Dangerfield": [9478.12],
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
    """Creates selection menu"""
    menu = raw_input(u'Enter 1 for "Send a Thank You"' +
                     ', 2 for "Create a Report"' +
                     ', or 3 for "Ouit":')

    while True:
        if menu == u"1":
            thank_you()
        elif menu == u"2":
            donor_report()
        else:
            menu == u"3"
            quit()

def thank_you():
    """Creates thank you letter menu"""
    thank_you.gotmail = raw_input(u"Enter donor's full name or type (list): ")

    for i in donors:
        if thank_you.gotmail in donors.keys():
            add_donation()
        elif thank_you.gotmail == u"list":
            print donors.keys()
            thank_you()
        else:
            thank_you.gotmail not in donors.keys()
            donors[thank_you.gotmail] = []
            print(u"This new donor will be added. Re-enter new donor name\
                  to add their donotion.")
            thank_you()

def add_donation():
    """Adds donation amount and checks if a number"""
    add_donation.amount = (float(raw_input(u"Enter donation amount" +
                                           " Ex: 25.00: ")))

    if type(add_donation.amount) == float:
        donors[thank_you.gotmail].append([add_donation.amount])
        letter()
    else:
        print(u"Please enter a number and include a decimal Ex: 25.00")
        add_donation()

def letter():
    """Generates thank you letter with donor name and amount"""
    thanks =  u"\n\nDear {},\n \n\nThank you for the donation, of ${}!\n\
    \nYour continued support is greatly appreciated.\n\
    \nPlease retain this letter for tax purposes.\n\n\
    \nYours truly,\n\
    \nThe Foundation\n".format(thank_you.gotmail, add_donation.amount)

    print(thanks)
    start_program()

def donor_report():
    """Creates a report with total historical donation amount. Including donor
    Name, total donated, number of donations and average donation amount as
    values in each row.
    """
    report = []

    for name, amount in donors.items():
        total_donations = sum(amount)
        num_donations = len(amount)
        avg_donations = (total_donations/num_donations)
        report.append((name, total_donations, num_donations, avg_donations))

    print("{:20} {:20} {:20} {:20}\n".format(
          "Name", "Total Donations", "Times Donated",
          "Avgerage Donation"))

    for row in report:
        print("{:20} {:<20} {:<20} {:<20}".format(
              row[0], row[1], row[2], row[3]))

    start_program()

def quit():

    print("Enter 'ctrl + d' to end this program.")
    start_program()


start_program()
