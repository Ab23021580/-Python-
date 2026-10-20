import unittest

from ordering_app.cli import OrderingApp


class CliTests(unittest.TestCase):
    def run_app(self, inputs: list[str]) -> list[str]:
        output: list[str] = []
        iterator = iter(inputs)
        OrderingApp(input_fn=lambda _: next(iterator), output_fn=output.append).run()
        return output

    def test_invalid_add_keeps_flow_and_reports_error(self) -> None:
        output = self.run_app(["2", "99", "1", "0"])
        self.assertTrue(any("錯誤" in line for line in output))
        self.assertIn("謝謝光臨！", output)

    def test_confirm_outputs_receipt(self) -> None:
        output = self.run_app(["2", "4", "2", "5", "0"])
        self.assertTrue(any("訂單編號：" in line for line in output))
        self.assertTrue(any("120 元" in line for line in output))

    def test_modify_updates_quantity_and_removes_item(self) -> None:
        output = self.run_app(
            [
                "2", "1", "1", "2", "2", "2", "3", "4", "1", "3", "3",
                "4", "0", "1", "4", "0", "2", "3", "0",
            ]
        )
        rendered = "\n".join(output)
        self.assertIn("牛肉麵 x 3 = 360 元", rendered)
        self.assertIn("雞肉飯 x 2 = 160 元", rendered)
        self.assertIn("目前訂單是空的。", output)
