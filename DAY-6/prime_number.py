"""Program to check Prime Number or not."""
def is_prime(num):
    """Function to check whether a number is prime or not."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i + 2) == 0:
            return False
        i = i + 6
    return True
