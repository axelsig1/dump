import re

print('''
Koden: 
''')

words = {}      # Tom lista för att räkna ord
line_dict = {'for', 'if', 'in', 'def', 'else'}    # Lista med python-ord
for line in open('kod.txt', 'r'):   # Går igenom koden som ska skrivas ut
    line = re.sub(r'#.*$', ' ', line)    # Tar bort alla kommentarer från koden
    line = re.sub(r'[^\w]', ' ', line)  # Ersätter alla tecken (så som . , () [] = ) med mellanrum
    line = re.sub('[^a-zA-Z]', ' ', line)  # Tar bort alla icke-internationella bokstäver

    for x in line_dict:     # Går igenom listan med python-ord
        if x in line.split():   # Om ordet är med i koden så ska det tas bort
            line = line.replace(x, '')
    for c in line.split():  # Går igenom koden utan orden som inte ska vara med
        if c in words:      # Om ordet i koden är med i listan med ord ska ordets värde uppdateras
            words[c] += 1
        else:       # Annars ska ordet läggas till i listan och får värdet 1
            words[c] = 1

with open('kod.txt') as f:      # Öppnar text dokumentet med koden
    count = 1       # Radräknare börjar på 1
    for lines in f:     # För varje rad i programmet ska det skrivas ut radnummer och koden på raden
        print(str(count) + '\t' + lines.rstrip('\n'))
        count += 1      # Uppdaterar räknaren för radnummer

print('''
Referenslista: 
''')

with open('kod.txt') as f:      # Öppnar text dokumentet med koden
    reference = {word: [] for word in words}      # Skapar en lista för varje ord som också har en lista
    for num, line in enumerate(f, start=1):     # Går igenom varje rad i koden
        for word in words:
            if word in line:    # Om ordet från words är med i koden ska radnumret läggas till i minilistan i results
                reference[word].append(num)

for a in sorted(reference):     # Skriv ut referenslistan i alfabetisk ordning
    print("\t %s %s" % (a, reference[a]))
