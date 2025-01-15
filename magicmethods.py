class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)):
            raise ValueError("PS muss eine Zahl sein.")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Addition ist nur zwischen zwei Auto-Objekten erlaubt.")
        return Auto(self.ps + other.ps)

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Subtraktion ist nur zwischen zwei Auto-Objekten erlaubt.")
        return Auto(self.ps - other.ps)

    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Multiplikation ist nur zwischen zwei Auto-Objekten erlaubt.")
        return Auto(self.ps * other.ps)

    def __eq__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps > other.ps

    def __len__(self):
        return int(self.ps)

    def __repr__(self):
        return f"Auto({self.ps} PS)"

# Testfälle
if __name__ == "__main__":
    # Auto-Objekte erstellen
    a1 = Auto(50)
    a2 = Auto(60)

    # Addition
    a3 = a1 + a2
    print(a3)  # Erwartet: Auto(110 PS)

    # Subtraktion
    a4 = a2 - a1
    print(a4)  # Erwartet: Auto(10 PS)

    # Multiplikation
    a5 = a1 * a2
    print(a5)  # Erwartet: Auto(3000 PS)

    # Vergleichsoperationen
    print(a1 == a2)  # Erwartet: False
    print(a1 < a2)   # Erwartet: True
    print(a1 > a2)   # Erwartet: False

    # len()-Funktion
    print(len(a1))   # Erwartet: 50
    print(len(a2))   # Erwartet: 60

    # Ungültige Operationen
    try:
        print(a1 + 10)  # Erwartet: TypeError
    except TypeError as e:
        print(e)

    try:
        print(a1 - "test")  # Erwartet: TypeError
    except TypeError as e:
        print(e)
