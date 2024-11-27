def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if the length is between 2 and 6 characters
    if len(plate) < 2 or len(plate) > 6:
        return False
    
    # Check if the first two characters are letters
    if not plate[:2].isalpha():
        return False
    
    # Check if the plate contains only alphanumeric characters (no periods, spaces, or punctuation marks)
    if not plate.isalnum():
        return False
    
    # Find where the digits start, if any
    for i in range(2, len(plate)):
        if plate[i].isdigit():
            # Ensure no letter appears after the first number
            if not plate[i:].isdigit():
                return False
            # Ensure the first number is not '0'
            if plate[i] == '0':
                return False
            break

    # All checks passed, return True
    return True


main()
