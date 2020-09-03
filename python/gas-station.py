class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas_remaining = 0
        past_total_remaining = 0
        starting_point = 0
        i = 0
        for g, c in zip(gas, cost):
            gas_remaining = g - c
            total_gas_remaining = total_gas_remaining + gas_remaining
            if gas_remaining < 0 and total_gas_remaining < 0:
                starting_point = i + 1
                past_total_remaining += total_gas_remaining
                total_gas_remaining = 0
            
            
            i = i + 1
            
        if total_gas_remaining + past_total_remaining >= 0:
            return starting_point
        
        return -1
# Whenever you reach a place where gas remaining is neg and total gas remaining is negative then choose the next starting point as there is a single unique solution 
