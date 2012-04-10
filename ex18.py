# Variable Number of Arguments
def print_two_variable(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_three_variable(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

# Fixed Number of Arguments
def print_two_fixed(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments
def print_none():
    print "I got nothin'."


print_two_variable("Sai","Teja")
print_three_variable("J","S","Teja")
print_two_fixed("Sai","Teja")
print_one("Wow")
print_none()
