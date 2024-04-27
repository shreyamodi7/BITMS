def print_E(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * (n-1))
        elif i == n//2:
            print('*' * (n//2))
        else:
            print('*')

# Example usage with n=5
print_E(5)