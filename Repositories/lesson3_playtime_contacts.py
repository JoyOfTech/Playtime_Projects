# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
    'Joy': {'phone': '202-555-1234', 'twitter': '@jmwisthebest', 'github': '@joymw' },
    'Rep. Gabbard': {'phone': '808-404-9876', 'twitter': '@reptulsigabbard', 'github': '@repgabbard'},
    'Ndamukong Suh': {'phone': '313-777-3313', 'twitter': '@pumpkinSUHp', 'github': '@DetriotLionsSuh'},
    'Stromae':{'phone': '011 32 2 123 4567', 'twitter': '@Stromae', 'github': '@touslesmemes'},
    'Edie Windsor': {'phone': '202-345-9467', 'twitter': '@EdieWindsor', 'github': '@EdieWindsor'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

"""
#this code takes up less space, but I don't understand it 
for contact in contacts.keys():
    print "{0}'s contact information is:\n Phone:{1}\n Twitter: {2}\n Github: {3}".format(contact,contacts[contact]["phone"],contacts[contact]["twitter"],contacts[contact]["github"])
"""

#I tried the code below, and it works. but I can't get it to run with html
for name, contact_info in contacts.items():
    print "{0}'s contact information is: ".format(name)
    for contact_type,contact_value in contact_info.items():
        print"{0}: {1}".format(contact_type,contact_value)
    print "\n" #this is to put a new line in between contacts


# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey


# Goal 2:  Display that information as an HTML table.

contacts = {
    'Joy': {'phone': '202-555-1234', 'twitter': '@jmwisthebest', 'github': '@joymw' },
    'Rep. Gabbard': {'phone': '808-404-9876', 'twitter': '@reptulsigabbard', 'github': '@repgabbard'},
    'Ndamukong Suh': {'phone': '313-777-3313', 'twitter': '@pumpkinSUHp', 'github': '@DetriotLionsSuh'},
    'Stromae':{'phone': '011 32 2 123 4567', 'twitter': '@Stromae', 'github': '@touslesmemes'},
    'Edie Windsor': {'phone': '202-345-9467', 'twitter': '@EdieWindsor', 'github': '@EdieWindsor'}
}

# """ = making HTML a string (not actually commenting out)

html_table = """<table border="1">
 <tr>
 <td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Phone: {1} </td>
 <td> Twitter: {2} </td>
 <td> Github: {3} </td>
 </tr>
 </table>
"""

for c in contacts:
    name = c   
    phone = contacts[c]['phone']
    twitter = contacts[c]['twitter']
    github = contacts[c]['github']
    print html_table.format(name, phone, twitter, github)


# Sample output:
# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# ...

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

with open("lesson3.html", "w") as contacts_html:
    contacts_html.write("<html><body>") #telling it they we're in html
    for c in contacts:
        name = c   
        phone = contacts[c]['phone']
        twitter = contacts[c]['twitter']
        github = contacts[c]['github']
        contacts_html.write(html_table.format(name, phone, twitter, github))
    contacts_html.write("</body></html>") #closing html



# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).
