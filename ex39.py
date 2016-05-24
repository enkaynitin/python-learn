# create a mapping of state to abbreviation
states = {
    'Bangladesh': 'BD',
    'Bhutan': 'BT', 
    'India': 'IN',
    'Nepal': 'NP',
	'Pakistan':'PK'
}

# create a basic set og states and some cities in them
cities = {
    'IN': 'Delhi',
    'PK': 'Islamabad',				
    'BT': 'Thimphu',
}

#add some more cities
cities['NP'] = 'Kathmandu'
cities['BD'] = 'Dhaka'

# print out some cities
print '-' * 10
print "NP State has: ", cities['JK']
print "BD State has: ", cities['KA']

#print some states
print '-' * 10
print "Pakistan's abbreviation is: ", states['Pakistan']
print "India's abbreviation is: ", states['India']

#do it by using the state then cities dict
print '-' * 10
print "Pakistan has: ", cities[states['Pakistan']]
print "India has: ", cities[states['India']]

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
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city
