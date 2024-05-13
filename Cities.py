#write a python program to add list box which is having choices of city to be visited .from those choices only two choice should be submited, rest should be eliminiated
import tkinter as tk

def submit_choices():
    selected_cities = listbox.curselection()

    # Check if exactly two cities are selected
    if len(selected_cities) != 2:
        status_label.config(text="Please select exactly two cities.")
        return

    # Get the selected cities and update the status label
    city1 = listbox.get(selected_cities[0])
    city2 = listbox.get(selected_cities[1])
    status_label.config(text=f"Selected Cities: {city1} and {city2}")

    # Disable the listbox to prevent further selections
    listbox.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("City Selection Example")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5)
listbox.pack(pady=10)

# Add cities to the Listbox
cities = ["New York", "Los Angeles", "London", "Paris", "Tokyo", "Sydney"]
for city in cities:
    listbox.insert(tk.END, city)

# Create a Submit button
submit_button = tk.Button(root, text="Submit Choices", command=submit_choices)
submit_button.pack(pady=10)

# Create a Label to display the selected cities
status_label = tk.Label(root, text="Selected Cities: None")
status_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
