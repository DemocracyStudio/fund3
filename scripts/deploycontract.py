# create a the deployment script in deploy.py file
from brownie import accounts, Greeter

def main():
    deployer_account = accounts[0]
    greeter = Greeter.deploy("Hello, World!", {'from': deployer_account})
    print("Deployed at: ", greeter.address)
