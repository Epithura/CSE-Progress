"""
a=2
for i in range(3,1000):
    for j in (2,i):
        if i%j==0:
            break
        else:a=a+i
print(a)
"""
def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_first_n_primes(n):
    """Calculate the sum of the first n prime numbers."""
    count = 0
    num = 2
    prime_sum = 0

    while count < n:
        if is_prime(num):
            prime_sum += num
            count += 1
        num += 1

    return prime_sum

# Calculate the sum of the first 1000 primes
sum_primes = sum_of_first_n_primes(1000)
print("The sum of the first 1000 prime numbers is:", sum_primes)

