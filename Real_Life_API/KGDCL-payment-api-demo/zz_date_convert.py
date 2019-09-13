from datetime import datetime

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
###############################################################
# date = 'Jun 1 2005  1:33PM'
# datetime_object = datetime.strptime(date, '%b %d %Y %I:%M%p')
##############################################################
date = '25-03-2008'
datetime_object = datetime.strptime(date, '%d-%m-%Y')
#datetime_object = datetime.strptime(date, '%d-%b-%Y')#.strftime('%d-%m-%Y')
my_date = datetime_object.date()
##############################################################
print(datetime_object)
print(my_date)
print(type(datetime_object.date()))

# import datetime
# t = datetime.datetime(2012, 2, 23, 0, 0)
# t.strftime('%m/%d/%Y')
# print(t)
# print("******",type(t))
