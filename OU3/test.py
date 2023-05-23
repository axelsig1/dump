import keyword
import re


with open('kod.txt', 'r') as f:
    f = f.readlines()
    print(f)
    print('''
    Koden:
    ''')
    count = 1
    for line in f:
        print(str(count) + '\t' + line.rstrip('\n'))    # Skriver ut kod med radnummer
        count += 1

    words = {}
    line_dict = keyword.kwlist

    for lines in f:
        lines = re.sub(r'#.*$', '', lines)  # Tar bort kommentarer
        lines = re.sub('[^a-zA-Z]', ' ', lines)     # Tar bort tecken (+, =, ., osv)
        for x in line_dict:  # Går igenom listan med python-ord
            if x in lines.split():  # Om ordet är med i koden så ska det tas bort
                lines = lines.replace(x, '')
        for c in lines.split():  # Går igenom koden utan orden som inte ska vara med
            if c in words:  # Om ordet i koden är med i listan med ord ska ordets värde uppdateras
                words[c] += 1
            else:  # Annars ska ordet läggas till i listan och får värdet 1
                words[c] = 1


    reference = {word: [] for word in words}  # Skapar en lista för varje ord som också har en lista
    for num, line in enumerate(f, start=1):  # Går igenom varje rad i koden
        for word in words:
            if word in line:  # Om ordet från words är med i koden ska radnumret läggas till i minilistan i results
                reference[word].append(num)

print('''
Referenslista:
''')

for a in sorted(reference):  # Skriv ut referenslistan i alfabetisk ordning
        print("\t %s %s" % (a, reference[a]))

