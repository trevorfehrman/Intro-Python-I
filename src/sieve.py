import math

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes


def sieve(n):

    sieve_list = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (sieve_list[p] == True):
            for i in range(p * 2, n+1, p):
                sieve_list[i] = False
        p += 1

    for p in range(2, n):
        if sieve_list[p]:
            print(p)


sieve(30)
