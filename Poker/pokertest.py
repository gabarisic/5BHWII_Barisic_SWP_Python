import unittest
from newpoker import Karte, hat_paar, hat_flush, generiere_deck

class TestPokerKombinationen(unittest.TestCase):
    def setUp(self):
        self.deck, self.werte_reihenfolge = generiere_deck()

    def test_hat_paar(self):
        hand = [Karte('2', 'Herz'), Karte('2', 'Karo'), Karte('3', 'Kreuz'), Karte('4', 'Pik'), Karte('5', 'Herz')]
        self.assertTrue(hat_paar(hand))

    def test_hat_flush(self):
        hand = [Karte('2', 'Herz'), Karte('3', 'Herz'), Karte('4', 'Herz'), Karte('5', 'Herz'), Karte('6', 'Herz')]
        self.assertTrue(hat_flush(hand))


if __name__ == "__main__":
    unittest.main()