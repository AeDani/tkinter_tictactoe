import tkinter as tk
from tkinter import ttk
from game import GameLogic


class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tic tac toe")

        # load game logic
        self.game = GameLogic()

        # top level container
        container = ttk.Frame(self)
        container.grid()

        # Menu
        self.__create_menu()

        # Frame with Label of current player
        lbl_frame = tk.Frame(container)
        lbl_frame.grid(row=0, column=0)
        self.current_player = tk.StringVar(value="Player 1")
        label = tk.Label(lbl_frame, textvariable=self.current_player)
        label.grid()

        # Frame with 9 buttons
        self._cells = {}
        self.btn_frame = tk.Frame(container)
        self.btn_frame.grid(row=1, column=0)
        self.__create_board(self.btn_frame)

    def reset_game(self):
        self.game = GameLogic()
        self.__create_board(self.btn_frame)

    def __create_board(self, parent):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    parent, command=lambda id=(i, j): self.game.play_game(id, self), height=6, width=8)
                btn.grid(row=i, column=j)
                self._cells[(i, j)] = btn

    def __create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar)

        file_menu.add_command(
            label='Exit',
            command=self.destroy
        )

        file_menu.add_command(
            label='Reset Game',
            command=self.reset_game
        )

        menubar.add_cascade(
            label="Game",
            menu=file_menu
        )


app = TicTacToe()
app.mainloop()
