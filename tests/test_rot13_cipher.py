
from app.operaciones import rot13_cipher


class TestClass:
    def test_rot13_cipher(self):
        assert rot13_cipher("footbar") == "fafdasaf"
        assert rot13_cipher("HELLO WORLD") == "fsafdsaf"
        assert rot13_cipher("HolaMundo") == "hafjakfjdsa"

