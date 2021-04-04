print("Geben Sie Ihr monatliches Gehalt ein:")

z = input()
zahl = int(z)
m = zahl*0.22
l = zahl*0.18

if zahl > 2500:
    print("Es ergibt sich eine Steuer von",m ,"Euro")
else:
    print("Es ergibt sich eine Steuer von",l ,"Euro")