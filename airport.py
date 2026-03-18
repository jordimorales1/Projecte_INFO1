#Pas 1

# Codis ICAO dels paisos de l'espai Schengen
SCHENGEN_PREFIXES = ['LO', 'EB', 'LK', 'LC', 'EK', 'EE', 'EF', 'LF', 'ED', 'LG', 'EH', 'LH',
    'BI', 'LI', 'EV', 'EY', 'EL', 'LM', 'EN', 'EP', 'LP', 'LZ', 'LJ', 'LE', 'ES', 'LS']

class Airport :
    def __init__(self, code, lat, lon):
        self.code = code
        self.lat = lat
        self.lon = lon
        self.schengen = False

def IsSchengenAirport(code):
    if code in SCHENGEN_PREFIXES :
        return True
    return False

def SetSchengen(airport):
    airport.schengen = IsSchengenAirport(airport.code)

def PrintAirport(airport):
    print("Codi ICAO : {airport.code")
    print("Latitud : {airport.lat}")
    print("Longitud : {airport.lon}")
    print("Schengen : {airport.schengen}")