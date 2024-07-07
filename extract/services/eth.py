from web3 import Web3

from services import Chain, get_chain


def is_contract(self, chain_name: str, address: str) -> bool:
    chain = get_chain(chain_name)
    web3client = Web3(provider=Web3.HTTPProvider(chain.rpc_url))
    checksum_address = Web3.to_checksum_address(address)
    code = web3client.eth.get_code(checksum_address)
    return code is not None and code.hex() != "0x"
