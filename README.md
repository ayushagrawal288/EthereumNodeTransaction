## Basic outline of the steps to follow:

1. Connect to an Ethereum node (hosted by Infura) using web3js on the Kovan testnet.
    Reference: https://www.shawntabrizi.com/ethereum/ethereum-web3-js-hello-world-get-eth-balance-ethereum-address/.
2. You can use this blockchain testnet API endpoint on Infura: kovan.infura.io/v3/6c6f87a10e12438f8fbb7fc7c762b37c
3. For Go developers, refer https://goethereumbook.org/en/ for starters.
4. It is possible to get a particular ethereum block, using the getBlock API.
5. Index the data in a database of your choice that will serve as the datastore for the API requests. Most important fields in a transaction for the purpose of this assignment will be from, to, blockNumber and transactionHash.
6. We would like you to index at least 10,000 recent blocks.
7. Construct an API to retrieve the user transactions, given the user address.

I have created a database and indexed transaction for 12000 blocks



Getting Started
---------------

- Change directory into your newly created project.

    cd EthereumNodeTransaction/

- Create a Python virtual environment.

    virtualenv -p python3 venv
    source venv/bin/activate

- Upgrade packaging tools.

    pip install -r requirements.txt

- Run your project.

    python manage.py runserver

Endpoints
---------
Book:
- List(get):
    /eth/transactions/{user_hash}/
