from extract import Contract


def extract_data(contract: Contract, data):
    contract.holder_count = data["token"]["total_holders"]
    contract.is_honeypot = data["honeypot_result"]["is_honeypot"]
    contract.is_open_source = data["contract_code"]["open_source"]

