import pygsheets

gc = pygsheets.authorize(outh_file='client_secretxxx.json')
#gc = pygsheets.authorize(service_file='service_creds.json')
# Open spreadsheet and then workseet
sh = gc.open('Сегафредо')

#alphabet = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N',
#15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21: 'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z', 27:'AA', 28:'AB', 29:'AC',
#30:'AD', 31:'AE', 32:'AF', 33:'AG', 34:'AH', 35:'AI', 36:'AJ', 37:'AK', 38:'AL', 39:'AM', 40:'AN', 41:'AO', 42:'AP'}

'''wks = sh[5]
cities = wks.get_values('A3','A30')
stores = wks.get_values('B3', 'B30')
#print(cities)
#print(stores)

positions=wks.get_values('G2','AP2', include_empty=True)
positions = positions[0]
wks.clear('AZ3', 'AZ30')
count=0
for count in range (3,31):
    netu=[]
    est=wks.get_values('G'+str(count),'AP'+str(count), include_empty=True)
    est = est[0]
    count+=1
    #count1+=1
    #print (cities[count-3], end='')
    #print(stores[count-3])
    for index, i in  enumerate(est):
        if i =='' or i=='0':
            print (positions[index])
            netu+=[positions[index]]
            #print(netu)
            wks.update_cell('AZ'+str(count-1), str(netu[:]))
            #print(count)
'''

wks=sh[6]

positions=wks.get_values('H2','AP2', include_empty=True)
positions = positions[0]
wks.clear('AS3', 'AS30')
count=0
for count in range (3,7):
    netu=[]
    est=wks.get_values('H'+str(count),'AO'+str(count), include_empty=True)
    est = est[0]
    count+=1
    #count1+=1
    #print (cities[count-3], end='')
    #print(stores[count-3])
    for index, i in  enumerate(est):
        if i =='' or i=='0':
            #print (positions[index])
            netu+=[positions[index]]
            print(netu)
            wks.update_cell('AS'+str(count-1), str(netu[:]))
            print(count)

#print (positions)
#print (est)

#for index, string in enumerate(est):
#    print (index, string)
#kikoriki = wks.range('G3:AP3', returnas='range')
#kikoriki.name = 'kikoriki'



# Update a cell with value (just to let him know values is updated ;) )
