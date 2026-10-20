# Data Model: 純文字點餐軟體

## MenuItem

- `id`: 非空且唯一的整數編號
- `name`: 非空餐點名稱
- `price`: 大於或等於零的整數元

## OrderItem

- `menu_item`: 一個 `MenuItem`
- `quantity`: 大於零的整數
- `subtotal`: `menu_item.price * quantity`

## Order

- `items`: 依餐點編號合併的 `OrderItem` 集合
- `total`: 所有項目 subtotal 的總和
- `status`: `OPEN` 或 `CONFIRMED`
- `order_id`: 確認後產生的本次執行唯一識別碼

### State transitions

```text
OPEN --confirm with items--> CONFIRMED
OPEN --remove last item--> OPEN (empty)
OPEN --invalid input--> OPEN (unchanged)
```

## Validation rules

- 不存在的餐點編號拒絕加入或更新。
- 數量必須是十進位正整數；更新為零代表移除。
- 空訂單不能確認。
- 已確認訂單不可再修改。
