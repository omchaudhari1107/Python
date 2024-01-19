# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [7, 1, 5, 3, 6, 4]


def MaxProfit(lst):
    min_sorted = sorted(lst, reverse=True)
    buy = min_sorted[len(min_sorted) - 1]
    for i in range(len(lst) - 1):
        if buy == lst[i]:
            Oli_min = i
    max_sorted = sorted(lst[Oli_min : len(lst)])
    sell = max_sorted[len(max_sorted) - 1]
    # print(buy,sell)
    profit = sell - buy
    return profit


print(MaxProfit(prices))
