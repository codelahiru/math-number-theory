import matplotlib.pyplot as plt

def collatz_sequence(n):
    steps = 0
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1

    return sequence, steps


# Test the function with a specific number
n = int(input("Enter a positive integer to test the Collatz sequence: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sequence, steps = collatz_sequence(n)

    # Plot the sequence
    plt.figure(figsize=(12, 6))
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title(f'Collatz Sequence for Starting Number {n}')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.yscale('log')  # Use a logarithmic scale for better visualization of large values
    plt.grid(True)
    plt.show()

    print(f"Starting number: {n}")
    print(f"Sequence: {sequence}")
    print(f"Total steps to reach 1: {steps}")

