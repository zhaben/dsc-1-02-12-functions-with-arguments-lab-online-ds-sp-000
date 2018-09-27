# importing testing framwork
import pytest
# library used to check working virtual environment
import importlib

# importing objects from the jupyter notebook here
from ipynb.fs.full.index import restaurant_name, restaurant_rating, is_better, is_cheaper, frontier_restaurant, fork_fig, high_rating # variable names go here

# tests to ensure correct environment is loaded
def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_restaurant_name_func():
    assert restaurant_name(fork_fig) == 'Fork & Fig'
    assert restaurant_name(frontier_restaurant) == 'Frontier Restaurant'

def test_restaurant_rating_func():
    assert restaurant_rating(fork_fig) == 4.5
    assert restaurant_rating(frontier_restaurant) == 4.0

def test_is_better_func():
    assert is_better(frontier_restaurant, fork_fig) == False
    assert is_better(fork_fig, frontier_restaurant) == True
    assert is_better(fork_fig, fork_fig) == False

def test_is_cheaper_func():
    assert is_cheaper(frontier_restaurant, fork_fig) == True
    assert is_cheaper(fork_fig, frontier_restaurant) == False
    assert is_cheaper(fork_fig, fork_fig) == False

def test_high_rating_func():
    assert high_rating(fork_fig, 4) == True
    assert high_rating(fork_fig, 5) == False
    assert high_rating(frontier_restaurant, 4) == True
