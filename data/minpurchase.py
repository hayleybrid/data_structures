def min_purchases_for_candles(stack, K):
    """
    Returns the minimum number of boxes Mary must buy from the top
    so that she has at least one copy of each candle 1..K.
    If impossible (some number in 1..K not present), returns -1.

    :param stack: list[int] representing the stack from top (index 0) to bottom
    :param K: highest numbered candle Mary needs (needs 1..K)
    :return: minimal number of boxes to buy, or -1 if impossible
    """
    if K <= 0:
        return 0  # nothing required

    seen = [False] * (K + 1)  # index 0 unused
    remain = K  # number of distinct required candles still needed

    for i, val in enumerate(stack):
        if 1 <= val <= K:
            if not seen[val]:
                seen[val] = True
                remain -= 1
                if remain == 0:
                    # i is 0-based; number of purchases is i+1
                    return i + 1
        # ignore irrelevant values outside 1..K

    # some required candles missing
    return -1


# Example driver
if __name__ == "__main__":
    stack1 = [2, 5, 1, 3, 2, 4]  # top is index 0
    print(min_purchases_for_candles(stack1, 4))  # Output: 6

    stack2 = [1, 2, 3]
    print(min_purchases_for_candles(stack2, 3))  # Output: 3

    stack3 = [2, 2, 2]
    print(min_purchases_for_candles(stack3, 2))  # Output: -1
