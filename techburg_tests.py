# techburg_tests.py
import unittest
from techburg_classes import RechargeStation, SparePart, SurvivorBot

class TestTechburgSimulation(unittest.TestCase):
    def test_bot_movement_and_energy(self):
        bot = SurvivorBot((0, 0))
        bot.move((1, 1))
        self.assertEqual(bot.location, (1, 1))
        self.assertEqual(bot.energy, 95)

    def test_collect_and_deposit_part(self):
        bot = SurvivorBot((1, 1), 100)
        part = SparePart('small', (1, 1))
        station = RechargeStation((2, 2))
        bot.collect_part(part)
        bot.move((2, 2))
        bot.deposit_part(station)
        self.assertEqual(len(station.stored_parts), 1)
        self.assertIsNone(bot.carrying)

if __name__ == '__main__':
    unittest.main()
