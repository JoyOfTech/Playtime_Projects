
# Lesson 2 Playtime: bottles of beer


beer = 99

while beer > 1:
    print "{0} bottles of beer on the wall, {0} bottles of beer...".format(beer)

    beer = beer - 1

    if beer > 1:

        print "Take one down, pass it around, {0} bottles of beer on the wall".format(beer)
        
    else: 

        print "Take one down, pass it around, {0} bottle of beer on the wall!".format(beer)        
    

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall




