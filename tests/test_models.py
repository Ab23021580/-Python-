import unittest

from ordering_app.models import MenuItem, OrderError, OrderItem


class ModelTests(unittest.TestCase):
    def test_subtotal(self) -> None:
        self.assertEqual(OrderItem(MenuItem(1, "飯", 80), 3).subtotal, 240)

    def test_invalid_quantity_rejected(self) -> None:
        with self.assertRaises(OrderError):
            OrderItem(MenuItem(1, "飯", 80), 0)
