def getPrimeNumbers(n):
    """
    Returns a list containing all prime numbers between 2 and n.
    """
    def isPrime(num):
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    primes = [x for x in range(2, n + 1) if isPrime(x)]
    return primes

n = int(input("Enter a number: "))
print("Prime numbers between 2 and", n, "are:", getPrimeNumbers(n))

        

