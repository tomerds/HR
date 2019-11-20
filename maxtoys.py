def maximumToys(prices, k):

    newprices = []

    for i in range(len(prices)):
        if prices[i] < k:
            newprices.append(prices[i])

    newprices.sort()
    count = 0
    sum = 0
    for i in range(len(newprices)):
        sum += newprices[i]
        if sum < k:
            count += 1
        else:
            break


    return count



print(maximumToys([1, 12, 5, 111, 200, 1000, 10],70))