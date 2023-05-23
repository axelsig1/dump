import itertools
import re


def part2(x):
    return x[1]     # returnerar andra objektet i listan


filnamn = input('Ange filens namn: ')   # Ber användaren att ange filens namn
n = int(input('Hur många av de vanligaste bokstäverna ska visas?: '))   # Mata in hur många av de vanligaste ska visas
m = int(input('Hur många av de ovanligaste bokstäverna ska visas?: '))  # Mata in hur många av de ovanligaste ska visas
print()

with open(filnamn, 'r') as f:       # Öppnar filen
    text = f.read()     # Läser hela filen som en str
    print(text)     # Skriver ut hela filen
    text_list = re.findall(r'[a-zA-ZåäöÅÄÖ]+', text)    # Skapar en lista med alla ord i texten
    word_count = len(text_list)     # Beräknar längden av text_list, dvs alla ord i listan.
    print()
    print(f'Antal ord: ', word_count)   # Skriver ut alla ord

    unique_words = {}   # Skapar en tom lista för unika ord
    for i in text_list:     # Går igenom listan med ord
        if i in unique_words:   # Om ordet finns i listan för unika ord görs inget
            pass
        else:       # Om ordet inte finns med i listan kommer det läggas till i listan
            unique_words[i] = 1
    print('Antal unika ord:', len(unique_words))    # Beräknar och skriver ut längden på listan med unika ord
    print()

    txt = [c.lower() for c in text_list]    # Skapar en ny lista med där alla bokstäver är små
    freq = {}   # Skapar en tom lista för förekomsten av orden.
    for word in txt:    # Går igenom listan med ord
        if word in freq:    # Om ordet finns med i listan för ordens frekvens kommer den addera 1
            freq[word] += 1
        else:       # Annars kommer ordet läggas till i listan och få värdet 1
            freq[word] = 1

    freq_list = list(freq.items())      # Skapar en lista med alla objekt från freq, dvs [('det', 3), ('var', 5), ...]
    for a in [n, m]:    # Går igenom loopen en gång för n och en gång för m. (Värdena på hur många ord som ska visas)
        if a == n:      # Om a = n ska de vanligaste orden skrivas ut
            print('De', a, 'vanligaste orden är: ')
            freq_order = sorted(freq_list, key=part2, reverse=True)     # Sorterar listan störst till minst
        else:       # annars ska de ovanligaste orden skrivas ut
            freq_order = sorted(freq_list, key=part2, reverse=False)    # Sorterar listan minst till störst
            print('De', m, 'ovanligaste orden är: ')

        for i, e in enumerate(itertools.islice(freq_order, a), start=1):    # Går igenom listan, skriver ut a st objekt
            print(f'{e[1]:2d} {e[0]}', end='\t')  # Skriver siffran för ordet samt ordet. TAB efter varje utskrift
            if i % 6 == 0:  # Radbrytning var 6:e utskrift
                print()
        print()
