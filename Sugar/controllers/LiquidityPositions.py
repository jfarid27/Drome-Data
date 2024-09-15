import pandas as pd
from time import sleep
from Sugar.models.Sugar import Sugar

def fetch_all_pools(sugar_address: str, limit: int= 10, debug=False):
    """
    Fetches all liquidity pools from the given sugar address and returns raw data from Sugar contract.

    Args:
        sugar_address (str): The address of the sugar contract.
        limit (int, optional): The maximum number of pools to fetch in each iteration. Defaults to 10.
        debug (bool, optional): If set to True, the function will stop after 20 iterations for debugging purposes. Defaults to False.

    Returns:
        list: A list of liquidity pool tuple data from address.
    """
    sugar = Sugar(sugar_address)
    current = 0
    final = False
    lp_responses = []
    current_pool = []
    while (not final):
        if debug and current > 20:
            break
        if len(current_pool) < limit:
            final = True
        current_pool = sugar.fetch_pools(current, limit=limit)
        lp_responses += current_pool
    return lp_responses

def fetch_pools(sugar_address: str, limit: int= 10, debug=False):
    """
    Fetches liquidity pools for a given sugar address.

    Args:
        sugar_address (str): The address of the sugar to fetch pools for.
        limit (int, optional): The maximum number of pools to fetch. Defaults to 10.
        debug (bool, optional): If True, enables debug mode. Defaults to False.

    Returns:
        pd.DataFrame: A DataFrame containing the fetched liquidity pools with columns:
            - 'pool_address': The address of the liquidity pool.
            - 'symbol': The symbol of the liquidity pool.
            - 'token0': The first token in the liquidity pool.
            - 'token1': The second token in the liquidity pool.
    """
    lp_responses = fetch_all_pools(sugar_address, limit=limit, debug=debug)
    rows = []
    for pool in lp_responses:
        row = { 'pool_address': pool['lp'], 'symbol': pool['symbol'],'token0': pool['token0'], 'token1': pool['token1'] }
        rows.append(row)

    return pd.DataFrame(rows)