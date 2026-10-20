# CLI Contract

## Startup

`python run.py` starts an interactive session and displays the main menu.

## Main menu commands

| Input | Operation |
|---|---|
| `1` | 顯示菜單 |
| `2` | 加入餐點 |
| `3` | 查看目前訂單 |
| `4` | 修改訂單 |
| `5` | 確認訂單 |
| `0` | 離開 |

Unknown commands return an error message and redisplay the menu.

## Output contract

Menu output contains item id, name, and price. Order output contains item name,
unit price, quantity, subtotal, and total. Confirmation output contains order id,
all order lines, and total.

## Error contract

Invalid input is reported as a human-readable message in the terminal. The current
valid order remains unchanged. Empty orders cannot be confirmed.
