import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    delta = {#キー：押されているキーkey/値：移動幅リスト[x, y]
        ""     :[0, 0],
        "Up"   :[0, -20],
        "Down" :[0, +20],
        "Left" :[-20, 0],
        "Right":[+20, 0]}
    cx, cy = cx+delta[key][0], cy+delta[key][1]
    canvas.coords("kusodori", cx, cy)
    root.after(50, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える糞鳥")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    kusodori = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=kusodori, tag="kusodori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()