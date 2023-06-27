"""
Testing the town cost and its title.
"""

import pytest
from costs import TownCost

def test_make_town_cost():

    unit_cost = TownCost(5, 2000.0)
    assert unit_cost.get_cost() == (5, 2000.0)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        TownCost(5, -1)

    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name():

    with pytest.raises(ValueError) as exp:
        TownCost(11, 2000)

    assert str(exp.value) == "Invalid index!!"

