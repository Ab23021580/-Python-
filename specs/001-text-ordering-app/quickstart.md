# Quickstart Validation

## Prerequisites

- Python 3.11 or newer
- No third-party packages

## Run the application

```text
python run.py
```

Choose `1` to view the menu, `2` to add an item, `3` to view the order, `4` to
modify it, and `5` to confirm it. Choose `0` to exit.

## Run automated tests

```text
python -m unittest discover -s tests -v
```

Expected result: all tests pass, including price calculations, invalid input
preservation, cart updates, empty-order rejection, and confirmation summaries.
