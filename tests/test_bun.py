import pytest
from practikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("white bun", 100),
    ("black bun", 150),
    ("sesame bun", 120)
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


def test_bun_name():
    bun = Bun("wheat bun", 110)
    assert bun.get_name() == "wheat bun"


def test_bun_price():
    bun = Bun("rye bun", 130)
    assert bun.get_price() == 130
