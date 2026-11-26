decimal_text = input("Enter a positive decimal number: ").strip()

try:
    decimal_number = int(decimal_text)
    if decimal_number <= 0:
        raise ValueError("The number must be positive")
except ValueError as error:
    print("Please enter a valid positive decimal integer.")
else:
    print("Binary:", bin(decimal_number))
    print("Hexadecimal:", hex(decimal_number))
