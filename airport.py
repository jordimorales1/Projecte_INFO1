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
    if code[:2] in SCHENGEN_PREFIXES : #el code[:2] selecciona només els 2 primers caracters del codi ICAO
        return True
    return False

def SetSchengen(airport):
    airport.schengen = IsSchengenAirport(airport.code)

def PrintAirport(airport):
    print(f"Codi ICAO : {airport.code}")
    print(f"Latitud : {airport.lat}")
    print(f"Longitud : {airport.lon}")
    print(f"Schengen : {airport.schengen}")


#per acabar de pulir Pas 3
def LoadAirports(filename):
    ap = []

    F = open(filename, 'r')
    lines = F.readlines()
    """
    if filename not found : 
        print(f"No s'ha trobat el fitxer {filename}")
        return ap
    """

    for line in lines[1:]:
        line = line.strip()
        parts = line.split()
        code = parts[0]
        """
        S'han de passar a graus decimals
        """
        lat = parts[1]
        lon = parts[2]
        airport = Airport(code, lat, lon)
        ap.append(airport)
    return ap



