# this contract only works for local development chains as thats what i programmed it for

from brownie import Greeter, accounts, config, network

def main():
    deploy()

def deploy():
    account = accounts[0]
    Greeter_contract = Greeter.deploy({"from":account})
    print(Greeter_contract)
    setGreet = Greeter_contract.setGreet({"from":account})
    setGreet.wait(1)
    print(setGreet)
    getGreet = Greeter_contract.getGreet()
    print(getGreet)

