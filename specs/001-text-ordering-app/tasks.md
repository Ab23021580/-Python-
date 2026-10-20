# Tasks: 純文字點餐軟體

**Input**: Design documents from `specs/001-text-ordering-app/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli-contract.md, quickstart.md

## Phase 1: Setup

- [x] T001 Create the `ordering_app` package with `ordering_app/__init__.py` and the `tests/` directory
- [x] T002 [P] Create the `run.py` entry point and document local execution in `README.md`
- [x] T003 [P] Add Python ignore patterns to `.gitignore`

## Phase 2: Foundational

- [x] T004 Define `MenuItem`, `OrderItem`, `Order`, and validation exceptions in `ordering_app/models.py`
- [x] T005 Define the fixed menu and lookup helper in `ordering_app/menu.py`
- [x] T006 [P] Add model and money calculation tests in `tests/test_models.py`
- [x] T007 Add service contract tests for adding, merging, updating, removing, and confirming orders in `tests/test_service.py`

## Phase 3: User Story 1 - 瀏覽菜單並建立訂單 (Priority: P1)

**Goal**: 顧客可查看固定菜單、加入餐點、合併重複餐點並查看小計。

**Independent Test**: Run the service tests for menu lookup and adding items; valid items
appear with correct quantities and totals.

- [x] T008 Implement `OrderService.add_item` and `OrderService.get_summary` in `ordering_app/service.py`
- [x] T009 [P] Add CLI menu rendering and add-item flow in `ordering_app/cli.py`
- [x] T010 Add CLI tests for valid add flow and invalid item/quantity preservation in `tests/test_cli.py`

## Phase 4: User Story 2 - 檢視與修改購物車 (Priority: P2)

**Goal**: 顧客可查看明細、更新數量與移除餐點。

**Independent Test**: Start with two items, update one quantity, remove the other, and
verify item subtotals and total.

- [x] T011 Implement `OrderService.update_quantity` and `OrderService.remove_item` in `ordering_app/service.py`
- [x] T012 Implement CLI order display and modification flow in `ordering_app/cli.py`
- [x] T013 [P] Extend `tests/test_service.py` and `tests/test_cli.py` for cart updates, removal, and empty-cart messages

## Phase 5: User Story 3 - 確認訂單並取得摘要 (Priority: P3)

**Goal**: 顧客可拒絕空訂單，確認有效訂單並取得唯一編號與摘要。

**Independent Test**: Confirm a non-empty order and verify its receipt; confirm an empty
order and verify it remains open with an error.

- [x] T014 Implement confirmation state transition and receipt generation in `ordering_app/service.py`
- [x] T015 Implement CLI confirmation, exit confirmation, and main loop in `ordering_app/cli.py`
- [x] T016 [P] Add confirmation, empty-order rejection, and exit-flow tests in `tests/test_cli.py`

## Phase 6: Polish and Cross-Cutting Concerns

- [x] T017 [P] Add type hints and concise docstrings to public functions in `ordering_app/`
- [x] T018 Run `python -m unittest discover -s tests -v` and fix all failures
- [x] T019 Run the quickstart scenarios manually and update `README.md` if output or commands differ

## Dependencies and Execution Order

```text
T001 -> T004 -> T005 -> T006/T007
T007 -> T008 -> T009/T010
T008 -> T011 -> T012/T013
T011 -> T014 -> T015/T016
T015/T016 -> T017 -> T018 -> T019
```

Parallel opportunities:

- T002 and T003 can run in parallel after T001.
- T006 and T007 can run in parallel after model/menu setup.
- T009 and T010 can run in parallel after T008 if the CLI contract is stable.
- T013 and T016 are test-focused and can be prepared in parallel with their respective CLI changes.
- T017 can run after all feature phases and before final validation.

## Implementation Strategy

1. Complete setup and foundational models first.
2. Deliver the P1 add-and-view flow as the MVP.
3. Add cart modification as an independently testable P2 slice.
4. Add confirmation and receipt output as P3.
5. Finish with type/documentation polish and full validation.

## Phase 7: Convergence

- [x] T020 Add CLI tests covering quantity updates, item removal, and the empty-order display per US2/AC1-AC3 (partial)
