import json
import logging
import time
from utils import get_env

from web3 import Web3, HTTPProvider


(
    CONTRACT_ADDRESS,
    RINKEBY_PUBLIC_INFURA_ENDPOINT,
    MAINNET_PUBLIC_INFURA_ENDPOINT,
    CHAIN_ID,
) = get_env()


PUBLIC_INFURA_ENDPOINT = (
    MAINNET_PUBLIC_INFURA_ENDPOINT
    if CHAIN_ID == "1"
    else RINKEBY_PUBLIC_INFURA_ENDPOINT
)

# read api
with open("abi.json") as f:
    abi = json.loads(f.read())["abi"]

address = "your address"
private_key = "your private key"
my_token_id = [1, 2]

# in gwei
maxFeePerGas = "60"
maxPriorityFeePerGas = "2"


def main():
    logging.info(f"Bot is active now!")
    w3 = Web3(HTTPProvider(PUBLIC_INFURA_ENDPOINT))
    logging.info(f"isConnected: {w3.isConnected()}")

    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    logging.info(f"Sucessfully connected to the contract")

    tx = {
        "gas": 300000,  # 看了看别人的 reveal 交易，gas 在 200 000 左右，所以还好
        "maxFeePerGas": w3.toWei(maxFeePerGas, "gwei"),
        "maxPriorityFeePerGas": w3.toWei(maxPriorityFeePerGas, "gwei"),
        "nonce": w3.eth.get_transaction_count(address),
    }

    transaction = contract.functions.reveal(my_token_id).buildTransaction(tx)
    signed_tnx = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_tnx.rawTransaction)
    logging.info(f"reveal txn hash: {w3.toHex(txn_hash)} ")

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    status = txn_receipt["status"]
    if status == 0:
        logging.info(f"Transaction reverted.")
    else:
        logging.info(f"Succeeded!")


if __name__ == "__main__":
    loglevel = logging.INFO
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y/%m/%d %I:%M:%S",
        level=loglevel,
    )
    main()
