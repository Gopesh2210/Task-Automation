'''
    Takes in map address from the (command line argument) OR (clipboard)
    Thereafter it uses the webbrowser module to redirect to the location in google map using this arg 
'''

import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', 'country', 'state', 'city']

if len(sys.argv) > 1:
    # slices the arg and makes an address string with spaces in between
    address = ' '.join(sys.argv[1:])

else :
    # stores the address copied in the clipboard which can be passed further
    address = pyperclip.paste()


# HOW TO RUN IT :
# OPENS THE ADDRESS YOU HAVE COPIED IN CLIPBOARD ON GOOGLE MAPS, THE MOMENT YOU RUN THE CODE

# GOOGLE MAPS link : https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)




