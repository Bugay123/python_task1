def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through each character in the Roman numeral string
    for char in reversed(s):
        current_value = roman_map[char]

        # If the current numeral is smaller than the previous one, subtract its value
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        # Update previous value
        prev_value = current_value

    return total

def convert_roman_numbers():
    while True:
        roman_input = input("Enter a Roman numeral (or 'q' to quit): ").upper()

        # Exit the loop if the user wants to quit
        if roman_input == 'Q':
            print("Exiting the program.")
            break

        # Validate if the input is a valid Roman numeral
        if all(char in 'IVXLCDM' for char in roman_input):
            result = romanToInt(roman_input)
            print(f"The integer value of {roman_input} is {result}.")
        else:
            print("Invalid Roman numeral. Please try again.")

# Call the function to start converting numbers
convert_roman_numbers()
