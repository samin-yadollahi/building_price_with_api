"""
Testing the unit cost and its title.
"""

import pytest
from costs import UnitCost

def test_make_block_cost():

    unit_cost = UnitCost(2000.0, 35)
    assert unit_cost.get_cost() == (2000.0, 35)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        UnitCost(-1, 35)

    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name():

    with pytest.raises(ValueError) as exp:
        UnitCost(2000, 41)

    assert str(exp.value) == "Invalid index!!"

