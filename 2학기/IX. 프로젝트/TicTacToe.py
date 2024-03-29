class TicTacToe:
    def __init__(self):
        self.board = [".", ".", ".", \
                      ".", ".", ".", \
                      ".", ".", "."]
        self.current_turn = "X"

    def set(self, row, col): #빈칸일 경우에만말을 놓을 수 잇도록!
        # if self.current_turn == "O":
        #     self.current_turn = "X"
        # else:
        #     self.current_turn = "O"
        if self.get(row, col) == ".":
            self.current_turn = "X" if self.current_turn == "O" else "O"
            self.board[(row * 3) + col] = self.current_turn
        else:
            print("빈칸아닙니다;")

    def get(self, row, col):
        return self.board[(row * 3) + col]

    def check_winner(self):
        check = self.current_turn
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == check:
                # |
                return check
            elif self.get(0, i) == self.get(1, i) == self.get(2, i) == check:
                # -
                return check
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == check:
            # \
            return check
        elif self.get(0, 2) == self.get(1, 1) == self.get(2, 0) == check:
            # /
            return check

        if not "." in self.board:
            return "d"  # 비김

    def __str__(self):
        s = ""
        for i, v in enumerate(self.board):
            s += v
            if i % 3 == 2:
                s += "\n"
        return s