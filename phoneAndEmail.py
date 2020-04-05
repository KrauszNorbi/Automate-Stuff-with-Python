#! python3

import re, pyperclip

# Create a rejex for Danish phone numbers
phoneRegexDanish = re.compile(r'''
# +45 4646 0000, +45 46 46 00 00
(
(\+\d\d)?                                               # +45 (optional)
\s                                                      # space separator
((\d\d\d\d\s\d\d\d\d)|(\d\d\s\d\d\s\d\d\s\d\d))         # phone number
)
''', re.VERBOSE)


# Create a rejex for US phone numbers
phoneRegexUS = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional, can appear 0 or 1 times)
(\s|-)                          # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x)               # extension word-part (optional)
 (\d{2,5}))?                    # extension number-part (optional)
)                 
''', re.VERBOSE)


# Create a rejex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+                 # name part (+ = one or more of them)
@                               # @ symbol
[a-zA-Z0-9_.+]+                 # domain name part
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedDanishPhone = phoneRegexDanish.findall(text)
extractedUsPhone = phoneRegexUS.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedDanishPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)
