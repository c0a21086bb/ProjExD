import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x500")
    root.title("電卓")

    btn = tk.button(root,
                    text = 9,
                    )

    root.mainloop