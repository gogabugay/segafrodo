import datetime
from datetime import date, timedelta

if date.today().weekday()==0: #определяем нужную среду
    wednesday = date.today() - timedelta(5)
elif date.today().weekday()==1:
    wednesday = date.today() - timedelta(6)
elif date.today().weekday()==2:
    wednesday = date.today() - timedelta(7)
elif date.today().weekday()==3:
    wednesday = date.today() - timedelta(1)
elif date.today().weekday()==4:
    wednesday = date.today() - timedelta(2)
elif date.today().weekday()==5:
    wednesday = date.today() - timedelta(3)
elif date.today().weekday()==6:
    wednesday = date.today() - timedelta(4)
print (wednesday)
