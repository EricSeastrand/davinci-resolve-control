from ui_interactor.utility import *

import pytest

def test_center_point_even_numbers():
    input_coords = {
        'L': 10,
        'R': 20,
        'T': 30,
        'B': 60
    }

    x,y = calc_center_point(input_coords)

    assert x == 15, "X coord is not halfway between L and R"

    assert y == 45, "Y coord is not halfway between T and B"

def test_center_point_left_must_be_less_than_right():
    with pytest.raises(Exception) as excinfo:
        input_coords = {
            'L': 30,
            'R': 20,
            'B': 20,
            'T': 30
        }

        x,y = calc_center_point(input_coords)

    assert "Left must be less than Right" in str(excinfo.value)

def test_center_point_top_must_be_less_than_bottom():
    with pytest.raises(Exception) as excinfo:
        input_coords = {
            'L': 20,
            'R': 30,
            'B': 20,
            'T': 30
        }

        x,y = calc_center_point(input_coords)

    assert "Top must be less than Bottom" in str(excinfo.value)
