person = "Harold Finch"
print person[0],person[1]; # H a
print person[0:6] # Harold
greeting = "Hello " + person; # Hello Harold Finch
print greeting[:6] + "John Reese"; # Hello John Reese
contains = 'H' in person;
notcontains = 'R' in person;
print contains, notcontains; # True, False