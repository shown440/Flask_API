from datetime import datetime

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
###############################################################
# date = 'Jun 1 2005  1:33PM'
# datetime_object = datetime.strptime(date, '%b %d %Y %I:%M%p')
##############################################################
date = '02-MAY-2019'
datetime_object = datetime.strptime(date, '%d-%b-%Y')
##############################################################
print(datetime_object)
print(datetime_object.date())
print(type(datetime_object))
