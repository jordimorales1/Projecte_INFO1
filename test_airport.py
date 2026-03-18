from airport import *
airport = Airport ("LEBL", 41.297445, 2.0832941 )
SetSchengen(airport)
PrintAirport (airport)
""" Test Pas 3
airports = LoadAirports("Airports.txt")
print(f"Aeroports carregats: {len(airports)}")
# Mostrem els 3 primers
for a in airports[:3]:
    SetSchengen(a)
    PrintAirport(a)
"""