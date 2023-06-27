"""
Testing the unit cost and its title.
"""

import pytest
from costs import UnitCost

def test_make_unit_cost():

    unit_cost = UnitCost(2000.0)
    assert unit_cost.get_cost() == (2000.0)


def test_generating_cost():

    with pytest.raises(ValueError) as exp:
        UnitCost(-1)

    assert str(exp.value) == "invalid input the cost should be a positive number"

