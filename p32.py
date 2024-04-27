def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_magical_prime(n):
    if is_prime(n):
        reverse_n = int(str(n)[::-1])
        if is_prime(reverse_n):
            return True
    return False

# Example usage:
number = 17
if is_magical_prime(number):
    print(f"{number} is a magical prime.")
else:
    print(f"{number} is not a magical prime.")