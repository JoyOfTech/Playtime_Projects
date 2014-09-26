# Lesson 2: PBJ Loop

# Goal #1: Write a new version of the PB&J program that uses a while loop. 
"""
total = 1 #I have no idea how anyone found this out. add variable "total", make it equal 1, then add 1 each time.
bread = 83
peanutbutter = 23
jelly = 18


sandwich = min(bread / 2, peanutbutter, jelly)


while sandwich >= 1:
    
    print "Making Sandwich #{}".format(total)

    sandwich = sandwich - 1 #so it doesn't go on forever
    total = total + 1

if sandwich < 1:
    
    print "All done; only had enough ingredients for {} sandwiches.".format(total -1)
"""

    
# Goal #2 Modify program to say how many sandwiches-worth of each ingredient remains.

total = 1 
bread = 28
peanutbutter = 23
jelly = 18

sandwich_bread = bread / 2

sandwich = min(sandwich_bread, peanutbutter, jelly)
#sandwich_bread will be easier to loop (i.e. bread/2 -1 <-- order of operations?)


while sandwich > 1:
    
    print "Making Sandwich #{}".format(total)
    print "I have enough bread for {} more sandwiches, enough peanutbutter for {} more, and enough jelly for {} more.".format(sandwich_bread, peanutbutter, jelly)

# here's how to get the ingredients to go down, while the total goes up.
    sandwich = sandwich - 1
    total = total + 1
    sandwich_bread = sandwich_bread - 1 
    peanutbutter = peanutbutter - 1
    jelly = jelly - 1

if sandwich == 1: #this line is only to make the sentence "1 sandwich" instead of "1 sandwiches"
    print "Making Sandwich #{}".format(total)
    print "I have enough bread for {} more sandwich, enough peanutbutter for {} more, and enough jelly for {} more.".format(sandwich_bread, peanutbutter, jelly)

    sandwich = sandwich - 1
    total = total + 1
    sandwich_bread = sandwich_bread - 1 
    peanutbutter = peanutbutter - 1
    jelly = jelly - 1
    
if sandwich < 1:
    
    print "All done; only had enough ingredients for {} sandwiches.".format(total -1)

