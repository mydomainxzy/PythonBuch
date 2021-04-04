# Definition der Funktion
def steuer(x):
    if x > 2500:
        ergebnis = x*0.22
        return ergebnis
    else:
        ergebnis = x*0.18
        return ergebnis

# Hauptprogramm
print("Gehalt:", 1800, "€", "  Steuer:", steuer(1800), "€")
print("Gehalt:", 2200, "€", "  Steuer:", steuer(2200), "€")
print("Gehalt:", 2500, "€", "  Steuer:", steuer(2500), "€")
print("Gehalt:", 2900, "€", "  Steuer:", steuer(2900), "€")