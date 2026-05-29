def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_strong_number(number: int) -> bool:
    """Return True if the number is a strong number."""
    original = number
    total = 0
    while number > 0:
        digit = number % 10
        total += factorial(digit)
        number //= 10

    return total == original


if __name__ == "__main__":
    try:
        value = int(input("Enter a number: ").strip())
        if value < 0:
            print("Strong numbers are defined for non-negative integers only.")
        elif is_strong_number(value):
            print(f"{value} is a strong number.")
        else:
            print(f"{value} is not a strong number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
