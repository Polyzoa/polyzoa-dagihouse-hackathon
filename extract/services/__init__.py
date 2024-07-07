from dataclasses import dataclass
from enum import Enum


@dataclass
class Chain:
    name: str
    id: int | None
    rpc_url: str | None = None


class Chains(Enum):
    ETHEREUM = Chain(name="ethereum", id=1, rpc_url="https://rpc.ankr.com/eth")
    POLYGON = Chain(name="polygon", id=137, rpc_url="https://rpc.ankr.com/polygon")
    BINANCE = Chain(name="bsc", id=56, rpc_url="https://rpc.ankr.com/bsc")
    BASE = Chain(name="base", id=8453, rpc_url="https://rpc.ankr.com/base")
    OPTIMISM = Chain(name="optimism", id=10, rpc_url="https://rpc.ankr.com/optimism")
    AVALANCHE = Chain(name="avalanche", id=43114, rpc_url="https://rpc.ankr.com/avalanche")


def get_chain(name: str) -> Chain | None:
    return next((item.value for item in Chains if item.value.name == name), None)

