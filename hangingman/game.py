import random
import string

from os.path import abspath, dirname, join

WORDS = ["dog", "table", "fish", "books", "vertigo"]


class HangingmanEngine:

    levels = {"easy": (4, 5, 6),
              "normal": (7, 8, 9),
              "hard": (10, 11, 12),
              "harder": (13, 14, 15)}

    def __init__(self, level):
        self.level = str(level)
        self.words = type(self).levels[self.level]
        self.chances = 5

    def guess_word(self):
        word_length = random.choice(self.words)
        word = [x.upper() for x in self.select_word(word_length)]
        player_matches = [None for char in word]
        player_guesses = set()

        while 1:
            print(word, player_matches, sorted(list(player_guesses)), self.chances)
            guess = self.take_a_guess()
            if guess in word:
                matches = [i for i, _ in enumerate(word) if _ == guess]
                for m in matches:
                    player_matches[m] = guess
            else:
                player_guesses.add(guess)
                self.chances -= 1
            if self.chances == 0:
                return self.game_over()
            if player_matches == word:
                return self.game_won()

    def select_word(self, length):
        words_file_name = str(length) + ".txt"
        words_file_path = abspath(
            join(dirname(__file__), "data", words_file_name))
        num_words = file_len(words_file_path)
        with open(words_file_path, "r") as f:
            line = random.randint(1, num_words)
            for i, l in enumerate(f):
                if i == line:
                    return l.strip()

    def take_a_guess(self):
        letter = ""
        while letter not in string.ascii_letters or len(letter) != 1:
            letter = input("> ")
        return letter.upper()

    def game_over(self):
        print("Game over")

    def game_won(self):
        print("Game won")

    def play_game(self):
        self.guess_word()


def file_len(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


if __name__ == "__main__":
    game = HangingmanEngine("easy")
    game.play_game()
