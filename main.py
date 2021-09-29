import tkinter as tk


HEIGHT = 500
WIDTH = 600

def search_function(entry):
    print(str(entry + " Price is: Price Per Share"))

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

large = tk.Frame(root, bg='black')
large.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(large, bg='gray', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frame, text="Search for a Stock:", bg='gray', fg='white', font=100)
label.place(relx=0, rely=0, relwidth=1, relheight=0.5)

entry = tk.Entry(frame, bg='#80c1ff', font=40)
entry.place(relx=0, rely=0.5, relwidth=0.65, relheight=0.5)

search = tk.Button(frame, text="Search", fg='blue', font=40, command=lambda: search_function(entry.get()))
search.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.5)

lower_frame = tk.Frame(large, bg='gray', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

one = tk.Button(lower_frame, text="1", fg='green', font=40)
one.place(relwidth=0.5, relheight=0.2)

five = tk.Button(lower_frame, text="5", fg='green', font=40)
five.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

ten = tk.Button(lower_frame, text="10", fg='green', font=40)
ten.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.2)

twentyfive = tk.Button(lower_frame, text="25", fg='green', font=40)
twentyfive.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.2)

fifty = tk.Button(lower_frame, text="50", fg='green', font=40)
fifty.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.2)

onehundred = tk.Button(lower_frame, text="100", fg='green', font=40)
onehundred.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.2)

fivehundred = tk.Button(lower_frame, text="500", fg='green', font=40)
fivehundred.place(relx=0, rely=0.6, relwidth=0.5, relheight=0.2)

onethousand = tk.Button(lower_frame, text="1,000", fg='green', font=40)
onethousand.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.2)

search_again = tk.Button(lower_frame, text="Search Another Stock", fg='green', font=40)
search_again.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

root.mainloop()
