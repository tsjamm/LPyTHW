tabby = "\tI'm tabbed in."
persian = "I'm split\non a line."
backslash = "I'm \\ a \\ fish."

fat = '''
I'll do a list:
\t-> %s
\t-> %r
\t-> %s
''' % (tabby, persian, backslash)

print fat
