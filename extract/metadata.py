from extract import Contract


def extract_data(contract: Contract, data):
    contract.contract_type = data["contract_type"]
    contract.name = data["name"]
    contract.symbol = data["symbol"]
    contract.total_supply = data["totalSupply"]
    contract.decimals = data["decimals"]
    contract.owner = data["owner"]
