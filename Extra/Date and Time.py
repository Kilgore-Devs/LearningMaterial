import datetime  # imports datetime module

x = datetime.datetime.now()  # gets the current date and time
print(x)  # prints x in YYYY-MM-DD HH:MM:SS.MCROSEC format

y = datetime.datetime.now()
print(y.year)  # prints the year of y
print(y.strftime("%A"))  # prints the current day of y

# create a date using datetime() class - constructor of datetime module.
# datetime() require 3 parameters - year, month, and day.
z = datetime.datetime(2023, 1, 1)
print(z)

a = datetime.datetime(1968,6,1, 12, 38, 55, 123456)
print(a.strftime("%A"))  # Weekday full name
print(a.strftime("%a"))  # Weekday short name
print(a.strftime("%B"))  # month full name
print(a.strftime("%b"))  # month short name
print(a.strftime("%c"))  # Local version of date and time
print(a.strftime("%C"))  # Century
print(a.strftime("%d"))  # day of month
print(a.strftime("%f"))  # Microseconds
""" %a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01 """
