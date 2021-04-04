print("Geben Sie Ihr monatliches Gehalt ein:")

z = input()
zahl = int(z)
m = zahl*0.26
l = zahl*0.22
p = zahl*0.18

if zahl > 4000:
    print("Es ergibt sich eine Steuer von",m ,"Euro")
elif zahl < 2500:
    print("Es ergibt sich eine Steuer von",p ,"Euro")
else:
    print("Es ergibt sich eine Steuer von",l , "Euro")
