import random


# OU2 1a)
# Skapa en funktion som fungera som remove() kommandot.
# Koden ska skapa en lista med 10 slumpade tal. Sedan ska delete() användas för att ta bort ett tal ur listan
def delete(my_list, number):
    if number in my_list:   # Kollar om number finns med i listan.
        my_list.pop(my_list.index(number))      # Om det finns ska funktionen hitta talets index och använda pop för att ta bort talet ur listan


list = []   # Skapar en tom lista
for i in range(10):             # Lägger till 10 slumpade tal till listan
    list.append(random.randint(0, 10))
print(list)         # Listan innan delete()
delete(list, 10)
print(list)         # Listan efter delete()

# OU2 1b)
# Nu ska listan tömmas genom att slumpa tal mellan 0 och 10. Programmet ska räkna hur många iterationer det tog att töma listan
x = 0       # Räknare
while len(list):        # Medans listan har något innehåll
    a = random.randint(0, 10)   # Slumpa ett tal mellan 0 och 10
    delete(list, a)     # Ta bort det slumpade talet från listan
    x += 1          # Uppdatera räknaren

print('Det tog', x, 'iterationer att tömma listan')
print(list)     # Används för att testa