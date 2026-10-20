from dataclasses import dataclass, field
from enum import Enum


class OrderError(ValueError):
    """Raised when an order operation is invalid."""


class OrderStatus(Enum):
    OPEN = "open"
    CONFIRMED = "confirmed"


@dataclass(frozen=True)
class MenuItem:
    id: int
    name: str
    price: int

    def __post_init__(self) -> None:
        if self.id <= 0 or not self.name or self.price < 0:
            raise OrderError("餐點資料無效")


@dataclass
class OrderItem:
    menu_item: MenuItem
    quantity: int

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise OrderError("數量必須是正整數")

    @property
    def subtotal(self) -> int:
        return self.menu_item.price * self.quantity


@dataclass
class Order:
    items: dict[int, OrderItem] = field(default_factory=dict)
    status: OrderStatus = OrderStatus.OPEN
    order_id: str | None = None

    @property
    def total(self) -> int:
        return sum(item.subtotal for item in self.items.values())

    def ensure_open(self) -> None:
        if self.status is not OrderStatus.OPEN:
            raise OrderError("訂單已確認，無法修改")
