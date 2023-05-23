# Given studentversion av:
# Trafik system 1
# Två filer (lane1, lane2) och ett trafikljus (light) mellan dem.
# Och en kö, före lane2..
# lane1 - light - lane2 - kö
# Uppgift:
# I klassen TrafficSystem1 skall metoden number_in_system()
# modifieras.

from fVehicleAndLane_Stud import Lane, Vehicle
from fLight_Stud import Light
from fDestinations import Destinations
from time import sleep  # behövs för sleep-fkn
import statistics


class TrafficSystem2:
    """Representerar ett trafik system"""

    # Konstruktorn
    def __init__(self, lane_length, lanews_length, light_period, west_green, south_green):
        self.time = 0  # Tiden är noll, initialt
        self.lane = Lane(lane_length)  # Fil innan uppdelning
        self.lane_west1 = Lane(5)  # Fil west efter signal
        self.lane_west2 = Lane(lanews_length)   # Fil west innan signal
        self.lane_south1 = Lane(5)   # Fil south efter signal
        self.lane_south2 = Lane(lanews_length)  # Fil south innan signal
        self.light_west = Light(light_period, west_green)  # Trafikljus west, period 10, green period 8
        self.light_south = Light(light_period, south_green)     # Trafikljus south, period 10, green period 8
        self.queue = []  # Kön längst till höger är initialt tom
        self.generator = Destinations()  # skapar ett Destinations-objekt
        self.block = ' '
        self.block_count = 0    # räknar hur många gånger filen blockeras
        self.queue_count = 0    # Räknar hur många bilar som hamnar i queue filen
        self.time_west = []     # Tiden för olika bilar att passerar light_west
        self.time_south = []

    # Skriver ut trafiksystemet vid aktuell tid som exvis
    #   26: [WSSSW](G)[SWWSW]  ['W', 'S']
    # dvs tiden, filen efter trafikljuset, trafikljuset, filen framför trafikljuset, kön
    def snapshot(self):
        # Skapa en sträng som representerar kön
        sq = str([x.get_destination() for x in self.queue])
        # Skapa en sträng med värdet på self.time högerjusterat över 4 positioner
        stime = '%4d' % self.time + ": "
        snr = '%2d' % (self.number_in_system())
        # Bygg upp strängen med alla dess beståndsdelar
        s = stime + '(' + snr + ') \t' + str(self.lane_west1) + str(self.light_west) + str(self.lane_west2) \
            + str(self.block) + str(self.lane) + "  " + sq + '\n\t\t\t' + str(self.lane_south1) + \
            str(self.light_south) + str(self.lane_south2)
        print(s)

    # Stegar trafiksystemet från vänster till höger
    def step(self):
        self.time += 1  # Uppdatera tiden
        self.lane_west1.remove_first()  # Tar bort fordon först i lane_west1
        self.lane_south1.remove_first()
        self.lane_west1.step()  # Stega lane_west1
        self.lane_south1.step()

        if self.light_west.is_green():  # Om trafikljuset west är grönt...
            firstW = self.lane_west2.get_first()    # hämtar första bilen i kön
            if firstW != None:  # Används för statistiken, Om det är en bil längst fram
                self.time_west.append(self.time - firstW.get_borntime())    # tid det tog att passera ljuset i listan
            self.lane_west1.enter(self.lane_west2.remove_first())   # Flytta trafik från lane_west2 till lane_west1
        self.light_west.step()  # Stega trafikljuset west
        self.lane_west2.step()  # Stega lane_west2
        # Samma som ovan fast för south
        if self.light_south.is_green():
            firstS = self.lane_south2.get_first()
            if firstS != None:
                self.time_south.append(self.time - firstS.get_borntime())
            self.lane_south1.enter(self.lane_south2.remove_first())
        self.light_south.step()
        self.lane_south2.step()

        if self.lane.get_first() != None:   # Om det första objektet i lane är en bil:
            if self.lane.get_first().get_destination() == 'W':  # Om bilen ska till W:
                if self.lane_west2.last_free():     # Kolla om filen är ledig och flytta till filen
                    self.lane_west2.enter(self.lane.remove_first())
                    self.block = ' '
                else:
                    self.block = '*'    # Om det inte är ledigt skriv ut '*' mellan filerna
                    self.block_count += 1   # Uppdatera räknaren
            # Samma som ovan fast för south
            elif self.lane.get_first().get_destination() == 'S':    # Annars om bilen ska till S
                if self.lane_south2.last_free() is True:    # Kolla om filen är ledig och flytta til filen
                    self.lane_south2.enter(self.lane.remove_first())
                    self.block = ' '
                else:
                    self.block = '*'
                    self.block_count += 1
        self.lane.step()    # Stega lane

        # Nytt fordon vid detta tidssteg?
        destination = self.generator.step()  # Ger S, W eller None från generatorn
        if destination is not None:  # Om nytt fordon:
            # Skapa fordonet och lägg det sist i kön
            self.queue.append(Vehicle(destination, self.time))
            #if self.lane.last_free() is False:  # Om filen är full ska bilen hamna i queue:
             #   self.queue_count += 1   # uppdatera queue räknaren

        # Om det finns minst ett fordon i kön OCH sista positionen i lane2 är ledig:
        if len(self.queue) > 0 and self.lane.last_free():
            # Flytta fordonet från första position i kön till sista position i lane2.
            self.lane.enter(self.queue.pop(0))

        if len(self.queue) > 0:
            self.queue_count += 1

    # Beräknar och returnerar hur många fordon som för tillfället finns i trafikssystemet
    # dvs summan av fordon i alla filer och kön innan trafikljuset.
    def number_in_system(self):
        number_in_system = 0       # Lista med antal bilar i systemet
        for road in [str(self.lane_west2), str(self.lane_south2),
                     str(self.lane), self.queue]:
            if type(road) == str:   # Om road är av typen str
                road = road[1:-1]   # Ta bort '[' och ']' från road
                road = list(road)   # Gör road till en lista
            for x in range(len(road)):  # Lägg till alla forden som är i filen till listan
                if road[x] == '.':
                    pass
                else:
                    number_in_system += 1
        return number_in_system  # Beräkna och returnera längd på listan

    def print_statistics(self):
        # summan av bilar som har passerat och bilar som är i systemet
        total_vehicle = len(self.time_west) + len(self.time_south) + self.number_in_system()
        outW = len(self.time_west)  # Hur många bilar har passerat west
        outS = len(self.time_south)

        if outW != 0:   # Om bilar har passerat west
            minW = min(self.time_west)  # Minsta antal steg att ta sig igenom
            maxW = max(self.time_west)  # Flest antal steg att ta sig igenom
            meanW = round(statistics.fmean(self.time_west), 1)  # Beräkna medelvärdet med 1 decimal
            medianW = statistics.median(sorted(self.time_west))     # Hitta medianen
        else:   # Om inga bilar har tagit sig igenom är allt 0
            minW = 0
            maxW = 0
            meanW = 0
            medianW = 0

        # Samma som ovan fast för south
        if outS != 0:
            maxS = max(self.time_south)
            minS = min(self.time_south)
            meanS = round(statistics.fmean(self.time_south), 1)
            medianS = statistics.median(sorted(self.time_south))
        else:
            minS = 0
            maxS = 0
            meanS = 0
            medianS = 0

        return f'{self.time_west}\n' \
               f'{self.time_south}\n' \
               f'Statistics after {self.time} timesteps: \n \nCreated vehicles:\t{total_vehicle}' \
               f'\nIn system:\t{self.number_in_system()}' \
               f'\n\nAt exit\t\t\tWest\tSouth' \
               f'\nVehicles out:\t{outW}\t\t{outS}' \
               f'\nMinimal time:\t{minW}\t\t{minS}' \
               f'\nMaximal time:\t{maxW}\t\t{maxS}' \
               f'\nMean time:\t\t{meanW}\t{meanS}' \
               f'\nMedian time:\t{medianW}\t{medianS}' \
               f'\n\nBlocked:\t{round(100 * self.block_count/self.time, 1)}%' \
               f'\nQueue:\t\t{round(100 * self.queue_count/self.time, 1)}%'


# Funktion som testkör TrafficSystem2
def main():
    lane_length = 11  # Length first (rightmost) lane
    lanews_length = 8  # Length lanes in front of signals
    light_period = 14  # Period for the lights
    west_green = 6  # Green period westbound light
    south_green = 4  # Green period southbound light
    ts = TrafficSystem2(lane_length, lanews_length, light_period, west_green, south_green)
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)  # Vänta 100 ms
    print('\nFinal state:')
    ts.snapshot()
    print(ts.print_statistics())


# Testkör main
if __name__ == '__main__':
    main()
