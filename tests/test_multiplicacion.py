from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(4, 5) == 20
        assert multiplicacion(-1, -2) == 2
        assert multiplicacion(-7, 5) == -35
        assert multiplicacion(-7, 9) == -63
