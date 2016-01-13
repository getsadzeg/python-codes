def greeting(Name):
    "This function greets to person with Name."  # Docs
    return "Hello " + Name

print greeting("John")


def plus(x, y):
    #  x variable won't change outside the function because of immutability
    x += 4
    y = 8
    print "Inside x:", x
    print "Inside y:", y  # will be 8, reference is being overwritten
    return

x = 5  # won't be 9
y = 4
plus(x, y)
print "Outside x:", x
print "Outside y:", y  # won't be change


def setbaby(name, age=0):
    print "name:", name
    print "age:", age
    return

setbaby(name="zuck") # we give no argument of age, so it will be 0
