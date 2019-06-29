# guessing game.

secret_word = "sphynx"
guess = ""
count = 0

while guess != secret_word:
    guess = input("Enter your guess: ")
    count += 1

if guess == secret_word and count == 0:
    print("You won in one guess!")
else:
    print("You won in " + str(count) + " guesses!")
