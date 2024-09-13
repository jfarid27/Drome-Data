import pandas as pd
from time import sleep
from Sugar.models.Sugar import Sugar

def fetch_all_pools(sugar_address: str, limit: int= 10, debug=False):
    """
    Fetches all liquidity pools from the given sugar address.

    Args:
        sugar_address (str): The address of the sugar contract.
        limit (int, optional): The maximum number of pools to fetch in each iteration. Defaults to 10.
        debug (bool, optional): If set to True, the function will stop after 20 iterations for debugging purposes. Defaults to False.

    Returns:
        list: A list of liquidity pool addresses.
    """
    sugar = Sugar(sugar_address)
    current = 0
    final = False
    lp_addresses = []
    pools = []
    while (not final):
        if debug and current > 20:
            break
        if len(pools) < limit:
            final = True
        pools = sugar.fetch_pools(current, limit=limit)
        lp_addresses.append(pools)
    return lp_addresses