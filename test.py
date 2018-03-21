import pygsheets

gc = pygsheets.authorize(outh_file='client_secretxxx.json')
#gc = pygsheets.authorize(service_file='service_creds.json')
# Open spreadsheet and then workseet
sh = gc.open('Segafredo_test')


wks = sh[5]
positions=wks.range('A2:AP2')
est=wks.get_values('G3','AP3', include_empty=True)
#kikoriki = wks.range('G3:AP3', returnas='range')
#kikoriki.name = 'kikoriki'
for i in est:
    if i=='1':
        print ('blya')
#print (positions)
print (est)


# Update a cell with value (just to let him know values is updated ;) )
