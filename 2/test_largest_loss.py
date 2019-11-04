from unittest import TestCase
from largest_loss import largestLoss


class TestLargestLoss(TestCase):
    def test_largest_loss_function(self):
        prices_list = [0, 12, 4, 1234]
        self.assertEqual(largestLoss(prices_list), 1230)

    def test_largest_loss_function_empty_raise(self):
        self.assertRaises(Exception, lambda: largestLoss([]))

    def test_largest_loss_function_negative_raise(self):
        prices_list = [0, 12, -4, 1234]

        self.assertRaises(Exception, lambda: largestLoss(prices_list))

    def test_largest_loss_function_odd_raise(self):
        prices_list = [0, 12, 1234]

        self.assertRaises(Exception, lambda: largestLoss(prices_list))
