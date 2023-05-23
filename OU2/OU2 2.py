# OU2 2)
# Jämna ut en lista genom att hitta medelvärdet av x_i och de 2n närmsta talen.
# Vid kanterna antar man att listan förlängs med kantvärdet

def smooth_a(x, n):     # Funktionen jämnar ut en lista
    x = [x[0]]*n + x + [x[-1]]*n    # Förlänger listan med n gånger första elementet och n gånger sista elementet
    r = []              # Skapar en ny lista
    for i in range(n, len(x)-n):        # För varje element i den ursprungliga listan x ska:
        r.append(sum(x[i-n:i+n+1])/(2*n+1))     # medelvärdet av de 2n närmaste elementen beräknas och läggas in i r
    return r


# OU2 3)
# Avrunda alla tal i en lista till ett visst antal decimaler.

def round_list(a_list, ndigits):    # Funktionen avrundar talen i en lista till ndigits decimaler.
    new_list = [round(i, ndigits) for i in a_list]  # Skapar en ny lista och avrundar varje elementen i listan till n
                                                    # decimaler
    return new_list


# Kod för att testa 2) och 3)
x = [1, 2, 6, 4, 5, 0, 1, 2]    # Listan som ska jämnas ut
print(x)                # Skriver ut listan x
print(smooth_a(x, 1))   # Skriver ut den utjämnade listan med n = 1
print(smooth_a(x, 2))   # Skriver ut den utjämnade listan med n = 2
print(round_list(smooth_a(x, 1), 2))    # Skriver ut den utjämnade listan med n = 1 avrundat till 2 decimaler.


