from .models import MenuItem, OrderError


MENU = (
    MenuItem(1, "牛肉麵", 120),
    MenuItem(2, "雞肉飯", 80),
    MenuItem(3, "滷味拼盤", 100),
    MenuItem(4, "珍珠奶茶", 60),
)


def find_menu_item(item_id: int) -> MenuItem:
    """Return the menu item with the requested id."""
    for item in MENU:
        if item.id == item_id:
            return item
    raise OrderError("找不到此餐點")
