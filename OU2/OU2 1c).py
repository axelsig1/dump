def delete(the_list, number):
    new_list = []
    for n in the_list:
        if n == number:
            continue
        new_list.append(n)
    the_list = new_list     # Här får listan ett nytt lokalt värde som bara gäller i funktionen
    print('listan i delete', the_list)      # I funktionen tas 7an bort, men inte utanför


my_list = [2, 5, 1, 7, 12, 0, -5]       # Global variabel (lista)
print('my_list före delete', my_list)
delete(my_list, 7)      # Värdet från funktionen måste sparas som en global variabel
                        # Ex) x = delete(my_list, 7)
                        # Därefter kan den variabeln anropas som print('Listan efter delete', x)
print('my_list efter delete', my_list)      # 7an tas inte bort från den globala variabeln (listan)