import random


def initialize_game():
    count = dict()
    count['rounds'] = 0
    count['user'] = 0
    count['computer'] = 0

    while True:
        count['rounds'] = 1 + count.get('rounds', 0)
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)

        print(f"\nYou chose {user_action}, computer chose {computer_action}.")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
                count['user'] = 1 + count.get('user', 0)
            else:
                print("Paper covers rock! You lose.")
                count['computer'] = 1 + count.get('computer', 0)

        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
                count['user'] = 1 + count.get('user', 0)
            else:
                print("Scissors cuts paper! You lose.")
                count['computer'] = 1 + count.get('computer', 0)

        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
                count['user'] = 1 + count.get('user', 0)
            else:
                print("Rock smashes scissors! You lose.")
                count['computer'] = 1 + count.get('computer', 0)
        play_again = input(f"\n Play again? (y/n): \n")
        if play_again.lower() != 'y':
            print_scores(count)
            break


def print_scores(count):
    for key, value in count.items():
        print(f"{key.title()} : {value}")


def main():
    initialize_game()


if __name__ == '__main__':
    main()
