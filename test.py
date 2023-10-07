prices = [7, 2, 5, 12, 4, 3, 1, 15]
ii = []
pricee = []

for i, price in reversed(list(enumerate(prices[1:], 1))):
    ii.append(i)
    pricee.append(price)

print(ii)
print(pricee)
