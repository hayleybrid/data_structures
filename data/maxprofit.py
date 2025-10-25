def max_profit(cost, sell, K):
    n = len(cost)
    items = []

    # compute gain for each item, keep only profitable ones
    for i in range(n):
        gain = sell[i] - cost[i]
        if gain > 0:
            items.append((cost[i], gain))

    # sort by cost (ascending)
    items.sort(key=lambda x: x[0])

    capital = K
    for c, g in items:
        if capital >= c:
            capital += g
        else:
            break

    return capital - K


if __name__ == "__main__":
    cost = [5, 10, 3, 12]
    sell = [7, 15, 3, 20]
    K = 5
    print(max_profit(cost, sell, K))  # prints 2
