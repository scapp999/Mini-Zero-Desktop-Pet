import tkinter as tk

my_window = tk.Tk()

my_window.overrideredirect(True)

my_window.wm_attributes('-topmost', True)

my_window.config(bg='gray')
my_window.wm_attributes('-transparentcolor', 'gray')

zero1_raw = tk.PhotoImage(file="zero1.png")
zero2_raw = tk.PhotoImage(file="zero2.png")
zero1 = zero1_raw.subsample(3, 3)
zero2 = zero2_raw.subsample(3, 3)

my_label = tk.Label(my_window, image=zero1, bg='gray')
my_label.pack()

startX = 0
startY = 0

def clicked(event):
    global startX, startY
    startX = event.x
    startY = event.y
    my_window.focus_force()

def drag(event):
    new_x = my_window.winfo_x() + (event.x - startX)
    new_y = my_window.winfo_y() + (event.y - startY)
    my_window.geometry("+" + str(new_x) + "+" + str(new_y))


current_frame = 1

def animate():
    global current_frame
    
    if current_frame == 1:
        my_label.config(image=zero2)
        current_frame = 2
    else:
        my_label.config(image=zero1)
        current_frame = 1
        
    my_window.after(400, animate)

my_label.bind("<Button-1>", clicked)
my_label.bind("<B1-Motion>", drag)

my_label.bind("<Button-3>", lambda event: my_window.destroy())

my_window.bind("<Escape>", lambda event: my_window.destroy())

my_window.geometry("+600+400")

animate()

my_window.mainloop()
