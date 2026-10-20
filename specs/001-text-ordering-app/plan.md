# Implementation Plan: 純文字點餐軟體

**Branch**: `001-text-ordering-app` | **Date**: 2026-10-20 | **Spec**: [spec.md](spec.md)

## Summary

建立一個不依賴外部服務的 Python 命令列點餐程式。核心訂單規則放在可獨立測試的
領域模組，CLI 只負責顯示提示、解析輸入與呼叫服務，讓計算與互動流程容易驗證。

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: Python standard library only

**Storage**: In-memory only

**Testing**: `unittest` from the Python standard library

**Target Platform**: Windows, macOS, and Linux terminals

**Project Type**: CLI application

**Performance Goals**: 每次選單操作在 100ms 內完成；支援至少 100 個訂單項目

**Constraints**: 離線可執行、無第三方套件、金額使用整數元、錯誤不得中斷主流程

**Scale/Scope**: 單一使用者、單次執行、固定菜單與本次訂單

## Constitution Check

- **User-Centered Task Management**: PASS — 功能以清楚的點餐與訂單狀態為核心。
- **Explicit and Consistent Data Contracts**: PASS — MenuItem、OrderItem、Order 與 CLI 命令輸入均明確定義。
- **Testable Correctness**: PASS — 領域邏輯使用 `unittest` 覆蓋成功、錯誤與空訂單流程。
- **Secure and Resilient Defaults**: PASS — 輸入在邊界驗證，錯誤保留訂單狀態且不使用敏感資料。
- **Simple, Observable Evolution**: PASS — 僅使用標準函式庫，CLI 錯誤訊息清楚且不引入過度抽象。

## Project Structure

```text
specs/001-text-ordering-app/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── cli-contract.md
└── tasks.md

ordering_app/
├── __init__.py
├── models.py
├── menu.py
├── service.py
└── cli.py

tests/
├── test_models.py
├── test_service.py
└── test_cli.py

README.md
run.py
```

**Structure Decision**: 使用根目錄下的 `ordering_app` 套件與 `tests` 測試目錄。
`models.py` 定義資料模型，`service.py` 實作訂單規則，`cli.py` 負責互動。
`run.py` 提供直接啟動入口。

## Complexity Tracking

無違反憲章的複雜度；不需要額外追蹤。
