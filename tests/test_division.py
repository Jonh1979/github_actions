from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(10, 5) == 2
        assert division(15, 3) == 5
        assert division(40, 5) == 8
        assert division(5, 5) == 1
