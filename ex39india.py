# create a mapping of state to abbreviation
states = {
    'Punjab': 'PB',
    'Odisha': 'OR', 
    'Uttar Pradesh': 'UP',
    'Himachal Pradesh' : 'HP',
    'Jammu and Kashmir': 'JK',
}

# create a basic set og states and some cities in them
cities = {
    'OR': 'Bhubaneswar',
    'UP': 'Lucknow',				
    'JK': 'Srinagar',
}

#add some more cities
cities['HP'] = 'Shimla'
cities['PB'] = 'Chandigarh'

# print out some cities
print '-' * 10
print "JK State has: ", cities['JK']
print "UP State has: ", cities['UP']

#print some states
print '-' * 10
print "Jammu and Kashmir's abbreviation is: ", states['Jammu and Kashmir']
print "Uttar Pradesh's abbreviation is: ", states['Uttar Pradesh']

#do it by using the state then cities dict
print '-' * 10
print "Jammu and Kashmir has: ", cities[states['Jammu and Kashmir']]
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
#safely get an abbreviation for state that not be there
state = states.get('None', None)

if not state:
    print "Sorry, no None."

# get a city with a default value
city = cities.get('None', 'Does Not Exist')
print "The city for the state 'None' is: %s" %city
