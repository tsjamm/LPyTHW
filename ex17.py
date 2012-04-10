from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying Command Initiated. From %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "Input File Analyzed. It is %d bytes long" % len(indata)

print "Checking Status of Output File...\nExists? %r" % exists(to_file)
print "Hit RETURN To Continue Operation, CTRL-C To Abort Operation..."
raw_input()

open(to_file, 'w').write(indata)

print "Task Completed.(dot)"

#output.close()
#input.close()
