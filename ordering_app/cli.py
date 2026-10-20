from collections.abc import Callable

from .menu import MENU
from .models import OrderError
from .service import OrderService

Input = Callable[[str], str]
Output = Callable[[str], None]


class OrderingApp:
    """Run the interactive terminal ordering flow."""

    def __init__(
        self,
        service: OrderService | None = None,
        input_fn: Input = input,
        output_fn: Output = print,
    ) -> None:
        self.service = service or OrderService()
        self.input = input_fn
        self.output = output_fn

    def show_menu(self) -> None:
        """Print all available menu items."""
        self.output("菜單：")
        for item in MENU:
            self.output(f"{item.id}. {item.name} - {item.price} 元")

    def _read_int(self, prompt: str) -> int:
        try:
            return int(self.input(prompt).strip())
        except ValueError as exc:
            raise OrderError("請輸入整數") from exc

    def add_item(self) -> None:
        """Read and add one item to the current order."""
        try:
            self.service.add_item(self._read_int("餐點編號："), self._read_int("數量："))
            self.output("已加入訂單。")
        except OrderError as exc:
            self.output(f"錯誤：{exc}")

    def modify_order(self) -> None:
        """Read and apply one order modification."""
        try:
            item_id = self._read_int("餐點編號（輸入 0 移除）：")
            if item_id == 0:
                self.service.remove_item(self._read_int("要移除的餐點編號："))
            else:
                self.service.update_quantity(item_id, self._read_int("新數量："))
            self.output("訂單已更新。")
        except OrderError as exc:
            self.output(f"錯誤：{exc}")

    def confirm_order(self) -> None:
        """Confirm the current order and print its receipt."""
        try:
            receipt = self.service.confirm()
            self.output(f"訂單編號：{receipt.order_id}")
            self.output("\n".join(receipt.lines))
            self.output(f"總計：{receipt.total} 元")
        except OrderError as exc:
            self.output(f"錯誤：{exc}")

    def run(self) -> None:
        """Run the main menu until the user exits."""
        self.output("歡迎使用點餐系統！")
        while True:
            self.output("\n1. 查看菜單  2. 加入餐點  3. 查看訂單  4. 修改訂單  5. 確認訂單  0. 離開")
            choice = self.input("請選擇：").strip()
            if choice == "1":
                self.show_menu()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.output(self.service.get_summary())
            elif choice == "4":
                self.modify_order()
            elif choice == "5":
                self.confirm_order()
            elif choice == "0":
                if self.service.order.items:
                    answer = self.input("訂單尚未確認，確定離開？(y/n)：").strip().lower()
                    if answer != "y":
                        continue
                self.output("謝謝光臨！")
                return
            else:
                self.output("錯誤：無效的選項。")
