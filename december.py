# import tkinter as tk
# from tkinter import ttk

# def submit_data():
#     acc = terms_var.get()

#     if acc == "accepted":
#         firstname = first_name_entry.get()
#         lastname = last_name_entry.get()
#         gender = gender_combobox.get()
#         national = national_combobox.get()
#         state = state_combobox.get()
#         pincode = pincode_entry.get()
#         print("---------------------------------------")
#         print("First Name: ", firstname, "Last Name: ", lastname, "Gender: ", gender)
#         print("Nationality: ", national, "State: ", state, "Pincode: ", pincode)
#         print("---------------------------------------")
#     else:
#         print("Please accept the terms and conditions.")

# window = tk.Tk()
# window.title("user_info")

# frame = tk.Frame(window)
# frame.pack()

# user_info = tk.LabelFrame(frame, text="USER DETAILS")
# user_info.grid(row=0, column=0,sticky="news",padx=10,pady=10)

# first_name_label = tk.Label(user_info, text="First Name:")
# first_name_label.grid(row=0, column=0)

# last_name_label = tk.Label(user_info, text="Last Name:")
# last_name_label.grid(row=0, column=1)

# first_name_entry = tk.Entry(user_info)
# first_name_entry.grid(row=1, column=0)

# last_name_entry = tk.Entry(user_info)
# last_name_entry.grid(row=1, column=1)

# gender_label = tk.Label(user_info,text="Gender")
# gender_label.grid(row=0,column=2)
# gender_combobox = ttk.Combobox(user_info,values=["Male",'Female','Others']) 
# gender_combobox.grid(row=1,column=2)

# age_label = tk.Label(user_info,text="Age")
# age_label.grid(row=2,column=0)
# age_spinbox = tk.Spinbox(user_info,from_=18,to=60)
# age_spinbox.grid(row=3,column=0)

# national_label = tk.Label(user_info,text="Nationality")
# national_label.grid(row=2,column=1,sticky="news",padx=10,pady=10)
# national_combobox = ttk.Combobox(user_info,values=["indian","chinese","american","japanese"])
# national_combobox.grid(row=3,column=1)

# for widgets in user_info.winfo_children():
#     widgets.grid_configure(padx=10,pady=5)

# address_info = tk.LabelFrame(frame,text='Address')
# address_info.grid(row=1,column=0,sticky="news",padx=10,pady=10)
# state_name_label = tk.Label(address_info,text="state")
# state_name_label.grid(row=0,column=0)
# state_combobox = ttk.Combobox(address_info,values=["delhi","mumbai","u.p","m.p"])
# state_combobox.grid(row=1,column=0)
# pincode_label = tk.Label(address_info,text="pincode")
# pincode_label.grid(row=0,column=1)
# pincode_entry = tk.Entry(address_info)
# pincode_entry.grid(row=1,column=1)
# for widgets in address_info.winfo_children():
#     widgets.grid_configure(padx=10,pady=5)
# terms_label = tk.LabelFrame(frame, text="Terms")
# terms_label.grid(row=2, column=0,sticky="news",padx=10,pady=10)
# terms_var = tk.StringVar()
# terms_check = tk.Checkbutton(terms_label, text="I accept all terms and conditions", variable=terms_var,onvalue="accepted",offvalue="not accepted")
# terms_check.grid(row=0, column=0)

# submit_button = tk.Button(frame, text="Submit", command=submit_data)
# submit_button.grid(row=3, column=0, sticky="news")

# window.mainloop()




# import tkinter as tk
# from tkinter import ttk
# # root window
# window = tk.Tk()
# window.title("geeks for geeks")
# # window frame
# frame_1 = tk.Frame(window)
# frame_1.pack()
# # first frame
# user_info = tk.LabelFrame(frame_1,text="user details")
# user_info.grid(row=0,column=0)
# # inside user info frame
# name_lab = tk.Label(user_info,text="Name")
# name_lab.grid(row=0,column=0)
# name = tk.Entry(user_info)
# name.grid(row=0,column=1,padx=10,pady=10)

# gender_lab = tk.Label(user_info,text="Gender")
# gender_lab.grid(row=1,column=0)
# gender = ttk.Combobox(user_info,values=["male","female","others"])
# gender.grid(row=1,column=1,padx=10,pady=10)

# gender_1 = ttk.Radiobutton(user_info,text="male",value="male")
# gender_1.grid(row=2,column=0,padx=5,pady=5)
# gender_2 = ttk.Radiobutton(user_info,text="female",value="female")
# gender_2.grid(row=2,column=1,padx=5,pady=5)
# gender_3 = ttk.Radiobutton(user_info,text="other", value="other")
# gender_3.grid(row=2,column=2,padx=5,pady=5)

# age_bframe = tk.LabelFrame(frame_1,text="age")
# age_bframe.grid(row=1,column=0)
# age_label = tk.Label(age_bframe,text="age")
# age_label.grid(row=0,column=2)
# age_entry = tk.Spinbox(age_bframe,from_=18,to=60)
# age_entry.grid(row=0,column=3)


# window.mainloop()

# import tkinter as tk
# from tkinter import ttk
# # root window
# window = tk.Tk()
# window.title("geeks for geeks")
# window.mainloop()


