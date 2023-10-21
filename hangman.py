# Random word and show random 2 letters
# Display hangman in ASCII
# Player inputs one letter at the time if letter does not exist in word
# than one head adds to the hangman body.
# If letter exist than this letters shows in the word and
# Player loses if he does not guess the word while hangman not shown completely
from random import choice, randint
hangman = [
    '''
     _______
    |       |
            |
            |
            |
            |
    ''',
    '''
     _______
    |       |
    O       |
            |
            |
            |
    ''',
     '''
     _______
    |       |
    O       |
    |       |
            |
            |
    ''',
      '''
     _______
    |       |
    O       |
    |\      |
            |
            |
    ''',
      '''
     _______
    |       |
    O       |
   /|\      |
            |
            |
    ''',
       '''
     _______
    |       |
    O       |
   /|\      |
   /        |
            |
    ''',
    
          '''
     _______
    |       |
    O       |
   /|\      |
   / \      |
            |
    ''',
]


words = ['Elephant', 'Butterfly', 'Furniture', 'Universe', 'Mountain', 'Telescope', 'Happiness', 'Adventure', 'Education', 'Chocolate']
# words = ['wod', 'let']
hidden_word = choice(words).lower()
lines = ['_' for _ in hidden_word]
inputed_letters = set()

def show_hangman(index):
    print(hangman[index])

def reset_game():
    global hidden_word
    global lines
    global inputed_letters
    hidden_word = choice(words).lower()
    lines = ['_' for _ in hidden_word]
    inputed_letters = set()

def check_word():
    # Check if hidden_word is guessed
    if '_' not in lines:
        return 1
    
def check_letter(letter):
    if len(letter) > 1 or letter.isnumeric() or letter == '': 
        return 0
    indexes = [i for i, l in enumerate(hidden_word) if l == letter]
    if letter in inputed_letters:
        return 1
    if not indexes:
        inputed_letters.add(letter)
        return -1
    else:
        for index in indexes:
            lines[int(index)] = letter

def print_word():
    for char in lines:
        print(char, end=' ')
    print()
    
def new_game():
    print('New game started...')
    print('Guess the word.')
    error_count = 0
    hidden_word = choice(words).lower()
    while check_word() != 1:
        print_word()
        show_hangman(error_count)
        letter = input('Enter a letter-> ')
        answ = check_letter(letter)
        if answ == -1:
            error_count += 1
            print(f'Errors: {error_count}')

        elif answ == 1:
            print(f'You already entered "{letter}"')
            print(f'Errors: {error_count}')

        elif answ == 0:
            print('Enter only one letter!')

        if check_word() == 1:
            print('You won!')
            print_word()    
            reset_game()
            return
        if error_count == len(hangman) - 1:
            print('You lost!')
            print(f'Hidden word was a "{hidden_word}"')
            reset_game()
            show_hangman(error_count)
            return
        
def main():
    game = True
    while game:
        var = input('Press any key to start a new game or "q" to exit -> ')    
        if var == 'q':
            game = False
        else:
            new_game()

if __name__ == '__main__':
    main()
    