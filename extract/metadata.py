from extract import Contract
from services.eth import is_contract


def extract_data(contract: Contract, data):
    contract.contract_type = data["contract_type"]
    contract.name = data["name"]
    contract.symbol = data["symbol"]
    contract.total_supply = data["totalSupply"]
    contract.decimals = data["decimals"]
    contract.owner = data["owner"]
    contract.owner_contract_type = is_contract(contract.chain, contract.address)
