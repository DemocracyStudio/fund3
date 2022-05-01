# create a test in a file simple_test.py in tests folder
import pytest
from brownie import Greeter, accounts

@pytest.fixture
def simple():
    return accounts[0].deploy(simplecontract, "Hello, World!")
    # Check if the contract was deployed with the correct greeting
    def simple_test(simple):
        assert simple.greet() == "Hello, World!"
    # Check if the greeting changes
    def test_set_simple(simple):
        simple.setGreeting("Hola, mundo!")
        assert simple.greet() == "Hola, mundo!"
