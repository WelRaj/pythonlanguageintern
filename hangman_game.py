import random


words = ['apple', 'house', 'river', 'chair', 'snake']
word = random.choice(words)

tries = 6   
guesses = []  

hidden = []
for letter in word:
    hidden.append("_")

print("Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have", tries, "wrong tries.\n")


while tries > 0 and "_" in hidden:
    print("Word: ", " ".join(hidden))
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("You already guessed that.\n")
        continue

    guesses.append(guess)

    if guess in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
    else:
        print("Wrong guess!\n")
        tries -= 1
        print("Tries left:", tries, "\n")


if "_" not in hidden:
    print("You win! The word was:", word)
else:
    print("You lost. The word was:", word)
