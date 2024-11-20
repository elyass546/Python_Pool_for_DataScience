from ft_filter import ft_filter
import sys


def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad1")
        return

    input_string = sys.argv[1]
    provided_len = sys.argv[2]

    # Validate if the second argument is a digit (valid length)
    if not provided_len.isdigit():
        print("AssertionError: the arguments are bad2")
        return

    provided_len = int(provided_len)

    # Split the input string into a list of words
    splited_string = input_string.split(' ')

    # Use ft_filter to filter words based on length
    result = list(ft_filter(
                    lambda word: string_checker(word, provided_len),
                    splited_string))

    print(result)


def string_checker(word, pro_len):
    """
        Checks if the length of the word is
        greater than or equal to the provided length.
    """
    return len(word) >= pro_len


if __name__ == "__main__":
    main()
