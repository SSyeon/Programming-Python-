from tictactoe import TicTacToe
import tkinter


class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        # show_board()
        print(self.ttt)
        # 반복하자
        while True:
            # 위치를 입력받자
            row = int(input("row : "))
            col = int(input("col : "))
            # 말을 놓자
            self.ttt.set(row, col)
            print(self.ttt)
            # check_winner()
            if self.ttt.check_winner() == "O":
                print("O,승리, ㅊㅋㅊㅋ")
                break
            elif self.ttt.check_winner() == "X":
                print("ㅉㅉ 짐")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

        # result()


class GameManager_GUI:
    def __init__(self):
        self.ttt = TicTacToe()
        CANVAS_SIZE = 300
        self.TILE_SIZE = CANVAS_SIZE / 3

        self.root = tkinter.Tk()
        # self.root.title("택 택 토")
        self.root.geometry(str(CANVAS_SIZE) + "X" + str(CANVAS_SIZE))
        # geometry("300X300")
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg="white", width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()

        self.images = dict()
        self.imges["O"] = tkinter.PhotoImage(file="img/O.gif")
        self.imges["X"] = tkinter.PhotoImage(file="img/X.gif")
        self.canvas.bind("<Button-1>", self.click_handler)

    def click_handler(self, event):

        pass

    def draw_board(self):
        # clear
        self.canvas.delete("all")

        SIZE = 100
        x = 0
        y = 0
        for i, v in enumerate(self.ttt.board):
            if v == ".":
                pass
            elif v == "O":
                self.canvas.create_image(x, y, anchor="nw", images=self.images["O"])
            elif v == "X":
                self.canvas.create_image(x, y, anchor="nw", images=self.images["X"])
            x += self.TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += self.TILE_SIZE

    def play(self):
        self.root.mainloop()


if __name__ == '__main__':
    gm = GameManager_GUI()
    gm.play()
    gm.ttt.set(1, 1)
    gm.draw_board()
