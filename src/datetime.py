import time
import calendar
localtime = time.asctime(time.localtime(time.time()))  # formatted local time
print "Local time:", localtime
cal = calendar.month(2016,1);
print "Calendar of January in 2016:",cal
isLeap = calendar.isleap(2017); # False
print isLeap