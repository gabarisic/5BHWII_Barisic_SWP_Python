import unittest
from newpoker import generiere_deck, Karte, KartenDeck, hat_paar, hat_drilling, hat_flush, hat_strasse, hat_full_house, hat_vierling, hat_nur_high_card

class TestPokerFunctions(unittest.TestCase):

    def setUp(self):
        # Initialisiere ein Deck und Reihenfolge für Tests
        self.deck, self.werte_reihenfolge = generiere_deck()
        self.hand_paar = [Karte("2", "Herz"), Karte("2", "Karo"), Karte("4", "Pik"), Karte("7", "Kreuz"), Karte("8", "Karo")]
        self.hand_drilling = [Karte("3", "Herz"), Karte("3", "Karo"), Karte("3", "Kreuz"), Karte("9", "Pik"), Karte("10", "Herz")]
        self.hand_flush = [Karte("2", "Herz"), Karte("4", "Herz"), Karte("6", "Herz"), Karte("8", "Herz"), Karte("10", "Herz")]
        self.hand_strasse = [Karte("6", "Herz"), Karte("7", "Karo"), Karte("8", "Pik"), Karte("9", "Kreuz"), Karte("10", "Herz")]
        self.hand_full_house = [Karte("4", "Karo"), Karte("4", "Herz"), Karte("4", "Pik"), Karte("5", "Kreuz"), Karte("5", "Karo")]
        self.hand_vierling = [Karte("6", "Herz"), Karte("6", "Karo"), Karte("6", "Pik"), Karte("6", "Kreuz"), Karte("9", "Herz")]
        self.hand_high_card = [Karte("2", "Herz"), Karte("4", "Karo"), Karte("6", "Pik"), Karte("8", "Kreuz"), Karte("10", "Herz")]

    def test_generiere_deck(self):
        self.assertEqual(len(self.deck), 52)  # 52 Karten im Deck
        self.assertTrue(all(isinstance(karte, Karte) for karte in self.deck))  # Alle Elemente sind Karten

    def test_hat_paar(self):
        self.assertTrue(hat_paar(self.hand_paar))
        self.assertFalse(hat_paar(self.hand_high_card))

    def test_hat_drilling(self):
        self.assertTrue(hat_drilling(self.hand_drilling))
        self.assertFalse(hat_drilling(self.hand_paar))

    def test_hat_flush(self):
        self.assertTrue(hat_flush(self.hand_flush))
        self.assertFalse(hat_flush(self.hand_strasse))

    def test_hat_strasse(self):
        self.assertTrue(hat_strasse(self.hand_strasse, self.werte_reihenfolge))
        self.assertFalse(hat_strasse(self.hand_paar, self.werte_reihenfolge))

    def test_hat_full_house(self):
        self.assertTrue(hat_full_house(self.hand_full_house))
        self.assertFalse(hat_full_house(self.hand_paar))

    def test_hat_vierling(self):
        self.assertTrue(hat_vierling(self.hand_vierling))
        self.assertFalse(hat_vierling(self.hand_drilling))

    def test_hat_nur_high_card(self):
        self.assertTrue(hat_nur_high_card(self.hand_high_card, self.werte_reihenfolge))
        self.assertFalse(hat_nur_high_card(self.hand_paar, self.werte_reihenfolge))

    def test_karten_deck_ziehe_karten(self):
        karten_deck = KartenDeck(self.deck[:])
        gezogene_karten = karten_deck.ziehe_karten(5)
        self.assertEqual(len(gezogene_karten), 5)
        self.assertEqual(len(karten_deck.karten), 47) 

if __name__ == '__main__':
    unittest.main()
