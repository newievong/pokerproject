import unittest
import poker


class MyTestCase(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(poker.check_straight('S4', 'S5', 'S6'), 6)
        self.assertEqual(poker.check_straight('S6', 'S5', 'S4'), 6)
        self.assertEqual(poker.check_straight('SJ', 'SQ', 'S8'), 0)
        self.assertEqual(poker.check_straight('S10', 'S4', 'S7'), 0)
        self.assertEqual(poker.check_straight('S10', 'S9', 'S8'), 10)
        self.assertEqual(poker.check_straight('S2', 'S5', 'SJ'), 0)
        self.assertEqual(poker.check_straight('SQ', 'S4', 'S6'), 0)


    def test_check_3ofa_kind(self):
        self.assertEqual(poker.check_3ofa_kind('S5', 'S5', 'S5'), 5)
        self.assertEqual(poker.check_3ofa_kind('S4', 'S10', 'S3'), 0)
        self.assertEqual(poker.check_3ofa_kind('SQ', 'SQ', 'SQ'), 12)
        self.assertEqual(poker.check_3ofa_kind('S8', 'S2', 'S8'), 0)
        self.assertEqual(poker.check_3ofa_kind('S3', 'SK', 'S6'), 0)
        self.assertEqual(poker.check_3ofa_kind('S2', 'S4', 'S8'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(poker.check_royal_flush('SQ', 'SK', 'SA'), 14)
        self.assertEqual(poker.check_royal_flush('S5', 'SJ', 'SQ'), 0)
        self.assertEqual(poker.check_royal_flush('SK', 'SA', 'SQ'), 14)
        self.assertEqual(poker.check_royal_flush('S10', 'SJ', 'SQ'), 0)
        self.assertEqual(poker.check_royal_flush('S2', 'S7', 'S10'), 0)
        self.assertEqual(poker.check_royal_flush('S4', 'SK', 'SA'), 0)


    def test_play_cards(self):
        self.assertEqual(poker.play_cards('S2', 'S2', 'S2', 'S5', 'S5', 'S5'), 1)
        self.assertEqual(poker.play_cards('S7', 'S7', 'S7', 'S5', 'S5', 'S5'), -1)
        self.assertEqual(poker.play_cards('S8', 'S8', 'S8', 'S8', 'S8', 'S8'), 0)
        self.assertEqual(poker.play_cards('S10', 'S10', 'S10', 'S2', 'S3', 'S4'), 1)
        self.assertEqual(poker.play_cards('S6', 'S7', 'S8', 'S4', 'S4', 'S4'), -1)
        self.assertEqual(poker.play_cards('S2', 'S4', 'S6', 'S7', 'S8', 'S9'), 0)
        self.assertEqual(poker.play_cards('SK', 'SQ', 'SA', 'S3', 'S4', 'S9'), -1)
        self.assertEqual(poker.play_cards('S5', 'S5', 'S5', 'SQ', 'SK', 'SA'), 1)
        self.assertEqual(poker.play_cards('SA', 'SQ', 'SK', 'S2', 'S2', 'S2'), -1)
        self.assertEqual(poker.play_cards('SA', 'SQ', 'SK', 'S2', 'S3', 'S4'), -1)
        self.assertEqual(poker.play_cards('S4', 'S5', 'S6', 'SK', 'SA', 'SQ'), 1)
        self.assertEqual(poker.play_cards('S9', 'S10', 'SJ', 'SA', 'SQ', 'SK'), 1)
        self.assertEqual(poker.play_cards('S2', 'S6', 'S5', 'S10', 'S4', 'S8'), 0)
        self.assertEqual(poker.play_cards('S4', 'S3', 'S7', 'S2', 'S6', 'SK'), 0)
        self.assertEqual(poker.play_cards('S9', 'S10', 'SJ', 'S8', 'S8', 'S4'), 0)




if __name__ == '__main__':
    unittest.main()
