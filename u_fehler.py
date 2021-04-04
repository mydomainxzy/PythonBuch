fehler = 1

while fehler == 1:
    print("Bitte eine Zahl eingeben:")
    z=input()
    try:
        zahl=int(z)
        print(zahl,"Inch gibt", zahl*2.45,"Cm")
        fehler = 0
    except:
        print("Sie haben keine ganze Zahl angegeben")
        fehler = 1

print("Ende des Programms")