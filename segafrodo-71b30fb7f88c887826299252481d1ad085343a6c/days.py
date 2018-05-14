import pygsheets
import datetime
gc = pygsheets.authorize(outh_file='client_secretxxx.json')
#gc = pygsheets.authorize(service_file='service_creds.json')
# Open spreadsheet and then workseet
sh = gc.open('Copy of Сегафредо')
wks = sh[5]
dates = wks.get_values('F3','F30')

print (dates)

for date in dates[0]:
    date = int (date)
    date = datetime.date(date)
