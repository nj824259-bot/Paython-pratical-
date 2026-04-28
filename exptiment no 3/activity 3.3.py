def total_stairs_climbed(n: int) -> int:
    """
    Calculates the number of distinct ways to climb a staircase of n steps,
    where you can climb 1 or 2 steps at a time.

    Args:
        n: The total number of steps in the staircase.

    Returns:
        The number of distinct ways to reach the top.
    """
    # Base cases:
    # If there are 0 steps, there is one way (you are already at the top).
    if n == 0:
        return 1
    # If there is 1 step, there is only one way (take 1 step).
    elif n == 1:
        return 1
    # If n is negative, it's an invalid state, return 0 ways.
    elif n < 0:
        return 0
    
    # Recursive case:
    # The total ways to reach step n is the sum of ways to reach step n-1
    # and the ways to reach step n-2.
    else:
        return total_stairs_climbed(n - 1) + total_stairs_climbed(n - 2)

