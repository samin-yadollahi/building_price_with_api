"""
Testing the town cost and its title.
"""

import pytest
from costs import TownCost

def test_make_town_cost():

    unit_cost = TownCost(2000.0, 5)
    assert unit_cost.get_cost() == (2000.0, 5)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        TownCost(-1, 5)

    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name():

    with pytest.raises(ValueError) as exp:
        TownCost(2000, 11)

    assert str(exp.value) == "Invalid index!!"

