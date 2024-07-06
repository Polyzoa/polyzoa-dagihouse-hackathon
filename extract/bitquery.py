def extract_data(contract, data):
    contract.contract_type = data["transactions"][0]["creates"]["smart_contract"]["contract_type"]
    contract.name = data["transactions"][0]["creates"]["smart_contract"]["currency"]["name"]
    contract.symbol = data["transactions"][0]["creates"]["smart_contract"]["currency"]["symbol"]
    contract.decimals = data["transactions"][0]["creates"]["smart_contract"]["currency"]["decimals"]
    contract.creator = data["transactions"][0]["sender"]["address"]
    contract.creator_contract_type = (data["transactions"][0]["sender"]["smart_contract"]["contract_type"]
                                      if data["transactions"][0]["sender"]["smart_contract"]["contract_type"] is not None
                                      else "EOA")
    contract.creation_date = data["transactions"][0]["block"]["timestamp"]["unixtime"]
