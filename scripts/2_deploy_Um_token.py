from brownie import accounts, config, UmarToken

initial_supply = 1000000000000000000 
token_name = "UMAR"
token_symbol = "UMR"


def main():
    account = accounts[0]
    erc20 = UmarToken.deploy(initial_supply, {"from": account})
        