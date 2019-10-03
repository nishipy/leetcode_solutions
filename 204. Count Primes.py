class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        else:
            primes = [True]*n
            primes[0] = False
            primes[-1] = False
            for i in range(2, int(n**(0.5))+1):
                for j in range(2, n//i + 1):
                    primes[i*j - 1] = False
            return sum(primes)