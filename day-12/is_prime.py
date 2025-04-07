def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Eliminate even numbers
    
    # Check for factors from 3 to √n
    for i in range(3, int(n**0.5) + 1, 2):  # Skip even numbers
        if n % i == 0:
            return False
    
    return True

# Example usage
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False