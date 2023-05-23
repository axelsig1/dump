import matplotlib.pyplot as plt
import csv


# Uppgift 1
def load_csv(filename):
    lexicon = {}    # Tomt lexikon
    with open(filename, 'r') as csvf:   # Läser filen
        reader = csv.reader(csvf)
        for row in reader:      # itererar över varje rad
            i = 1   # kolumn 2 innehåller lanskod, alltså i = 1
            if row[0] == 'Country Name':    # Hoppar över första raden
                continue
            countrycode = row[i]    # Sparar landskoden
            countrycode = countrycode.lower()   # gör om till små bokstäver
            i += 2  # Alla värden börjar i kolumn 4, dvs i = 3
            co2 = [float(v) for v in row[i:]]   # Sätter co2 till en lista av alla värden efter kolumn 4.
            lexicon[countrycode] = co2  # Sparar till lexikon
        return lexicon


# Uppgift 2
def smooth_a(x, n):     # Funktionen jämnar ut en lista
    x = [x[0]]*n + x + [x[-1]]*n    # Förlänger listan med n gånger första elementet och n gånger sista elementet
    r = []              # Skapar en ny lista
    for i in range(n, len(x)-n):        # För varje element i den ursprungliga listan x ska:
        r.append(sum(x[i-n:i+n+1])/(2*n+1))     # medelvärdet av de 2n närmaste elementen beräknas och läggas in i r
    return r


# Uppgift 1
filename = 'CO2Emissions_filtered.csv'
print(load_csv(filename))

# Uppgift 2
filename = 'CO2Emissions_filtered.csv'
lexicon1 = load_csv(filename)   # Anropar funktionen för att få ett lexikon
time = list(range(1960, 2015))      # Bestämmer tidsintervall
countrycodes = ['dnk', 'fin', 'isl', 'nor', 'swe']  # namn för de nordiska länderna
colors = ['red', 'blue', 'green', 'purple', 'orange']   # färg för länderna
fig, ax = plt.subplots()    # Skapar en figur med axlar
for i, j in zip(countrycodes, colors):      # Plottar kurvorna med landets färg
    ax.plot(time, lexicon1[i], j, linestyle=':')
    ax.plot(time, smooth_a(lexicon1[i], 5), j, label=i)
ax.set(xlabel='År', ylabel='Co2 Utsläpp (kT)', title='Årliga Co2 utsläpp i norden')     # Titel och axlar
ax.grid()   # slår på rutmönster
ax.legend()     # visar vilken färg som hör till vilket land
plt.show()  # Visar figuren

# Uppgift 3
file2 = open('uppsala_tm_1722-2020.dat', 'r')   # Öppnar filen
text = file2.read()     # Läser filen
rows = text.splitlines()    # Delar upp i rader
# Listor för medeltemperatur under varje århundrade
avg1700 = []
avg1800 = []
avg1900 = []
avg2000 = []
listavg = [avg1700, avg1800, avg1900, avg2000]  # samlar temperaturerna
tvalue = [2418, 3100, 3100, 620]    # 31 dagar i maj, dvs 78*31, 100*31, 100*31, 20*31
start = 1722    # Start år
end = 1800      # Slut år för första cykeln

h = 0   # Används för att cykla tvalue
k = 0   # används för att cykla listavg
for r in range(4):  # Upprepar 4 ggr, en gång för varje sekel
    temp = []   # lista för temperaturerna
    t = 0
    for i in rows:      # Går igenom varje rad
        if start <= float(i[0:4]) <= end:   # Om året är mellan start och end
            if float(i[4:7]) == 5:      # Om det är maj månad
                temp.append(float(i[12:17]))    # Lägg till temperaturen till listan temp
    for i in temp:  # Går igenom listan med temperaturer
        while t < tvalue[h]:    # om räknaren t är mindre än värdet i tvalue
            x = round((sum(temp[t:t+31]))/31, 3)    # beräkna medelvärdet av temperaturen per år. (31 dagar i maj)
            listavg[k].append(x)    # Lägger till värdet i listan listavg
            t += 31     # adderar 31 till räknaren
    h += 1      # Cyklar till nästa element i tvalue
    k += 1      # Cyklar till nästa element i listavg
    start = end     # sätter startåret till slutåret
    end += 100  # Ökar slutåret med 100

fig, ax = plt.subplots()    # figur och axlar
fig.suptitle('Medeltemperaturer i maj', fontsize=14, fontweight='bold')
ax.boxplot(listavg)     # boxplot av temperaturerna från listavg
plt.xticks([1, 2, 3, 4], ['1700', '1800', '1900', '2000'])  # steglängd på x-axeln
ax.set_xlabel('Bergström, H., Moberg, A.: Daily air temperature and pressure series for\nUppsala (1722-1998), Climate Change, 53:213-252.', fontsize=8)
ax.set_ylabel('Temperaturer')
plt.show()