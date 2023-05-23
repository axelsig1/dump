# Studentversion av filen.
# Givet Ã¤r ett skal till klassen Light
# och kod (funktionen demo_light) som testar klassen Light.
# Fyll i det som saknas i klassen Light sÃ¥ att utskriften nedan fÃ¥s.

# Uppgift 2
class Light:
    """Representerar ett trafikljus"""

    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.step_counter = 0

    def step(self):
        # Stegar den interna klockan
        step = self.step_counter % self.period  # Step cyklar mellan 0 och self.period
        return step

    def is_green(self):
        # Kontrollerar om ljuset är grönt
        if 0 <= self.step() < self.green_period:    # Om step() är i intervallet är ljuset grönt,
            return True     # Då returnerar True
        else:
            return False    # Annars returneras False

    def __str__(self):
        # Sträng representation av trafikljuset
        if self.is_green() is True:     # Om ljuset är grönt
            self.step_counter += 1  # uppdateras räknaren
            return f'(G)'   # returnerar (G)
        else:   # Annars
            self.step_counter += 1  # uppdateras räknaren
            return f'(R)'   # och den returnerar (F)


def demo_light():
    """För demonstration av klassen Light"""
    a_light = Light(7, 3)  # Skapa ett trafikljus, period 7, green time 3
    # Simulera 15 tidssteg
    for t in range(15):
        print(t + 1, a_light, a_light.is_green())
        a_light.step()  # Nästa steg för trafikljuset


def main():
    print('\nLight demonstration')
    demo_light()


if __name__ == '__main__':  # If this file is the main program, you are running:
    main()  # Call the main function above

# When the Python interpreter reads a python file, it defines
# the special variable __name__
# If you are running your module as the main program,
# the interpreter will assign the hard-coded string "__main__" to the __name__ variable
# If this python file is demo_light() imported by another program, and they run that program, the
# main function is not called

""" När man kör denna kod skall följande hända:
Light demonstration
1 (G) True
2 (G) True
3 (G) True
4 (R) False
5 (R) False
6 (R) False
7 (R) False
8 (G) True
9 (G) True
10 (G) True
11 (R) False
12 (R) False
13 (R) False
14 (R) False
15 (G) True
"""