"""Can I make a Peanut Butter and Jelly Sandwich?

F5 = RUN CODE

First Goal """


bread = 72
peanutbutter = 25
jelly = 20

""" 
if bread >= 2 and peanutbutter >= 1 and jelly >= 1:
        
     print ("It's Peanut Butter Jelly Time!")

else:
    print ("Go buy a panini")

        

 Second Goal: How many Sandwiches?

if bread >= 2 and peanutbutter >= 1 and jelly >= 1:
        
    print "You can make this many sandwiches"

else:
    print "Go buy a panini"
"""

# Third Goal
# % = 0 or 1
# 0 = no remainder (even)
# 1 = remainder (odd)

"""
if bread % 2 == 1 and peanutbutter > 0 and jelly > 0:
        
    print ("You can make a sandwich, but it will have to be open-faced.")

elif bread % 2 == 0 and peanutbutter > 0 and jelly > 0:

    print ("It's Peanut Butter Jelly Time!")

else:
    
    print ("You're going to go hungry for lunch")

 Fourth Goal

if bread % 2 == 1 and peanutbutter > 0 and jelly > 0:
        
    print ("You can make a sandwich, but it will have to be open-faced.")

elif bread % 2 == 0 and peanutbutter > 0 and jelly > 0:

    print ("It's Peanut Butter Jelly Time!")

elif bread < 2:
    print ("You need more bread")

elif peanutbutter < 1:
    print ("You need more peanut butter")

elif jelly < 1:
    print ("You need more jelly")
"""

#Fifth Goal

if bread % 2 == 1 and peanutbutter > 0 and jelly > 0:
        
    print ("You can make a sandwich, but it will have to be open-faced.")

elif bread % 2 == 0 and peanutbutter > 0 and jelly > 0:

    print ("It's Peanut Butter Jelly Time!")

elif bread < 2:
    print ("You need more bread")

elif peanutbutter < 1:
    print ("You need more peanut butter")

elif bread >= 2 and jelly < 1 and peanutbutter >= 1:
    print ("You can make a peanutbutter sandwhich. Which is pretty disgusting. Get your life together.")

sandwichbread = bread / 2
sandwiches = min(sandwichbread, peanutbutter, jelly)

if peanutbutter >= 1:
    if jelly >= 1:
        if bread >=2:
            print('I can have this many sandwiches: {}'.format(sandwiches))


