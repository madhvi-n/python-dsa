import random
from rich import print


words = [
    "awake",
    "blush",
    "focal",
    "evade",
    "serve",
    "grade",
    "quiet",
    "ocean",
    "dream",
    "drawn",
    "rapid",
    "pitch"
]


class Wordle:
    def __init__(self):
        self.word = random.choice(words)
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "] * 5,
            1: [" "] * 5,
            2: [" "] * 5,
            3: [" "] * 5,
            4: [" "] * 5,
            5: [" "] * 5,
        }

    def draw(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("----" * (len(self.word) - 1))

    def user_input(self):
        user_guess = input("enter a 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input("Invalid input. Enter a 5 letter word: ")

        user_guess = user_guess.lower()
        for index, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[index]:
                    char = f"[green]{char.upper()}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.num_guesses][index] = char

        self.num_guesses += 1
        return user_guess

    def play(self):
        while True:
            self.draw()
            user_guess = self.user_input()
            if user_guess == self.word:
                self.draw()
                print(f"[green]You won. The word was {self.word}[/]")
                break

            if self.num_guesses > 5:
                self.draw()
                print(f"[red]You lost! The word was {self.word}[/]")
                break


def main():
    game = Wordle()
    game.play()


if __name__ == '__main__':
    main()
