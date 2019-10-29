from unittest import TestCase
from largest_loss import largestLoss


class TestLargestLoss(TestCase):
    def test_largest_loss_function(self):
        prices_list = [0, 12, 4, 1234]
        self.assertEqual(largestLoss(prices_list), 1230)

    def test_largest_loss_function_empty_raise(self):
        with self.assertRaises(Exception) as context:
            largestLoss([])

        self.assertTrue('The submitted list is empty' in context.exception)

    def test_largest_loss_function_negative_raise(self):
        prices_list = [0, 12, -4, 1234]

        with self.assertRaises(Exception) as context:
            largestLoss(prices_list)

        self.assertTrue('The prices cannot be negative' in context.exception)

    def test_largest_loss_function_odd_raise(self):
        prices_list = [0, 12, 1234]

        with self.assertRaises(Exception) as context:
            largestLoss(prices_list)

        self.assertTrue('The length of the submitted list needs to be even ' \
            'in order to check both the related bought and sold prices' in context.exception)
