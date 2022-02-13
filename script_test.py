# Tic-Tac-Toe

print("\nWelcome to a text-based version of Tic-Tac-Toe!\n")

player1 = input("Please enter the name of Player One: ")
player2 = input("\nPlease enter the name of Player Two: ")

print("""You are going to take turns to enter Xs and Os into the following grid.

The player who succeeds in placing three of their marks in a horizontal, vertical, 
or diagonal row is the winner.

        |_|_|_|    Use numbers to indicate which square
        |_|_|_|    you would like to place your mark.
        |_|_|_|    Ex: (1) corresponds to the first square.
""")


class Game:
    position_list = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def position_check(self, index):
        return self.position_list[index - 1] == "_"

    def player_check(self, user_input):
        return user_input % 2 != 0

    def update_board(self, user_input):
        if turn_tracker % 2 != 0:
            self.position_list[user_input - 1] = "X"
        if turn_tracker % 2 == 0:
            self.position_list[user_input - 1] = "O"

        grid = "\nCurrent game board:\n\n|" + self.position_list[0] + "|" + self.position_list[1] + "|" + self.position_list[2] + "|\n|" + self.position_list[
            3] + "|" + self.position_list[4] + "|" + self.position_list[5] + "|\n|" + self.position_list[6] + "|" + self.position_list[7] + "|" + self.position_list[
                   8] + "|\n"
        print(grid)

    def check_for_a_winner(self):

       winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

       for combination in winning_combinations:
           if self.position_list[combination[0]] == "X":
               if self.position_list[combination[1]] == "X":
                   if self.position_list[combination[2]] == "X":
                       print(player1 + " wins!")
                       return True
           if self.position_list[combination[0]] == "O":
               if self.position_list[combination[1]] == "O":
                   if self.position_list[combination[2]] == "O":
                       print(player2 + " wins!")
                       return True
       else:
           return False


game1 = Game()


turn_tracker = 1
while turn_tracker < 10:

    if game1.player_check(turn_tracker):
        input_string = player1 +": Please enter the square to place your mark: "
        choice = int(input(input_string))

        while not game1.position_check(choice):
            print("It looks like that square is already taken.")
            choice = int(input(input_string))

    if not game1.player_check(turn_tracker):
        input_string = player2 + ": Please enter the square to place your mark: "
        choice = int(input(input_string))

        while not game1.position_check(choice):
            print("It looks like that square is already taken.")
            choice = int(input(input_string))

    game1.update_board(choice)
    if game1.check_for_a_winner():
        break

    turn_tracker = turn_tracker + 1

print("Game over!")

