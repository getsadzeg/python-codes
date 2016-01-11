personinfo = {'Name': 'John', 'Surname': 'Reese', 'Occupation': 'Killer'};
personinfo['Occupation'] = "Agent"; # Update 
personinfo['Employer'] = "Harold Finch"; # Add
print personinfo['Name']
print "personinfo keys:", personinfo.keys();
print "personinfo values:", personinfo.values();
personinfo.clear();
print "personinfo's length after clearing:", len(personinfo);


