from brownie import accounts, config, TokenERC20

initial_supply = 1000000000000000000 
token_name = "UMAR"
token_symbol = "UMR"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}, publish_source=True
    ) 