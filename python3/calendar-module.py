# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
# print (calendar.TextCalendar(firstweekday=6).formatyear(2015))
m,d,y=map(int,input().split())
print(["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"][calendar.weekday(y,m,d)])
