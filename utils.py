import os
from dotenv import load_dotenv


def get_env():
    """get dot env variables from .env file

    Returns:
        tuple: a set of environment variables
    """

    load_dotenv()  # take environment variables from .env.

    CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")
    RINKEBY_PUBLIC_INFURA_ENDPOINT = os.environ.get("RINKEBY_PUBLIC_INFURA_ENDPOINT")
    MAINNET_PUBLIC_INFURA_ENDPOINT = os.environ.get("MAINNET_PUBLIC_INFURA_ENDPOINT")
    CHAIN_ID = os.environ.get("CHAIN_ID")

    return (
        CONTRACT_ADDRESS,
        RINKEBY_PUBLIC_INFURA_ENDPOINT,
        MAINNET_PUBLIC_INFURA_ENDPOINT,
        CHAIN_ID,
    )
