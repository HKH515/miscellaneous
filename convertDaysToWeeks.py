import math
raw_days = int(raw_input())
weeks = math.floor(raw_days/7)
days = raw_days % 7
print "weeks: %s\ndays: %s" % (int(weeks), days)
