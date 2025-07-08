def sieve_of_eratosthenes(n: int) -> list[int]:
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False
    threeDivisors = []
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    primes = [p for p in range(2, n+1) if prime[p]]
    
    threeDivisors = [p * p for p in primes if p * p <= n]
    
    return threeDivisors
    
print(sieve_of_eratosthenes(20000))