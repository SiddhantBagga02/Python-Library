# Import the Tkinter module
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Form")

# Create labels for each field
name_label = tk.Label(window, text="Name:")
address_label = tk.Label(window, text="Address:")
gender_label = tk.Label(window, text="Gender:")
email_label = tk.Label(window, text="Email:")

# Create entry widgets for each field
name_entry = tk.Entry(window)
address_entry = tk.Entry(window)
email_entry = tk.Entry(window)

# Create radio buttons for gender selection
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
other_radio = tk.Radiobutton(window, text="Other", variable=gender_var, value="Other")

# Create a submit button
submit_button = tk.Button(window, text="Submit")

# Arrange the widgets using grid layout
name_label.grid(row=0, column=0, sticky="e")
name_entry.grid(row=0, column=1, padx=10, pady=10)
address_label.grid(row=1, column=0, sticky="e")
address_entry.grid(row=1, column=1, padx=10, pady=10)
gender_label.grid(row=2, column=0, sticky="e")
male_radio.grid(row=2, column=1, sticky="w")
female_radio.grid(row=3, column=1, sticky="w")
other_radio.grid(row=4, column=1, sticky="w")
email_label.grid(row=5, column=0, sticky="e")
email_entry.grid(row=5, column=1, padx=10, pady=10)
submit_button.grid(row=6, column=1, sticky="e")

# Start the main loop
window.mainloop()
