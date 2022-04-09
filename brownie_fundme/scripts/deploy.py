from brownie import FundMe
from scripts.helpful_scripts import get_accounts


def deploy_fundme():
    account = get_accounts()
    fundme = FundMe.deploy({"from": account}, publish_source = True)
    print(f"contract depoyed to {fundme.address}")


def main():
    deploy_fundme()
