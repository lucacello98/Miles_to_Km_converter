import tkinter
from tkinter import Entry
from tkinter import Button

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.configure(background="white")
window.minsize(width=500, height=100)


# Convert miles to kilometers
def convert():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text = f"{km:.2f} Km")

# Configure the grid layout without expansion to spread it out
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=0)
window.grid_rowconfigure(2, weight=0)
window.grid_rowconfigure(3, weight=0)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Entry field
entry = Entry(width=10, bg="white", fg="black", insertbackground="black")
entry.grid(row=0, column=1, padx=5, pady=5)


# Label for miles
miles_label = tkinter.Label(text="Miles", bg="white",fg="black")
miles_label.grid(row=0, column=2, padx=5, pady=5)

is_equal_label = tkinter.Label(text="is equal to", bg="white",fg="black")
is_equal_label.grid(row=1, column=0, padx=5, pady=5)

Km_label = tkinter.Label(text="Km", bg="white",fg="black")
Km_label.grid(row=1, column=2, padx=5, pady=5)

calculate = Button(text="Calculate", command=convert,bg="White")
calculate.configure(bg="white")
calculate.grid(row=2,column=1,padx=5,pady=5)

# Result label (initially showing nothing or 0 km)
result_label = tkinter.Label(text="0 Km", bg="white", fg="black")
result_label.grid(row=1, column=1, padx=5, pady=10, sticky="ew")


window.mainloop()


