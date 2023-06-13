def rod_cutting(lengths, prices, n):
    revenue = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            revenue[i] = max(revenue[i], prices[j] + revenue[i - j - 1])

    return revenue[n]

# Example usage:
lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 4

max_revenue = rod_cutting(lengths, prices, rod_length)
print("Maximum revenue:", max_revenue)

