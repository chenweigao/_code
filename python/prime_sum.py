def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 10

n_prime = [_ for _ in range(n + 1) if isPrime(_)]

count = 0

for i in n_prime:
    if n - i in n_prime and i <= n - i:
        count += 1

print(count)