from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(16, 2) == 0
        assert resto(9, 3) == 0
        assert resto(12, 5) == 2
        assert resto(19,2) == 1
