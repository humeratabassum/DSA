class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0  # Track total gas balance for the entire journey
        current_gas = 0  # Track current gas balance for the current journey
        start = 0  # Starting index for the journey
        
        # Traverse each station
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]  # Update the total gas balance
            current_gas += gas[i] - cost[i]  # Update the current gas balance
            
            # If the current gas balance falls below 0, reset the starting station
            if current_gas < 0:
                start = i + 1  # Set the next station as the new starting station
                current_gas = 0  # Reset the current gas balance
        
        # If total gas is non-negative, we can complete the circuit
        return start if total_gas >= 0 else -1

        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        