import pytest

from hangingman import __version__, game


def test_version():
    assert __version__ == '0.1.0'


class TestHangingmanEngine:

    @pytest.fixture
    def hanging(self):
        return game.HangingmanEngine()
    
    def test_engine_init(self, hanging):
        assert hanging.level == "easy"
        assert hanging.chances == 5
        assert hanging.words == (4, 5, 6)

    def test_setup_level(self, hanging):
        hanging.setup_level("harder")
        assert hanging.level == "harder"
        assert hanging.chances == 5
        assert hanging.words == (13, 14, 15)

    def test_setup_level_wrong_arg(self, hanging):
        with pytest.raises(ValueError):
            hanging.setup_level("are you kidding me?")
            hanging.setup_level(9)
            hanging.setup_level(print)
