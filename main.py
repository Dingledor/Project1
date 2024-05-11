from tkinter import *
from logic import *


def main():
    root = Tk()
    root.configure(background='black')
    root.title("TV Remote")
    root.geometry("174x665+0+0")
    root.resizable(False, False)
    Logic(root)
    root.mainloop()


if __name__ == "__main__":
    main()
