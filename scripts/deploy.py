from scripts.helpful_scripts import get_account
from brownie import OurToken, web3
from web3 import Web3 


#Convert 1000 ETH to wei
initial_supply = Web3.toWei(1000, "ether")

def deploy_erc20_token():
    account = get_account()
    token = OurToken.deploy(initial_supply, {"from": account})
    print(token.name())

def main():
    deploy_erc20_token()

