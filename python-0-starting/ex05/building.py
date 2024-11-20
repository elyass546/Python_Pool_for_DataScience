import sys
import string


# Need to check the carriage return
def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) <= 2:
        # Initialize counters for each character type
        uppercase_count = 0
        lowercase_count = 0
        punctuation_count = 0
        digit_count = 0
        space_count = 0
        total_count = 0

        # Get the argument passed to the script
        if len(sys.argv) <= 1:
            argument = input("What is the text to count?\n")
        else:
            argument = sys.argv[1]

        for char in argument:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                space_count += 1
            elif char in string.punctuation:
                punctuation_count += 1
        total_count = (
            uppercase_count + lowercase_count +
            punctuation_count + space_count + digit_count)

        print(f"The text contains {total_count} characters:")
        print(f"{uppercase_count} upper letters")
        print(f"{lowercase_count} lower letters")
        print(f"{punctuation_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
