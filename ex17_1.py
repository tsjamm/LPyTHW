from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying Command Initiated. From %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "Input File Analyzed. It is %d bytes long" % len(indata)

print "Checking Status of Output File...\nExists? %r" % exists(to_file)
print "Hit RETURN To Continue Operation, CTRL-C To Abort Operation..."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Task Completed.(dot)"

output.close()
input.close()
