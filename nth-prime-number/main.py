def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    count = 0
    number = 1
    while count < n:
        number = number + 1
        if is_prime(number):
            count = count + 1
    return number

# Find the 100th prime number
hundredth_prime = find_nth_prime(100)
print("The 100th prime number is:", hundredth_prime)
