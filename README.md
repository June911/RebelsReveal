# Rebels Reveal 

This repository calls the `reveal` function in [rebels contract](https://etherscan.io/address/0xe9fca552b9eb110c2d170962af740725f71f5644). Of course, you can reveal the rebels' cards on [rebels.art/reveal/connect](https://rebels.art/reveal/connect), but it does not give the option to reveal multiple cards in a single transaction. Here, this Repo calls the `reveal` function, which can reveal multiple cards in a single transaction. For those of you who have multiple cards in your wallet and want to save money on gas and, this repo is for you.


## Qucik Start 

Install required packages 

```
pip install -r requirements.txt 
```

Copy .env.sample and rename it to .env, then modify the contents.

```
cp .env.sample .env
```

Modify the inputs in `reveal.py`
- `address` and `private_key` are you wallet info 
- `my_token_id` is your rebels card id, 
    - you can find them [here](https://rebels.art/reveal/connect)
    - it returns the id in Hexadecimal format, 
    - to convert hexadecimal into decimals, check [here](https://www.rapidtables.com/convert/number/hex-to-decimal.html)
    - in the end, you should have a list of id, e.g., [1, 2, 3]
- `maxFeePerGas` and `maxPriorityFeePerGas` are the eth gas parameters. To get the market gas price, check [here](https://etherscan.io/gastracker)

After filling out the inputs, you're ready to reveal. LFG REBELS!  

```
python reveal.py
```