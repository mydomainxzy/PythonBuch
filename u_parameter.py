# Definition der Funktion
def steuer(x):
    if x > 2500:
        print("Gehalt:", x,"€", "  Steuer:", x*0.22,"€")
    else:
        print("Gehalt:", x,"€", "  Steuer:", x*0.18,"€")

# Hauptprogramm
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)