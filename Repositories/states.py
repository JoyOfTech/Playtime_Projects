#Lesson 2 Playtime: States

state_abbreviation = ["AL","AK","AZ","AR","CA", "CO","CT","DE","DC", "FL","GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH","NJ", "NM", "NY", "NC", "ND", "OH","OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV","WI", "WY"]

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


print "<select>"

for state_abbreviation, states in zip(state_abbreviation, states):

    print "<option value = '{0}'>{1}</option>".format(state_abbreviation, states)


print "</select>"





#zipped = zip(state_abbreviation, states)


#    print "<option value = (zipped{0})>states</option>".format(zipped)  

