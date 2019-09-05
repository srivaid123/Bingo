import random

number_pool = [i for i in range(1, 91)]
random.shuffle(number_pool)
computer_card = sorted(random.sample(number_pool, 15))
player_card = sorted(random.sample(number_pool, 15))


def display_cards():
    print("=================================================================")
    print("= Computer card:                                                =\n")
    print(computer_card)
    print("=================================================================")
    print("= Player card:                                                  =\n")
    print(player_card)
    print("=================================================================")


def winner_found():
    if (len(computer_card) == 0 or len(player_card) == 0):
        return True
    return False


def who_won():
    if(len(player_card) == 0):
        return "Player"
    if(len(computer_card) == 0):
        return "Computer"


def wait():
    input()


def main():
    while (not winner_found()):
        print("\n########### NEW ROW ###########")
        random_choice = number_pool.pop()
        print("The random lotto is: {} ".format(random_choice))
        display_cards()
        if random_choice in player_card:
            player_card.remove(random_choice)
        if random_choice in computer_card:
            computer_card.remove(random_choice)

        wait()
    # If winner_found():
    print("There's a winner: The {}!" .format(who_won()))


if __name__ == '__main__':
    main()