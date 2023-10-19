def decimal_to_binary(decimal):
    """Converts a decimal number to binary."""
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    """Converts a decimal number to octal."""
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    """Converts a decimal number to hexadecimal."""
    return hex(decimal)[2:]

#Main Program

def main():
    """Main function for user interaction."""
    try:
        user_input = int(input("Enter a decimal number: "))
        conversion_choice = int(input("Choose conversion:\n1. Decimal to Binary\n2. Decimal to Octal\n3. Decimal to Hexadecimal\n"))

        if conversion_choice == 1:
            result = decimal_to_binary(user_input)
        elif conversion_choice == 2:
            result = decimal_to_octal(user_input)
        elif conversion_choice == 3:
            result = decimal_to_hexadecimal(user_input)
        else:
            print("Invalid input. Please try again.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

if __name__ == "__main__":
    main()
