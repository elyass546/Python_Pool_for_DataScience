import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    
    argument = sys.argv[1]
    if not all(char.isalnum() or char.isspace() for char in argument):
        print("AssertionError: the arguments are bad")
        return
    
    morse_code_dict = {
        'A': '.- ', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..',
        
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

        ' ': '/'  # Space between words in Morse code
    }

    result = ' '.join(morse_code_dict.get(char.upper(), '') for char in argument)
    
    print(result)

if __name__ == "__main__":
    main()