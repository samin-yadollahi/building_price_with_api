"""
Testing the floor cost and its title.
"""

import pytest
from costs import FloorCost

def test_make_floor_cost():

    unit_cost = FloorCost(25, 2000.0)
    assert unit_cost.get_cost() == (25, 2000.0)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        FloorCost(25, -1)

    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name():

    with pytest.raises(ValueError) as exp:
        FloorCost(31, 2000)

    assert str(exp.value) == "Invalid index!!"

