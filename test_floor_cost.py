"""
Testing the floor cost and its title.
"""

import pytest
from costs import FloorCost

def test_make_floor_cost():

    unit_cost = FloorCost(2000.0, 25)
    assert unit_cost.get_cost() == (2000.0, 25)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        FloorCost(-1, 25)

    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name():

    with pytest.raises(ValueError) as exp:
        FloorCost(2000, 31)

    assert str(exp.value) == "Invalid index!!"

