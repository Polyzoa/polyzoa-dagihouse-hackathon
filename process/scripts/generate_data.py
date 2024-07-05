import numpy as np
import pandas as pd

def generate_token_data(malicious=False):
    """
    Generate synthetic token data for malicious or non-malicious tokens.

    Features:
    - avg_transaction_value: Average value of transactions.
    - max_transaction_value: Maximum value of a single transaction.
    - transaction_frequency: Number of transactions per unit time.
    - liquidity_pool_size: Size of the liquidity pool.
    - holder_count: Total number of unique holders.
    - token_age: Time (in days) since the token was created.
    - high_contract_supply: Check if total supply is within a range.
    - rate_of_failed_transactions: Number of failed transactions divided by total transactions.
    - small_transactions_ratio: Very small transactions divided by total transactions.
    - number_of_pool_interactions: Number of interactions with the liquidity pool.
    - has_spam_name: Check if the name or symbol has a domain format.
    - owner_percentage_holding: Percentage of tokens held by the owner.
    - creator_percentage_holding: Percentage of tokens held by the creator.
    - creator_type_contract: True if the creator is a contract, false if it is an EOA.
    - owner_type_contract: True if the owner is a contract, false if it is an EOA.
    """
    avg_transaction_value = np.random.uniform(1, 100)
    max_transaction_value = avg_transaction_value + np.random.uniform(0, 50)
    transaction_frequency = np.random.randint(1, 1000)  # Simplified for now
    liquidity_pool_size = np.random.uniform(1, 10000)
    holder_count = np.random.randint(1, 10000)
    token_age = np.random.randint(1, 365)
    high_contract_supply = np.random.choice([True, False])
    rate_of_failed_transactions = np.random.uniform(0, 1)
    small_transactions_ratio = np.random.uniform(0, 1)
    number_of_pool_interactions = np.random.randint(1, 1000)
    has_spam_name = np.random.choice([True, False])
    owner_percentage_holding = np.random.uniform(0, 1)
    creator_percentage_holding = np.random.uniform(0, 1)
    creator_type_contract = np.random.choice([True, False])
    owner_type_contract = np.random.choice([True, False])

    # Create some dummy malicious data
    if malicious:
        avg_transaction_value = np.random.uniform(1, 1000)
        max_transaction_value = avg_transaction_value + np.random.uniform(0, 500)
        holder_count = np.random.randint(1, 1000)
        rate_of_failed_transactions = np.random.uniform(0.5, 1)
        small_transactions_ratio = np.random.uniform(0.5, 1)
        owner_percentage_holding = np.random.uniform(0.5, 1)
        creator_percentage_holding = np.random.uniform(0.5, 1)

    return [
        avg_transaction_value,
        max_transaction_value,
        transaction_frequency,
        liquidity_pool_size,
        holder_count,
        token_age,
        high_contract_supply,
        rate_of_failed_transactions,
        small_transactions_ratio,
        number_of_pool_interactions,
        has_spam_name,
        owner_percentage_holding,
        creator_percentage_holding,
        creator_type_contract,
        owner_type_contract,
        int(malicious)
    ]

def generate_dataframe(rows=50000, malicious_ratio=0.2):
    data = []
    malicious_count = int(rows * malicious_ratio)
    non_malicious_count = rows - malicious_count

    for _ in range(malicious_count):
        data.append(generate_token_data(malicious=True))

    for _ in range(non_malicious_count):
        data.append(generate_token_data(malicious=False))

    columns = [
        'avg_transaction_value',
        'max_transaction_value',
        'transaction_frequency',
        'liquidity_pool_size',
        'holder_count',
        'token_age',
        'high_contract_supply',
        'rate_of_failed_transactions',
        'small_transactions_ratio',
        'number_of_pool_interactions',
        'has_spam_name',
        'owner_percentage_holding',
        'creator_percentage_holding',
        'creator_type_contract',
        'owner_type_contract',
        'flag'
    ]

    df = pd.DataFrame(data, columns=columns)
    # df = df.head(5000) # for quick testing
    df.to_csv('data/token_data.csv', index=False)

    return df

if __name__ == "__main__":
    generate_dataframe()

