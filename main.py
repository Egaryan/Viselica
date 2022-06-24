import random
from words import wordList


def getWords():
    word = random.choice(wordList)
    return word.upper()


def displayViselica():


    s1 = ["|" + " " * 3, "", "\n"]
    s2 = ["|" + " " * 2, "", "", "", "\n"]
    s3 = ["|" + " " * 2, "", " ", "", ""]

    top = """
+---+
|   |
"""
    bott = """
|
|______
  """

    def human(tries):

        if tries == 6:
            print("")
        elif tries == 5:
            s1[1] = "O"
        elif tries == 4:
            s2[1] = "/"
        elif tries == 3:
            s2[2] = "|"
        elif tries == 2:
            s2[3] = "\\"
        elif tries == 1:
            s3[1] = "/"
        elif tries == 0:
            s3[3] = "\\"

        if tries > 0:
            print(top + "".join(s1) + "".join(s2) + "".join(s3) + bott)

    return human


def game(word):
    wordDisplay = "*" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    display_viselica = displayViselica()
    print("Сыграем в виселицу!")
    print(display_viselica(tries))
    print(wordDisplay)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Угадай букву или слово: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("Вы уже угадали букву: ", guess)
            elif guess not in word:
                print(guess, " этого нет в слове")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print(guess, " Есть в слове")
                guessedLetters.append(guess)
                wordAsList = list(wordDisplay) ########### накосячил с чем-то
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordDisplay = "".join(wordAsList)
                if "*" not in wordDisplay:
                    guessed = True ################

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("Ты уже угадал слово", guess)
            elif guess != word:
                print(guess, "Это не то слово")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordDisplay = word

        else:
            print("Введите БУКВУ или корректное слово")

        print(display_viselica(tries))
        print(wordDisplay)
        print("\n")
    if guessed:
        print("Поздравляю, вы угадали слово")
    else:
        print("У вас кончились попытки. Слово:" + word)


def main():
    word = getWords()
    game(word)
    while input("Сыграть снова? (Y/N) ").upper() == "Y":
        word = getWords()
        game(word)



main()