#list box using tkinter
import tkinter as tk

def on_select(event):
    # Get the selected item from the list box
    selected_item = listbox.get(listbox.curselection())
    status_label.config(text=f"Selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("List Box Example")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Add items to the Listbox
for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

# Bind the on_select function to the listbox selection event
listbox.bind('<<ListboxSelect>>', on_select)

# Create a Label to display the selected item
status_label = tk.Label(root, text="Selected: None")
status_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
