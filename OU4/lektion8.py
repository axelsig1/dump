file2 = open('uppsala_tm_1722-2020.dat', 'r')
text = file2.read()
rows = text.splitlines()
avg1700 = []
avg1800 = []
avg1900 = []
avg2000 = []
listavg = [avg1700, avg1800, avg1900, avg2000]
tvalues = [2418, 3100, 3100, 620]
# Medel temp per år
counter = 1
temp17 = []
temp18 = []
temp19 = []
temp20 = []

for i in rows:
    if float(i[0:2]) == 17:
        if float(i[4:7]) == 5:  # Om det är den 5e månaden
            temp17.append(float(i[12:17]))
    if float(i[0:2]) == 18:
        if float(i[4:7]) == 5:  # Om det är den 5e månaden
            temp18.append(float(i[12:17]))
    if float(i[0:2]) == 19:
        if float(i[4:7]) == 5:  # Om det är den 5e månaden
            temp19.append(float(i[12:17]))
    if float(i[0:2]) == 20:
        if float(i[4:7]) == 5:  # Om det är den 5e månaden
            temp20.append(float(i[12:17]))

avgtemp17 = round((sum(temp17[1:31]))/31, 3)
avg1700.append(avgtemp17)
avgtemp18 = round((sum(temp18[1:31]))/31, 3)
avg1800.append(avgtemp18)
avgtemp19 = round((sum(temp19[1:31]))/31, 3)
avg1900.append(avgtemp19)
avgtemp20 = round((sum(temp20[1:31]))/31, 3)
avg2000.append(avgtemp20)

print(listavg)
