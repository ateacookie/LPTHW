import ex46

mydata = [501, 207, 349, 67, 83, 14579, 839]
result = []
for num in mydata:
    result.append((num, ex46.isprime(num)))

print result
