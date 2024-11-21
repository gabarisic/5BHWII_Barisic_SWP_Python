import random
def generiere_deck():
    farben = ['Herz', 'Karo', 'Kreuz', 'Pik']
    werte = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    return [Karte(wert, farbe) for farbe in farben for wert in werte], werte

class Karte:
    def __init__(self, wert, farbe):
        self.wert = wert
        self.farbe = farbe

    def __repr__(self):
        return f'{self.wert} von {self.farbe}'

class KartenDeck:
    def __init__(self, karten):
        self.karten = karten
        random.shuffle(self.karten)

    def ziehe_karten(self, anzahl):
        return [self.karten.pop() for _ in range(anzahl)]

def hat_paar(hand):
    werte = [karte.wert for karte in hand]
    return any(werte.count(wert) == 2 for wert in werte)

def hat_drilling(hand):
    werte = [karte.wert for karte in hand]
    return any(werte.count(wert) == 3 for wert in werte)

def hat_flush(hand):
    farben = [karte.farbe for karte in hand]
    return len(set(farben)) == 1

def hat_strasse(hand, werte_reihenfolge):
    wert_ordnung = {wert: i for i, wert in enumerate(werte_reihenfolge)}
    werte = sorted([wert_ordnung[karte.wert] for karte in hand])
    return werte == list(range(werte[0], werte[0] + 5))

def hat_full_house(hand):
    werte = [karte.wert for karte in hand]
    paar_gefunden = any(werte.count(wert) == 2 for wert in set(werte))
    drilling_gefunden = any(werte.count(wert) == 3 for wert in set(werte))
    return paar_gefunden and drilling_gefunden

def hat_vierling(hand):
    werte = [karte.wert for karte in hand]
    return any(werte.count(wert) == 4 for wert in werte)

def hat_nur_high_card(hand, werte_reihenfolge):
    return not (hat_paar(hand) or hat_drilling(hand) or hat_flush(hand) or
                hat_strasse(hand, werte_reihenfolge) or hat_full_house(hand) or hat_vierling(hand))

def simuliere_pokerspiele(anzahl_spiele, werte_reihenfolge):
    kombinationen_zaehler = {
        'paar': 0, 'drilling': 0, 'flush': 0, 'strasse': 0,
        'full_house': 0, 'vierling': 0, 'high_card': 0
    }
    deck, _ = generiere_deck()
    for _ in range(anzahl_spiele):
        karten_deck = KartenDeck(deck[:])
        hand = karten_deck.ziehe_karten(5)

        if hat_paar(hand):
            kombinationen_zaehler['paar'] += 1
        if hat_drilling(hand):
            kombinationen_zaehler['drilling'] += 1
        if hat_flush(hand):
            kombinationen_zaehler['flush'] += 1
        if hat_strasse(hand, werte_reihenfolge):
            kombinationen_zaehler['strasse'] += 1
        if hat_full_house(hand):
            kombinationen_zaehler['full_house'] += 1
        if hat_vierling(hand):
            kombinationen_zaehler['vierling'] += 1
        if hat_nur_high_card(hand, werte_reihenfolge):
            kombinationen_zaehler['high_card'] += 1
    return kombinationen_zaehler

def berechne_prozentsaetze(zaehler, gesamt_spiele):
    return {kombination: f"{(anzahl / gesamt_spiele) * 100:.2f}%" for kombination, anzahl in zaehler.items()}

def main():
    anzahl_spiele = int(input("Geben Sie die Anzahl der zu simulierenden Spiele ein: "))
    deck, werte_reihenfolge = generiere_deck()
    kombinationen_zaehler = simuliere_pokerspiele(anzahl_spiele, werte_reihenfolge)
    prozentsaetze = berechne_prozentsaetze(kombinationen_zaehler, anzahl_spiele)

    print("Häufigkeit der Kombinationen:")
    print(kombinationen_zaehler)
    print("\nProzentuale Häufigkeit der Kombinationen:")
    print(prozentsaetze)

if __name__ == "__main__":
    main()



