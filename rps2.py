import random
class Game:
    def __init__(self):
        self.games_played = 0
        self.computer_wins = 0
        self.player_wins = 0
        self.ties = 0

    def add_games_played(self):
        self.games_played += 1

    def get_games_played(self):
        return self.games_played

    def add_computer_win(self):
        self.computer_wins += 1
    
    def get_computer_wins(self):
        return self.computer_wins
    
    def add_player_wins(self):
        self.player_wins += 1

    def get_player_wins(self):
        return self.player_wins
    
    def get_ties(self):
        return self.ties
    
    def add_ties(self):
        self.ties += 1

    @staticmethod
    def print_welcome():
        print("Welcome to Rock Paper Scissors!")

    @staticmethod
    def get_choice():
        print("Please choose Rock (r), Paper (p), or Scissors (s). Enter to quit.")
        choice = input("Choice: ")
        choices = ['r', 'p', 's', '']
        if choice in choices:
            return choice
        else:
            print("Sorry, that's not a valid choice.")

    @staticmethod
    def get_computer_choice():
        choices = ['r', 'p', 's']
        computer_choice = random.choice(choices)
        return computer_choice

    def check(self, user_choice, computer_choice):

        user_choice = user_choice
        computer_choice = computer_choice
        if user_choice == computer_choice:
            return 'tie'
            self.add_ties()
        elif user_choice == 'r' and computer_choice == 'p':
            return 'computer'
            self.add_computer_win()
        elif user_choice == 'r' and computer_choice == 's':
            return 'player'
            self.add_player_wins()
        elif user_choice == 'p' and computer_choice == 'r':
            return 'player'
            self.add_player_wins()
        elif user_choice == 'p' and computer_choice == 's':
            return 'computer'
            self.add_computer_win()
        elif user_choice == 's' and computer_choice == 'r':
            return 'computer'
            self.add_computer_win()
        elif user_choice == 's' and computer_choice == 'p':
            return 'player'
            self.add_player_wins()
        self.add_games_played()

running = True

# Instantiate game object
game = Game()

# Game starts
game.print_welcome()


# Game Loop Starts
while running:
    choice = game.get_choice()
    if choice == '':
        running = False
    c_choice = game.get_computer_choice()

    winner = game.check(choice, c_choice)
    print('Computer chose: ' + c_choice)
    if winner == 'computer':
        print('Computer wins!')
        game.add_computer_win()
    elif winner == 'player':
        print("You win!")
        game.add_player_wins()
    elif winner == 'tie':
        print("It's a tie!")
        game.add_ties()
    game.add_games_played()
    print('Games played: ' + str(game.get_games_played()))
    print('Wins: ' + str(game.get_player_wins()))
    print('Losses: ' + str(game.get_computer_wins()))
    print('Ties: ' + str(game.get_ties()))