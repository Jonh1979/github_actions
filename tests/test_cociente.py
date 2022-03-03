from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(10, 5) == 2
        assert cociente(5, 5) == 1
        assert cociente(17, 4) == 4
        assert cociente(20, 10) == 2
