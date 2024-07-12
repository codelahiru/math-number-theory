import matplotlib.pyplot as plt

def generalized_sequence(n, a, b):
    steps = 0
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = a * n + b
        sequence.append(n)
        steps += 1
        if steps > 1000:  # Add a step limit to prevent infinite loops
            break

    return sequence, steps


# Test the function with specific parameters
n = int(input("Enter a positive integer to test the generalized sequence: "))
a = int(input("Enter the multiplier (a): "))
b = int(input("Enter the constant (b): "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    sequence, steps = generalized_sequence(n, a, b)

    # Plot the sequence
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title(f'Generalized Sequence for Starting Number {n} ({a}x + {b})')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.yscale('log')  # Use a logarithmic scale for better visualization of large values
    plt.grid(True)
    plt.show()

    print(f"Starting number: {n}")
    print(f"Sequence: {sequence}")
    print(f"Total steps to reach 1 or stop: {steps}")
