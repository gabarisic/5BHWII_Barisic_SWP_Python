import sys
class Fahrzeuge:
    def __init__(self, marke, modell, baujahr):
        # Neuer Fehler, NICHT behebar
        if not marke or not modell or not isinstance(baujahr, int):
            raise ValueError("Marke, Modell und Baujahr müssen gültig sein.")
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def __str__(self):
        return f"{self.marke} {self.modell} aus dem Jahr {self.baujahr}"


class Auto(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, turen):
        super().__init__(marke, modell, baujahr)
        # Neuer Fehler, behebar
        if turen <= 0:
            raise ValueError("Die Anzahl der Türen muss positiv sein.")
        self.turen = turen

    def __str__(self):
        return f"{super().__str__()} mit {self.turen} Türen"


class Motorrad(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, ps):
        super().__init__(marke, modell, baujahr)
        # Hochgeblubberter Fehler, behebar
        if ps <= 0:
            raise ValueError("PS-Wert muss positiv sein.")
        self.ps = ps

    def __str__(self):
        return f"{super().__str__()} mit {self.ps} PS"


class Fahrrad(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, art):
        super().__init__(marke, modell, baujahr)
        # Hochgeblubberter Fehler, NICHT behebar
        if art not in ["Mountainbike", "Rennrad", "Citybike"]:
            raise ValueError(f"Unbekannte Fahrradart: {art}")
        self.art = art

    def __str__(self):
        return f"{super().__str__()}, Typ: {self.art}"


def my_cli():
    try:
        # Neuer Fehler, behebar
        auto = Auto("Audi", "RS7", 2020, 4)
        print(auto)

        # Hochgeblubberter Fehler, behebar
        try:
            motorrad = Motorrad("Yamaha", "MT-07", 2019, -215)
        except ValueError as e:
            print(f"Fehler bei der Erstellung eines Motorrads: {e}")
            motorrad = Motorrad("Yamaha", "MT-07", 2019, 215)  # Fehler wird behoben
        print(motorrad)

        # Hochgeblubberter Fehler, NICHT behebar
        try:
            fahrrad = Fahrrad("Cube", "Stereo", 2022, "Unbekannt")
        except ValueError as e:
            print(f"Fehler bei der Erstellung eines Fahrrads: {e}")
            fahrrad = None  # Kann nicht behoben werden
        if fahrrad:
            print(fahrrad)

    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        my_cli()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
