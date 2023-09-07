import pytest

from sps_python.ctverec import Ctverec


class TestCtverec:

    def setup_method(self):
        self.ct = Ctverec(velikost_strany=2)

    @pytest.mark.parametrize(
        "strana,output",
        [
            (4, 16),
            (5, 20),
            (6, 24)
        ]
    )
    def test_obvod(self, strana, output):
        self.ct.velikost = strana
        assert self.ct.obvod() == output
        self.ct.velikost = 100
        assert self.ct.obvod() == 400

    def teardown_method(self):
        pass