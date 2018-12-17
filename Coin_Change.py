#  Coin Change

#  This problem is common enough that is actually has its own Wikipedia Entry! Let's check the problem statement again:

# This is a classic recursion problem: Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

# For example:

# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

# 1+1+1+1+1+1+1+1+1+1

# 5 + 1+1+1+1+1

# 5+5

# 10

# With 1 coin being the minimum amount.


# Solution¶
# This is a classic problem to show the value of dynamic programming. We'll show a basic recursive example and show why it's 
# actually not the best way to solve this problem.

# Make sure to read the comments in the code below to fully understand the basic logic!


def rec_coin(target,coins):
    '''
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change
    
    Note, this solution is not optimized.
    '''
    
    # Default to target value
    min_coins = target
    
    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1
    
    else:
        
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive Call (add a count coin and subtract from the target) 
            num_coins = 1 + rec_coin(target-i,coins)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                
                min_coins = num_coins
                
    return min_coins


# Dynamic Programming Solution¶
def rec_coin_dynam(target,coins,known_results):
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)
    
    OUTPUT: Minimum number of coins needed to make the target.
    '''
    
    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
                
    return min_coins