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
    global cx, cy, mx, my
    delta = {#キー：押されているキーkey/値：移動幅リスト[x, y]
        ""     :[0,  0],
        "Up"   :[0, -1],
        "Down" :[0, +1],
        "Left" :[-1, 0],
        "Right":[+1, 0],
    }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my, mx = my+delta[key][1], mx+delta[key][0]
    except:
        pass
    cx, cy = mx*50+25, my*50+25
    canvas.coords("syobon", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるしょぼん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(30, 18)
    mm.show_maze(canvas, maze_bg)

    syobon = tk.PhotoImage(file="fig/syobon.png")
    mx, my = 1, 1
    cx, cy = mx*50+25, my*50+25
    canvas.create_image(cx, cy, image=syobon, tag="syobon")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()