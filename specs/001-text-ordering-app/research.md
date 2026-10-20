# Research: 純文字點餐軟體

## Decision: 使用 Python 標準函式庫與 `unittest`

**Rationale**: 需求是單機、離線、純文字應用；標準函式庫可避免安裝成本，
並符合簡單、可攜與可測試的憲章要求。

**Alternatives considered**: pytest 功能完整但需要外部依賴；資料庫不符合 v1
單次執行與記憶體儲存範圍。

## Decision: 分離領域邏輯與終端機 I/O

**Rationale**: 訂單計算、驗證與狀態轉換可用純函式或服務類別測試，CLI 使用注入的
輸入輸出函式測試，避免測試依賴真人互動。

**Alternatives considered**: 將所有邏輯放在單一互動迴圈中實作較快，但難以驗證並容易
在錯誤輸入時遺失狀態。

## Decision: 使用整數元表示金額

**Rationale**: v1 不處理小數貨幣；整數計算避免浮點誤差，輸出格式也更簡單。

**Alternatives considered**: Decimal 適合複雜貨幣，但會增加目前不需要的複雜度。
