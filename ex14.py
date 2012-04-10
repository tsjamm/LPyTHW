from sys import argv

script, user_name = argv
prompt = 'Enter->  '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer am I running?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Must be somewhere....
And I am running on a %r computer :P !!!
""" % (likes, lives, computer)
