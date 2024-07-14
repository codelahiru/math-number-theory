def is_divisible_by_all(number, divisors):
    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True

# List of numbers from 1 to 10
divisors = list(range(1, 11))
print(divisors)

# Start with the first natural number
number = 1

while True:
    if is_divisible_by_all(number, divisors):
        print(f"The first natural number that can be divided by each of the numbers from 1 to 10 without any remainder is: {number}")
        break
    number += 1