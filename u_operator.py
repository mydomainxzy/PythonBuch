print("Geben sie an ob sie unverheiratet (mit der 1) oder verheiratet (mit der 2) sind:")
x = input()
xint = int(x)

print("Geben sie ihr monatliches Gehalt ein:")
z = input()
zint = int(z)

if xint == 1 and zint > 4000:
    print("Ihr Steuersatz beträgt", zint*0.26,"Euro")
elif xint == 1 and zint <= 4000:
    print("Ihr Steuersatz beträgt", zint*0.22,"Euro")
elif xint == 2 and zint > 4000:
    print("Ihr Steuersatz beträgt", zint*0.22,"Euro")
elif xint == 2 and zint <= 4000:
    print("Ihr Steuersatz beträgt", zint*0.18,"Euro")
