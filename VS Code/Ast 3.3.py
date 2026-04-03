def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for k in range(2, 102):
    if is_prime(k):
        prime_numbers.append(k)

x = int(input(""))

output = []
for i in prime_numbers:
    n = 1
    while x % (i ** n) == 0:
        n += 1
    if n > 1:
        output.append(f"{i} {n - 1}")
print("\n".join(output), end="")
