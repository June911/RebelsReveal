# Rebels Reveal 

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

After filling out the inputs, you're ready to reveal.  

```
python reveal.py
```