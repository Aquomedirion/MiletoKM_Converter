from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)



# Label2

label2 = Label(text="is equal to", font=("Arial", 20, "bold"))
label2.grid(column=0, row=1)

# Label3
label3 = Label(text="Km", font=("Arial", 20, "bold"))
label3.grid(column=3, row=1)

# Label4
label4 = Label(text="Miles", font=("Arial", 20, "bold"))
label4.grid(column=3, row=0)

# Value Label
label1 = Label(text="", font=("Arial", 20, "bold"))
label1.config(padx=20, pady=20)
label1.grid(column=2, row=1)

# Calculate Function
def calculate():
    value = input.get()
    converted_value = round(int(value) * 1.60934, 2)
    label1.config(text=converted_value)

    return converted_value



# Entry

input = Entry()
input.grid(column=2, row=0)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=2)

window.mainloop()
