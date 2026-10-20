from dataclasses import dataclass
from uuid import uuid4

from .menu import find_menu_item
from .models import Order, OrderError, OrderStatus


@dataclass(frozen=True)
class Receipt:
    order_id: str
    lines: tuple[str, ...]
    total: int


class OrderService:
    """Manage the current in-memory order."""

    def __init__(self) -> None:
        self.order = Order()

    def add_item(self, item_id: int, quantity: int) -> None:
        """Add a menu item or increase its existing quantity."""
        self.order.ensure_open()
        if quantity <= 0:
            raise OrderError("數量必須是正整數")
        item = find_menu_item(item_id)
        current = self.order.items.get(item_id)
        if current:
            current.quantity += quantity
        else:
            from .models import OrderItem
            self.order.items[item_id] = OrderItem(item, quantity)

    def update_quantity(self, item_id: int, quantity: int) -> None:
        """Set an item's quantity, removing it when the quantity is zero."""
        self.order.ensure_open()
        if item_id not in self.order.items:
            raise OrderError("訂單中沒有此餐點")
        if quantity < 0:
            raise OrderError("數量不可為負數")
        if quantity == 0:
            del self.order.items[item_id]
        else:
            self.order.items[item_id].quantity = quantity

    def remove_item(self, item_id: int) -> None:
        """Remove an item from the open order."""
        self.order.ensure_open()
        if item_id not in self.order.items:
            raise OrderError("訂單中沒有此餐點")
        del self.order.items[item_id]

    def get_summary(self) -> str:
        """Return a human-readable summary of the current order."""
        if not self.order.items:
            return "目前訂單是空的。"
        lines = ["目前訂單："]
        for item in self.order.items.values():
            lines.append(
                f"{item.menu_item.name} x {item.quantity} = {item.subtotal} 元"
            )
        lines.append(f"總計：{self.order.total} 元")
        return "\n".join(lines)

    def confirm(self) -> Receipt:
        """Confirm the order and return a receipt."""
        self.order.ensure_open()
        if not self.order.items:
            raise OrderError("空訂單無法確認")
        order_id = uuid4().hex[:8].upper()
        self.order.order_id = order_id
        self.order.status = OrderStatus.CONFIRMED
        lines = tuple(
            f"{item.menu_item.name} x {item.quantity} = {item.subtotal} 元"
            for item in self.order.items.values()
        )
        total = self.order.total
        self.order.items.clear()
        return Receipt(order_id, lines, total)
