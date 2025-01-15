class Fahrzeuge:
    def __init__(self, marke, modell, baujahr):
        if not marke or not modell or not isinstance(baujahr, int):
            raise ValueError("Marke, Modell und Baujahr müssen gültig sein.")  # Neuer Fehler, nicht behebar
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def __str__(self):
        return f"{self.marke} {self.modell} aus dem Jahr {self.baujahr}"


class Auto(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, turen):
        super().__init__(marke, modell, baujahr)
        if turen <= 0:
            raise ValueError("Die Anzahl der Türen muss positiv sein.")  # Neuer Fehler, behebar
        self.turen = turen

    def __str__(self):
        return f"{super().__str__()} mit {self.turen} Türen"


class Motorrad(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, ps):
        super().__init__(marke, modell, baujahr)
        if ps <= 0:
            raise ValueError("PS-Wert muss positiv sein.")  # Hochgeblubberter Fehler, behebar
        self.ps = ps

    def __str__(self):
        return f"{super().__str__()} mit {self.ps} PS"


class Fahrrad(Fahrzeuge):
    def __init__(self, marke, modell, baujahr, art):
        super().__init__(marke, modell, baujahr)
        if art not in ["Mountainbike", "Rennrad", "Citybike"]:
            raise ValueError(f"Unbekannte Fahrradart: {art}")  # Hochgeblubberter Fehler, nicht behebar
        self.art = art

    def __str__(self):
        return f"{super().__str__()}, Typ: {self.art}"


if __name__ == "__main__":
    try:
        auto = Auto("Audi", "RS7", 2020, 4)
        try:
            motorrad = Motorrad("Yamaha", "MT-07", 2019, -215)  # Hochgeblubberter Fehler, behebar
        except ValueError as e:
            print(f"Fehler bei der Erstellung eines Motorrads: {e}")

        try:
            fahrrad = Fahrrad("Cube", "Stereo", 2022, "Unbekannt")  # Hochgeblubberter Fehler, nicht behebar
        except ValueError as e:
            print(f"Fehler bei der Erstellung eines Fahrrads: {e}")

        # Ausgabe der Fahrzeuge
        print(auto)
        # motorrad und fahrrad werden nur ausgegeben, wenn sie korrekt erstellt wurden
        if 'motorrad' in locals():
            print(motorrad)
        if 'fahrrad' in locals():
            print(fahrrad)

    except Exception as error:
        print(f"Unerwarteter Fehler: {error}")  # Hochgeblubberter Fehler, nicht behebar