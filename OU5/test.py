from fVehicleAndLane_Stud import Lane, Vehicle

v = Vehicle('S', 0)
l = Lane(5)
print(l.get_first)

x = l.get_first()
print(x.get_destination())

s = '10' + '(' + '10' + ') \t' + str('[......]') + str('G') + str('[......]') + \
            str('[......]') + "  " + '[]' + '\n\t\t' + str('[......]') + str('G') + str('[......]')

print(s)