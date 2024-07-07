from dataclasses import dataclass

from pandas import DataFrame

from extract import Contract

@dataclass
class Transfer:
    from_address: str
    to_address: str
    value: int


def extract_data(contract: Contract, data):
    transactions = data["data"]["items"]
    transfers = get_transfers(transactions, contract.address)
    df = DataFrame(transfers)
    # TODO add transfer stats to contract

def get_transfers(txns, address):
    transfers = []
    for tx in txns:
        logs = tx["log_events"]
        for log in logs:
            if "decoded" in log is None:
                continue
            decoded = log["decoded"]
            if decoded["name"] != "Transfer":
                continue
            value = None
            value_string = get_param(decoded["params"], "value")
            if value_string is not None:
                value = int(value_string)
            transfer = Transfer(
                from_address=get_param(decoded["params"], "from"),
                to_address=get_param(decoded["params"], "to"),
                value=value
            )
            transfers = [*transfers, transfer]
        return transfers

def get_param(params, name):
    return next((x for x in params if x["name"] == name), None)