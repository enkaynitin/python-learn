# create a mapping of state to abbreviation
states = {
    'Delhi': 'DL',
    'Maharashtra': 'MH', 
    'Uttar Pradesh': 'UP',
    'Himachal Pradesh' : 'HP',
    'Madhya Pradesh': 'MP',
}

# create a basic set og states and some cities in them
cities = {
    'MH': 'Mumbai',
   	'UP': 'Lucknow',				
    'MP': 'Bhopal',
}

#add some more cities
cities['HP'] = 'Shimla'
cities['DL'] = 'New Delhi'

# print out some cities
print '-' * 10
print "MP State has: ", cities['MP']
print "UP State has: ", cities['UP']

#print some states
print '-' * 10
print "Madhya Pradeh's abbreviation is: ", states['Madhya Pradesh']
print "Uttar Pradesh's abbreviation is: ", states['Uttar Pradesh']

#do it by using the state then cities dict
print '-' * 10
print "Madhya Pradesh has: ", cities[states['Madhya Pradesh']]
print "Uttar Pradesh has: ", cities[states['Uttar Pradesh']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated  %s" % (state, abbrev)

# print every city is state
print '-'* 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % ( state, abbrev, cities[abbrev])


print '-' * 10
#safely get an abbreviation by state that not be there
state = states.get('Bengal', None)

if not state:
    print "Sorry, no Bengal."

# get a city with a default value
city = cities.get('Bengal', 'Does Not Exist')
print "The city for the state 'WB' is: %s" %city
