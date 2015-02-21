#note: currently not working correctly
print "enter salary"
salary = int(raw_input())
print "enter salary increase in percent"
increase = int(raw_input())/100
old_month = salary/12
new_month = old_month
new_month += old_month *increase
unpaid = new_month*6

print "new monthly wage: %s\nunpaid: %s" % (new_month, unpaid)
