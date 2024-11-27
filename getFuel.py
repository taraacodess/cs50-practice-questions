def get_fuel_fraction():
    while True:
        try:
            # Prompt the user for input
            fraction = input("Enter the fuel amount as a fraction (X/Y): ")

            # Split the input into numerator and denominator
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)

            # Check for division by zero
            if denominator == 0:
                print("Denominator cannot be zero. Please try again.")
                continue

            # Check if the numerator is greater than the denominator
            if numerator > denominator:
                print("Numerator cannot be greater than denominator. Please try again.")
                continue

            # Return the fraction as a tuple if valid
            return numerator, denominator

        except ValueError:
            # Handle non-integer input or invalid fraction
            print("Invalid input. Please enter a valid fraction in the form X/Y, where X and Y are integers.")


def calculate_percentage(numerator, denominator):
    # Convert the fraction to a percentage
    return (numerator / denominator) * 100


def main():
    # Step 1 and 2: Get a valid fuel fraction from the user
    numerator, denominator = get_fuel_fraction()

    # Step 3: Convert the fraction to percentage
    percentage = calculate_percentage(numerator, denominator)

    # Step 4: Output based on special cases and rounded percentage
    if percentage <= 1:
        print("E")  # Output E if 1% or less remains
    elif percentage >= 99:
        print("F")  # Output F if 99% or more remains
    else:
        print(f"{round(percentage)}%")  # Output the percentage, rounded to the nearest integer

main()