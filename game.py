

class GameLogic():
    def __init__(self):
        self.players = ["Player 1", "Player 2"]
        self.players_symbol = ["x", "o"]
        self.currentPlayer = 0
        self.is_game_over = False

        self.board = [[0 for j in range(3)] for i in range(3)]

    def play_game(self, id, controller):
        row, col = id

        # update board
        self.board[row][col] = self.players_symbol[self.currentPlayer]

        # update button
        btn_clicked = controller._cells[id]
        btn_clicked["text"] = self.players_symbol[self.currentPlayer]
        # disable button
        btn_clicked["state"] = "disabled"

        # check winner
        self.check_winner()
        if self.is_game_over:
            # update label with winner
            controller.current_player.set(
                f"{self.players[self.currentPlayer]} wins!!!")
            # disable all buttons
            for btn in controller._cells.values():
                btn["state"] = "disabled"
            return

        # switch player
        self.currentPlayer = 1 - self.currentPlayer
        # update label with current player
        controller.current_player.set(self.players[self.currentPlayer])

    def check_winner(self):
        symbol_to_check = self.players_symbol[self.currentPlayer]

        # check rows
        if any([self.all_equal(row, symbol_to_check) for row in self.board]):
            self.is_game_over = True

        # check columns
        cols = []
        for i in range(3):
            cols.append([row[i] for row in self.board])
        if any([self.all_equal(col, symbol_to_check) for col in cols]):
            self.is_game_over = True

        # check diagonals
        diagonals = []
        diagonals.append([r[i] for i, r in enumerate(self.board)])
        diagonals.append([r[~i] for i, r in enumerate(self.board)])
        if any([self.all_equal(diagonal, symbol_to_check) for diagonal in diagonals]):
            self.is_game_over = True

    @staticmethod
    def all_equal(lst, element):
        return all([el == element for el in lst])
