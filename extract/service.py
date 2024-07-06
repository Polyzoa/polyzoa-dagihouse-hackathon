from pandas import DataFrame

import buckets
import holders
import honeypot
import transactions
import transactions_summary
from extract import Contract
import bitquery
import dexscreener


def get_address_files(file_names: list[str]) -> dict[str, list[str]]:
    address_files = {}
    for name in file_names:
        paths = str.split(name, "/")
        address = "/".join(paths[0:2])
        if address not in address_files:
            address_files[address] = []
        address_files[address] = [*address_files[address], name]
    return address_files


def extract_data(chain_address: str, files: list[str]) -> Contract:
    (chain,address) = str.split(chain_address, "/")
    contract = Contract(chain=chain, address=address)
    for file in files:
        data = buckets.get("data-wrangler", file)
        if file.endswith("blacklist.json"):
            contract.is_blacklisted = data["is_blacklisted"]
        elif file.endswith("bitquery.json"):
            bitquery.extract_data(contract, data)
        elif file.endswith("dexscreener.json"):
            dexscreener.extract_data(contract, data)
        elif file.endswith("holders.json"):
            holders.extract_data(contract, data)
        elif file.endswith("transactions_summary.json"):
            transactions_summary.extract_data(contract, data)
        elif file.endswith("transactions.json"):
            transactions.extract_data(contract, data)
        elif file.endswith("honeypot_is.json"):
            honeypot.extract_data(contract, data)

    return contract


def save_csv(contracts: list[Contract]):
    df = DataFrame(contracts)
    df.to_csv("contracts.csv", encoding="utf-8")


def extract_files(prefix: str):
    files = buckets.list_files("data-wrangler", "ethereum")
    file_names = [file.name for file in files]
    address_files = get_address_files(file_names)
    print(f"{len(address_files.keys())} addresses found")
    contracts = []
    count = 0
    for address in address_files:
        print(f"Loading {count}")
        contract = extract_data(address, address_files[address])
        contracts = [*contracts, contract]
        count += 1
        if count > 2:
            break
    save_csv(contracts)

if __name__ == '__main__':
    extract_files("ethereum")