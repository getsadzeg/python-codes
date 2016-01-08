var = 99; #Try assigning value 100. It will be true
if(var == 100) : print "Yeah, var equals 100";
else : print "Nope. var doesn't equals 100";

if(var < 30):
	print "var is less than 30";

elif(var > 30): # 'elif' is absolutely equivalent of 'else if'. I didn't know about it.
	print "var is greater than 30";

else:
	pass