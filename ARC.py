import tkinter as tk

def draw_arc(canvas):
    # Coordinates of the bounding box for the arc
    x0, y0, x1, y1 = 50, 50, 150, 150
    
    # Drawing the arc on the canvas
    canvas.create_arc(x0, y0, x1, y1, start=30, extent=120, style=tk.ARC, outline="blue", width=2)

# Create the main window
root = tk.Tk()
root.title("Arc Drawing Example")

# Create a Canvas widget
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Draw the arc on the canvas
draw_arc(canvas)

# Start the Tkinter event loop
root.mainloop()
