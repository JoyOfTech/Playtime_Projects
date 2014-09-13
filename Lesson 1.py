Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> print ("Watch out, world!")
Watch out, world!
>>> "This is a string"
'This is a string'
>>> "This will give you an error'
SyntaxError: EOL while scanning string literal
>>> 'But this is "entirely" okay'
'But this is "entirely" okay'
>>> 'My governor's name is Martin O'Malley'
SyntaxError: invalid syntax
>>> 'She said, "Testing, 1-2-3"'
'She said, "Testing, 1-2-3"'
>>> 'My governor\'s name is Martin O'\Malley'
SyntaxError: unexpected character after line continuation character
>>> 'My governor\'s name is Martin O\'Malley'
"My governor's name is Martin O'Malley"
>>> print(I am Rachel/n this is Hear Me Code")
      
SyntaxError: invalid syntax
>>> print("I am Rachel/n this is Hear Me Code")
I am Rachel/n this is Hear Me Code
>>> print("I am Rachel/nthis is Hear Me Code")
I am Rachel/nthis is Hear Me Code
>>> print("I am Rachel\nthis is \ "Hear Me Code\"")
      
SyntaxError: invalid syntax
>>> print("I am Rachel\nthis is\"Hear Me Code\"")
I am Rachel
this is"Hear Me Code"
>>> #press alt p to bring up previous line
>>> "Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files"
'Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files'
>>> print "Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files"
Lesson 	 Topic 
 1 	 Strings and Conditionals 
 2 	 Lists and Loops 
 3 	 Dictionaries & Files
>>> print "Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files"
Lesson 	 Topic 
 1 	 Strings and Conditionals 
 2 	 Lists and Loops 
 3 	 Dictionaries & Files
>>> output = "Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files"
>>> print output
Lesson 	 Topic 
 1 	 Strings and Conditionals 
 2 	 Lists and Loops 
 3 	 Dictionaries & Files
>>> output = "State \t Capital \n Michigan \t Lansing \n New York \t Albany \n California \t Sacramento \n New Jersey \t Trenton \n Florida \t Tallahassee \n Montana \t Helena"
>>> print output
State 	 Capital 
 Michigan 	 Lansing 
 New York 	 Albany 
 California 	 Sacramento 
 New Jersey 	 Trenton 
 Florida 	 Tallahassee 
 Montana 	 Helena
>>> first_name = "Shannon"
>>> print first_name[o]

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print first_name[o]
NameError: name 'o' is not defined
>>> print first_name[0]
S
>>> print first_name[1:5]
hann
>>> #from the second letter up UNTIL the sixth letter, but NOT the sixth letter
>>> print first_nam[ :5]

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print first_nam[ :5]
NameError: name 'first_nam' is not defined
>>> print first_name[:5]
Shann
>>> print first_name[3:6]
nno
>>> phone = "(202) 456-7890"
>>> print phone[0:6]
(202) 
>>> print phone[1:5]
202)
>>> print phone[1:4]
202
>>> print phone[7:10]
56-
>>> 
>>> print phone[6:9]
456
>>> "I am {0} and my age is {1}"
'I am {0} and my age is {1}'
>>> "I am {0} and my age is {1}".format("Joy", "28")
'I am Joy and my age is 28'
>>> "Your Number is {0}".format(phone)
'Your Number is (202) 456-7890'
>>> 'I am Joy and my age is 28'
'I am Joy and my age is 28'
>>> phone = 1234567890
>>> "Your number is {0}".format(phone)
'Your number is 1234567890'
>>> "your number is {0}".format
<built-in method format of str object at 0x02D0A1B0>
>>> "Your number is {0}".format(phone[5:8])

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    "Your number is {0}".format(phone[5:8])
TypeError: 'int' object has no attribute '__getitem__'
>>> phone = 555-1234
>>> print phone
-679
>>> phone = "555-1234"
>>> print phone
555-1234
>>> Phone = "2021234567"
>>> "Your number is {0}".format(phone)
'Your number is 555-1234'
>>> phone = "2021234567"
>>> "your number is {0}".format(phone)
'your number is 2021234567'
>>> "your number is {0}".format(phone[5:8])
'your number is 345'
>>> "your number is {0}".format(phone[3:])

'your number is 1234567'
>>> phone = "202-123-4567".format(phone[4:])
>>> phone = "202-123-4567".format(phone[4:])
>>> phone = "202-123-4567"
>>> "your number is {0}".format(phone[4:])
'your number is 123-4567'
>>> "Your phone number is {0}{1}{2}".format(phone)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    "Your phone number is {0}{1}{2}".format(phone)
IndexError: tuple index out of range
>>> "Your phone number is {0}{1}{2}".format(phone[0:3],[4:7],[8:])
SyntaxError: invalid syntax
>>> "Your phone number is {0}{1}{2}".format(phone[0:3],phone[4:7],phone[8:])
'Your phone number is 2021234567'
>>> "Your phone number is {0}-{1}-{2}".format
<built-in method format of str object at 0x02D376B0>
>>> "Your phone number is {0}-{1}-{2}".format(phone[0:3],phone[4:7],phone[8:])
'Your phone number is 202-123-4567'
>>> "Your phone number is {2}-{3}".format(phone[0:3],phone[4:7],phone[8:])

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    "Your phone number is {2}-{3}".format(phone[0:3],phone[4:7],phone[8:])
IndexError: tuple index out of range
>>> "Your phone number is {1}-{2}".format(phone[0:3],phone[4:7],phone[8:])
'Your phone number is 123-4567'
>>> "Your phone number is ({0}) {1}-{2}".format(phone[0:3],phone[4:7],phone[8:])
'Your phone number is (202) 123-4567'
>>> "Your phone number is +1-{0}-{1}-{2}".format(phone[0:3],phone[4:7],phone[8:])
'Your phone number is +1-202-123-4567'
>>> # .find is a method, just like .format
>>> email_address = "joy.m.whitt@gmail.com"
>>> email_address.find("@")
11
>>> email [email_address.find("@"):]

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    email [email_address.find("@"):]
NameError: name 'email' is not defined
>>> [email_address.find("@"):]
SyntaxError: invalid syntax
>>> phone - "555-1234"

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    phone - "555-1234"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> phone.replace("1234","5678")
'202-123-4567'
>>> phone = "555-1234"
>>> phone.replace("1234","5678")
'555-5678'
>>> Name = "Joy Marie Whitt"
>>> Name.replace("Marie","M.")
'Joy M. Whitt'
>>> Numbers = "Seven Eight Nine Ten"
>>> Numbers.replace("Seven","7","Eight","8","Nine","9","Ten","10")

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    Numbers.replace("Seven","7","Eight","8","Nine","9","Ten","10")
TypeError: replace() takes at most 3 arguments (8 given)
>>> Numbers.replace("Seven","7","Eight","8","Nine","9")

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    Numbers.replace("Seven","7","Eight","8","Nine","9")
TypeError: replace() takes at most 3 arguments (6 given)
>>> Numbers.replace("Seven","7")
'7 Eight Nine Ten'
>>> number = "Should I spell out the number nineteen, or no?"
>>> number.replace("nineteen","19")
'Should I spell out the number 19, or no?'
>>> 1 = len("apples")
SyntaxError: can't assign to literal
>>> 1=len("apples")
SyntaxError: can't assign to literal
>>> # .strip() will eliminate spaces at beginning and end of string
>>> # .count() will tell you how many times a thing appears in a string
>>> s = "eeeeeehelloeeeeeeeee"
>>> s.strip("e")
'hello'
>>> s.upper()
'EEEEEEHELLOEEEEEEEEE'
>>> s.strip("e").upper()
'HELLO'
>>> "How Happy is your Happy Hour?"
