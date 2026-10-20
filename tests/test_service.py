import unittest

from ordering_app.models import OrderError, OrderStatus
from ordering_app.service import OrderService


class ServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = OrderService()

    def test_add_merges_and_calculates_total(self) -> None:
        self.service.add_item(1, 2)
        self.service.add_item(1, 1)
        self.assertEqual(self.service.order.items[1].quantity, 3)
        self.assertEqual(self.service.order.total, 360)

    def test_update_and_remove(self) -> None:
        self.service.add_item(1, 1)
        self.service.add_item(2, 2)
        self.service.update_quantity(1, 3)
        self.service.remove_item(2)
        self.assertEqual(self.service.order.total, 360)

    def test_empty_order_cannot_confirm(self) -> None:
        with self.assertRaises(OrderError):
            self.service.confirm()

    def test_confirm_creates_receipt_and_locks_order(self) -> None:
        self.service.add_item(4, 1)
        receipt = self.service.confirm()
        self.assertEqual(receipt.total, 60)
        self.assertEqual(self.service.order.status, OrderStatus.CONFIRMED)
        with self.assertRaises(OrderError):
            self.service.add_item(1, 1)
