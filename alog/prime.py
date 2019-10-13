import math
def isPrime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        k=int(math.sqrt(n))
        print(k)
        for i in range(2,k+1):
            if(n%i==0):
                return False
        return True


primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
