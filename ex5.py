my_name = "Nitin Kumar"
my_age = 28 # not a lie
my_height = 66 # inches
my_weight = 85  # Kg
my_eyes = "Black"
my_teeth = "white"
my_hair = "Black"

print "Lets talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d Kg heavy." % my_weight
print "actually that's not too heavy."
print "He's got %s eyes and %s hair. " % (my_eyes, my_hair)
print "his teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." %(
	my_age, my_height, my_weight, my_age + my_height + my_weight)
