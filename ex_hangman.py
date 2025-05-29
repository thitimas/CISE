import random

words_with_hints = [
    ('algorithm', 'A step-by-step procedure for solving a problem'),
    ('encryption', 'The process of converting information into a secret code'),
    ('syntax', 'Rules that define how code should be written'),
    ('firewall', 'A network security system that monitors traffic'),
    ('phishing', 'A scam involving fraudulent emails or messages'),
    ('compiler', 'Translates source code into machine code'),
    ('database', 'Organized collection of data accessible electronically'),
    ('bandwidth', 'The amount of data transmitted in a fixed amount of time'),
    ('recursion', 'A function that calls itself'),
    ('latency', 'A delay before a transfer of data begins'),
    ('iteration', 'The repetition of a process or set of instructions'),
    ('debugging', 'The process of identifying and fixing errors in code'),
    ('protocol', 'A set of rules for data communication'),
    ('router', 'Device that directs data packets between networks'),
    ('malware', 'Software designed to disrupt or damage a system'),
    ('cache', 'Stored data used to speed up future requests'),
    ('token', 'A single element of a programming language syntax'),
    ('variable', 'A symbolic name for a piece of data'),
    ('function', 'A reusable block of code that performs a task'),
    ('boolean', 'A data type with two possible values: true or false')
]



MAX_LIVES = 6

def play():
    word, hint = pick_a_word()
    lives_remaining = MAX_LIVES
    guessed_letters = set()
    score = 0

    print("Hint: " + hint)

    while lives_remaining > 0:
        print_word_with_blanks(word, guessed_letters)
        print(f"Lives Remaining: {lives_remaining} | Score: {score}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        guess = input('Guess a letter or the whole word: ').strip().lower()

        if not guess:
            print("Empty input. Try again.")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            guessed_letters.add(guess)
            if guess in word:
                print("Good guess!")
                score += 1
            else:
                print("Wrong guess.")
                lives_remaining -= 1
        elif guess == word:
            print("Correct! You guessed the word!")
            score += 5
            break
        else:
            print("Wrong word.")
            lives_remaining -= 1

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed all the letters!")
            score += 5
            break

    print(f"The word was: {word}")
    print(f"Final Score: {score}")

def pick_a_word():
    return random.choice(words_with_hints)

def print_word_with_blanks(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '-' for letter in word])
    print(f"Word: {display}")

play()
