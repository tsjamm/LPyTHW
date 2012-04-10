def ice_cream_types(cone_count, cup_count):
    print "You have %d cones!" % cone_count
    print "You have %d cups of icecream!" % cup_count
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
ice_cream_types(30, 40)


print "OR, we can use variables from our script:"
amount_of_cones = 10
amount_of_cups = 50

ice_cream_types(amount_of_cones, amount_of_cups)

print "We can even do math inside too:"
ice_cream_types(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
ice_cream_types(amount_of_cones * 10, amount_of_cups + 100)
