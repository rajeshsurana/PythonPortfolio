# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    primes = []
    last = 1
    
    while True:
        flag = True
        last += 1
        for p in primes:
           if (last % p) == 0:
               flag = False
               break
        if flag:
            primes.append(last)
            yield(last)

