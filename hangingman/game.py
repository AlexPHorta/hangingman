import random
import string


WORDS = ["dog", "table", "fish", "books", "vertigo"]


class HangingmanEngine:
    
    def guess_word(self):
        chances = 3
        word = [x.upper() for x in self.select_word()]
        player_matches = [None for char in word]
        player_guesses = set()
        
        while 1:
            print(word, player_matches, sorted(list(player_guesses)), chances)
            guess = self.take_a_guess()
            if guess in word:
                matches = [i for i, _ in enumerate(word) if _ == guess]
                for m in matches:
                    player_matches[m] = guess
            else:
                player_guesses.add(guess)
                chances -= 1
            if chances == 0: return self.game_over()
            if player_matches == word: return self.game_won()
    
    def select_word(self):
        return random.choice(WORDS)
    
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


if __name__ == "__main__":
    game = HangingmanEngine()
    game.play_game()
