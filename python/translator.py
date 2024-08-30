import sys

numbers = { '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...' }

'''
NOTE:
    The unit tests use the following mappings for the numbers, so some of the tests may fail:
    
    { '0': 'O.....', '1': 'O.O...', '2': 'OO....', '3': 'OO.O..', '4': 'O..O..', '5': 'OOO...', '6': 'OOOO..', '7': 'O.OO..', '8': '.OO...', '9': '.OOO..' }

    I have based my implementation on the Wikipedia page and the image provided in the task description, which uses the following mappings:
    
    { '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...' }
'''

letters = {
    'a': 'O.....', 'b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..','i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.','m': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.','u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO','y': 'OO.OOO','z': 'O..OOO', ' ': '......'
}

capital_follows = '.....O'
number_follows = '.O.OOO'

def is_braile(text):
    # Checks if the first argument is valid braille text
    for letter in text:
        if letter not in ['O', '.']:
            return False
    return True

def to_braile(arguments):
    phrase = ' '.join(arguments)
    result = []
    
    for i in range(len(phrase)):
        if phrase[i].isupper():
            result.append(capital_follows)
            result.append(letters[phrase[i].lower()])
        elif phrase[i].isdigit():
            # Check if we have added an indicator already
            if i > 0 and phrase[i-1] == ' ':
                result.append(number_follows)
            result.append(numbers[phrase[i]])
        else:
            result.append(letters[phrase[i]])
    
    return ''.join(result)

def to_alphabet(text):
    # Reverse the dictionaries for easier lookup
    reversed_numbers = {v: k for k, v in numbers.items()}
    reversed_letters = {v: k for k, v in letters.items()}
    
    # Split the braille text into alphanumeric characters
    words = []
    for i in range(0, len(text), 6):
        words.append(text[i:i+6])
    
    is_capital = False
    is_number = False
    
    result = []
    curr_word = ''
    
    for i in range(len(words)):
        if words[i] == capital_follows:
            is_capital = True
            continue
        elif words[i] == number_follows:
            is_number = True
            continue
        
        if is_number:
            curr_word += reversed_numbers[words[i]]
        elif is_capital:
            curr_word += reversed_letters[words[i]].upper()
            is_capital = False
        else:
            curr = reversed_letters[words[i]]
            if curr == ' ':
                is_number = False
                result.append(curr_word)
                curr_word = ''
            else:
                curr_word += curr
                
    if curr_word:
        result.append(curr_word) 
    
    return ' '.join(result)


def main():
    # Only runs the code if there is an argument
    if len(sys.argv) < 2:
        print("Incorrect usage, please provide an argument")
        sys.exit(1)
    
    # Get the arguments without the script name
    arguments = sys.argv[1:]
    
    # Convert to either braille or alphabet based on the input type
    result = to_alphabet(arguments[0]) if is_braile(arguments[0]) else to_braile(arguments)
    
    print(result)

if __name__ == '__main__':
    main()
    