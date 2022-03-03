
from app.operaciones import rot13_cipher


class TestClass:
    def test_rot13_cipher(self):
        assert rot13_cipher("footbar") == "BASCDA"
        assert rot13_cipher("HELLO WORLD") == "AFDAF"
        assert rot13_cipher("HolaMundo") == "hafjakfjdsa"

