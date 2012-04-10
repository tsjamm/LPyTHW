formatter = "%r %r %r %r"

print formatter % (10, 20, 30, 40)
print formatter % ("ten", "twenty", "thirty", "fourty")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", # with a ' the string displays with double quotes
    "So I said good'nt."   # Here also double quotes.
)
