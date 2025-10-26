def count_unsafe(L, R):
    count = 0
    for i in range(L, R + 1):
        s = str(i)
        if s[0] == s[-1]:
            count += 1
    return count


if __name__ == "__main__":
    L, R = 10, 25
    print(count_unsafe(L, R))  # Output: 2
