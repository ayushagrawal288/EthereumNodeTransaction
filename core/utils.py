from core.models import Transactions
from core.serializers import TransactionSerializer
from web3.auto import w3
import pdb


def initialize_db():
    is_connected = w3.isConnected()

    if not is_connected:
        raise ConnectionError("W3 not connected")

    block_number = w3.eth.blockNumber

    # pdb.set_trace()

    # Query Get block 12000 times and populate the db
    for i in range(12000):
        block = w3.eth.getBlock(block_number-i, True)
        transactions = block.transactions

        for j in range(len(transactions)):
            t = transactions[j]
            data = {
                "block_number": t["blockNumber"],
                "to_user": t["to"],
                "from_user": t["from"],
                "hash": t["hash"].hex()
            }
            # pdb.set_trace()

            doc = Transactions.objects.create(**data)
            doc.save()
