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
"""The script should have a data structure that holds a list of your donors and
a history of the amounts they have donated.
-When run, the script should prompt the user to choose from a menu of 2
actions: ‘Send a Thank You’ or ‘Create a Report’.
-If the user selects ‘Send a Thank You’, prompt for a Full Name.
-If the user types ‘list’, show them a list of the donor names and re-prompt
-If the user types a name not in the list, add that name to the data structure
and use it.
-If the user types a name in the list, use it.
-Once a name has been selected, prompt for a donation amount.
-Verify that the amount is in fact a number, and re-prompt if it isn’t.
-Once an amount has been given, add that amount to the donation history of the
selected user.
-Finally, use string formatting to compose an email thanking the donor for their
generous donation. Print the email to the terminal and return to the original
prompt.
"""

donors = [u"Rodney Dangerfield", u"Margret Thatcher", u"William Shakespeare", u"Harriet Tubman"]
list = donors
total_donations = [18000, 23000, 5000, 22000]
num_donations = [5, 7, 2, 6]
avg_donations = []

def safe_input(key):
    try:
        input_error = raw_input(key)
    except (EOFError, KeyboardInterrupt):
        input_error = None
    return input_error
