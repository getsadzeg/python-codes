langlist = ["cpp", "c", "java", "python"]
print "first element of langlist:", langlist[0];
langlist[0] = "C#"; # Updating list element
print "after modification:", langlist[0];
size = len(langlist);
print "langlist's size is",size;
del langlist[1]; # del calling
for element in langlist:
	print element; # Prints each element of list except second element because of 'del' calling