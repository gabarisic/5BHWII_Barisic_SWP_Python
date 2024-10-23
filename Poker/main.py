import random

# Modellierung der Pokerkarten
FARBEN = ['Herz', 'Karo', 'Kreuz', 'Pik']
WERTE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']


class Karte:
    def __init__(self, wert, farbe):
        self.wert = wert
        self.farbe = farbe

    def __repr__(self):
        return f'{self.wert} von {self.farbe}'


class KartenDeck:
    def __init__(self):
        self.karten = [Karte(wert, farbe) for farbe in FARBEN for wert in WERTE]
        random.shuffle(self.karten)

    def ziehe_karten(self, anzahl=5):
        return [self.karten.pop() for _ in range(anzahl)]


def hat_paar(hand):
    werte = [karte.wert for karte in hand]
    for wert in werte:
        if werte.count(wert) == 2:
            return True
    return False


def hat_drilling(hand):
    werte = [karte.wert for karte in hand]
    for wert in werte:
        if werte.count(wert) == 3:
            return True
    return False


def hat_flush(hand):
    farben = [karte.farbe for karte in hand]
    return len(set(farben)) == 1


def hat_strasse(hand):
    wert_ordnung = {wert: i for i, wert in enumerate(WERTE)}
    werte = sorted([wert_ordnung[karte.wert] for karte in hand])
    return werte == list(range(werte[0], werte[0] + 5))


def hat_full_house(hand):
    werte = [karte.wert for karte in hand]
    paar_gefunden = False
    drilling_gefunden = False

    for wert in werte:
        anzahl = werte.count(wert)
        if anzahl == 2:
            paar_gefunden = True
        elif anzahl == 3:
            drilling_gefunden = True

    return paar_gefunden and drilling_gefunden


def hat_vierling(hand):
    werte = [karte.wert for karte in hand]
    for wert in werte:
        if werte.count(wert) == 4:
            return True
    return False


def hat_nur_high_card(hand):
    return not (hat_paar(hand) or hat_drilling(hand) or hat_flush(hand) or
                hat_strasse(hand) or hat_full_house(hand) or hat_vierling(hand))


# Simulation von 100.000 Pokerhänden
def simuliere_pokerspiele(anzahl_spiele=100000):
    kombinationen_zaehler = {
        'paar': 0, 'drilling': 0, 'flush': 0, 'strasse': 0,
        'full_house': 0, 'vierling': 0, 'high_card': 0
    }

    for _ in range(anzahl_spiele):
        deck = KartenDeck()
        hand = deck.ziehe_karten(5)

        # Prüfen, welche Pokerkombinationen in der Hand vorliegen
        if hat_paar(hand):
            kombinationen_zaehler['paar'] += 1
        if hat_drilling(hand):
            kombinationen_zaehler['drilling'] += 1
        if hat_flush(hand):
            kombinationen_zaehler['flush'] += 1
        if hat_strasse(hand):
            kombinationen_zaehler['strasse'] += 1
        if hat_full_house(hand):
            kombinationen_zaehler['full_house'] += 1
        if hat_vierling(hand):
            kombinationen_zaehler['vierling'] += 1
        if hat_nur_high_card(hand):
            kombinationen_zaehler['high_card'] += 1

    return kombinationen_zaehler


def berechne_prozentsaetze(zaehler, gesamt_spiele):
    return {kombination: round((anzahl / gesamt_spiele) * 100, 2) for kombination, anzahl in zaehler.items()}


# Simulation und Berechnung der Wahrscheinlichkeiten
kombinationen_zaehler = simuliere_pokerspiele()
prozentsaetze = berechne_prozentsaetze(kombinationen_zaehler, 100000)

print("Häufigkeit der Kombinationen nach 100.000 Spielen:")
print(kombinationen_zaehler)
print("\nProzentuale Häufigkeit der Kombinationen:")
print(prozentsaetze)
