import pytest

from app import mean_score


def test_mean_score_returns_average():
    assert mean_score([4, 5, 3, 5]) == 4.25


def test_mean_score_accepts_one_value():
    assert mean_score([7]) == 7


def test_mean_score_rejects_empty_list():
    with pytest.raises(ValueError):
        mean_score([])
