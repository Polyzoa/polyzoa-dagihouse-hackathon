from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class Contract:
    chain: str | None = None
    address: str | None = None
    name: str | None = None
    symbol: str | None = None
    decimals: int | None = None
    contract_type: int | None = None
    holder_count: int | None = None
    token_age: int | None = None
    total_supply: int | None = None
    rate_of_failed_transactions: float | None = None
    max_transaction_value: int | None = None
    transaction_frequency: float | None = None
    liquidity_pool_size: int | None = None
    avg_transaction_value: float | None = None
    small_transactions_ratio: float | None = None
    number_of_pool_interactions: int | None = None
    owner_percentage_holding: int | None = None
    creator: str | None = None
    creator_contract_type: bool | None = None
    creator_percentage_holding: int | None = None
    creation_date: str | None = None
    owner_type_contract: bool | None = None
    is_blacklisted: bool | None = None
    is_honeypot: bool| None = None
    transaction_number: int | None = None
    is_open_source: bool| None = None
    has_pair: bool | None = None
