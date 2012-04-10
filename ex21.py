def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Welcome to Primitive Math Functions"

x = int(raw_input("Enter First Number x = ")) # Converting String to Integer
y = int(raw_input("Enter Second Number y = "))# Converting String to Integer

one = add(x,y)
two = subtract(x,y)
three = multiply(x,y)
four = divide(x,y)

print "one = %d\ntwo = %d\nthree = %d\nfour = %d" % (one, two, three, four)

print "Now For Combination of Functions"

wow = add(one, subtract(two, multiply(three, divide(four, 2))))
print "The Combined Answer is ", wow, " real cool isn't it?"
