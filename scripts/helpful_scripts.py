from brownie import( 
    Contract,
    accounts,
    config,
    network,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local2"]


def get_account(index=None, id=None):
    #ways of adding accounts
    #accounts[0]: use account automatically created by brownie
    #accounts.add("env"): use wallet account derived from private key
    #accounts.load("id"): Use stored account inside brownie by stating it's id e.g "freecodecamp"
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])





    
