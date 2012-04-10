bikes = 50
space_in_a_bike = 3.0
drivers = 30
passengers = 50
bikes_not_driven = bikes - drivers
bikes_driven = drivers
transport_capacity = bikes_driven * space_in_a_bike
average_passengers_per_bike = passengers / bikes_driven


print "There are", bikes, "bikes available."
print "There are only", drivers, "drivers available."
print "There will be", bikes_not_driven, "empty bikes today."
print "We can transport", transport_capacity, "people today."
print "We have", passengers, "to transport today."
print "We need to put about", average_passengers_per_bike,
print "or", average_passengers_per_bike+1, "on each bike."
