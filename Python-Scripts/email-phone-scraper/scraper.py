'''
                                        "The Basic Scraper"
    
    This code is capable of extracting information of amercian phone numbers
    and generic email ids from any large set of texts copied into the clipboard.

    Thereafter it pastes it back on the clipboard which can then be pasted into the user preferred destination.
'''

import re,pyperclip

# PHONE regex

phoneRegex = re.compile(r'''

# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345 , ext. 12345 , x12345
(
((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
((ext(\.)?\s)|x(\d{2,5}))? # extension (optional)
)
''',re.VERBOSE)

# EMAIL regex

emailRegex   =  re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

# Getting the TEXT off the clip-board
text = pyperclip.paste()

# EXTRACT email and phone.no from the text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for item in extractedPhone:
    allPhoneNumbers.append(item[0])


# checking extracted data
print(allPhoneNumbers)
print(extractedEmail)

# COPY the extracted data to the clipboard
scrapedData = "Phone Numbers :\n\n" + '\n'.join(allPhoneNumbers) + '\n\n' + "Email IDs :\n\n" + '\n'.join(extractedEmail)
pyperclip.copy(scrapedData)
