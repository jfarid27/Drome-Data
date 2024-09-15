import json
from ape import Contract
from eth_utils import from_wei

class Sugar:
    def __init__(self, contract_address:str,
                 abi_file:str="Sugar/contracts/SugarAPI.json"):
        self.contract = Contract(contract_address, abi=abi_file)
    
    def fetch_pools(self, offset=0, limit=10):
        """Return the balance of the given address."""
        params = [limit, offset]
        results = self.contract.all(*params)
        return results
