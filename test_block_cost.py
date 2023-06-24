"""
Testing the block cost and its title.
"""

import pytest
from costs import BlockCost

def test_make_block_cost():

    block_cost = BlockCost(2000.0, 15)
    assert block_cost.get_cost() == (2000.0, 15)


def test_generating_block_cost():

    with pytest.raises(ValueError) as exp:
        BlockCost(-2000, 15)
    assert str(exp.value) == "invalid input the cost should be a positive number"


def test_generating_name_cost():

    with pytest.raises(ValueError) as exp:
        BlockCost(2000, 21)
    assert str(exp.value) == "invalid index!!"
    