player_one_choice, player_two_choice = 0, 0
scores = [0, 0]


def confirm_continue(a):
    while True:
        choice = input(a)
        if choice == "":
            return True
        elif choice == "exit":
            return False
        else:
            print("If you want to continue, press enter. If you want to exit, type \'exit\'")


def correct_input_checker(player_name):
    while True:
        choice = input(f"{player_name}, your choice: ")
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)
        else:
            print("Wrong input. Please try again.")


def winner_checker(player_one_choice, player_two_choice):
    '''
    returns True when player one wins
    returns False when player two wins
    returns None when it's a tie
    '''
    if player_one_choice == player_two_choice:
        return None
    elif player_one_choice == 1 and player_two_choice == 3:
        return True
    elif player_one_choice == 2 and player_two_choice == 1:
        return True
    elif player_one_choice == 3 and player_two_choice == 2:
        return True
    else:
        return False


if confirm_continue('Hello to Rock, Paper, Scissors Game (press enter to continue)'):
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    print(f"Welcome {player_one_name} and {player_two_name}. Let's play rock, paper, scissors!")

    while True:
        print("For rock, type 1. For paper, type 2. For scissors, type 3.")
        player_one_choice = correct_input_checker(player_one_name)
        player_two_choice = correct_input_checker(player_two_name)

        if winner_checker(player_one_choice, player_two_choice):
            scores[0] += 1
        elif not winner_checker(player_one_choice, player_two_choice):
            scores[1] += 1
        elif winner_checker(player_one_choice, player_two_choice) is None:
            print("It's a tie!")

        print(f"it\'s {scores[0]} : {scores[1]}")
        if not confirm_continue("Wanna play again? Press enter to continue, type exit to exit."):
            print(f"{player_one_name} won {scores[0]} times, {player_two_name} won {scores[1]} times.")
            break


else:
    print("Cancelled.")
