counter = 0;
while(counter < 10): # while loop
	counter+=1;
	print "Now counter is ", counter;


print "out of loop" # indentation here

"""while(counter): 
# Ok. Just infinite loop.
	print "LOL";"""

for letter in "Python":
	print letter, "\n"; # Prints every letter in referenced word

for i in range(1,10):
	if(i == 5): continue # Skips fifth iteration
	if(i == 8): break # Buut breaks at 8th iteration.
	print i;
