from tkinter import *


class GUI(Tk):
    def __init__(self, title="Window", width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


def convert():
    from_val = from_.get()
    to_val = to_.get()
    str_lb = ""
    try:
        num = float(enterE.get())
        if from_val == "Meters" and to_val == "Inches":
            num *= 39.37
        elif from_val == "Meters" and to_val == "Foot":
            num *= 3.28
        elif from_val == "Inches" and to_val == "Meters":
            num /= 39.37
        elif from_val == "Inches" and to_val == "Foot":
            num /= 12
        elif from_val == "Foot" and to_val == "Meters":
            num /= 3.28
        elif from_val == "Foot" and to_val == "Inches":
            num *= 12
        str_lb = "Ans. " + str(round(num, 2))
    except:
        str_lb = "Invalid value entered"

    ans_lb = Label(root, text=str_lb, bg=bg, width=18)
    ans_lb.grid(row=2, column=1)


if __name__ == '__main__':
    bg = "white"
    scales = ["Meters", "Inches", "Foot"]

    # Making Window
    root = GUI("Length Converter", width=330, height=110)

    from_ = StringVar()
    from_.set("Meters")
    from_menu = OptionMenu(root, from_, *scales)
    from_menu.grid(row=0, column=0, pady=5, padx=5)

    lb = Label(root, text="Convert to", bg=bg)
    lb.grid(row=0, column=1, pady=5, padx=5)

    to_ = StringVar()
    to_.set("Inches")
    to_menu = OptionMenu(root, to_, *scales)
    to_menu.grid(row=0, column=2, pady=5, padx=5)

    enterL = Label(root, text="Enter Length", bg=bg)
    enterL.grid(row=1, column=0, pady=5, padx=5)

    enterE = Entry(root)
    enterE.grid(row=1, column=1, pady=5, padx=5)

    btn = Button(root, text="Convert", command=convert)
    btn.grid(row=2, column=0, pady=5, padx=5)

    # Starting Window
    root.start()
