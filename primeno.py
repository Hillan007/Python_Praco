def is_prime(num):
    # Prime numbers are greater than 1
    if num < 2:
        return False
    # Check divisibility from 2 up to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print prime numbers between 2 and 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
