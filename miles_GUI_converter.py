from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=130)
window.config(padx=10, pady=10)


#Entries
miles_input = Entry(width=5)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

#Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

label1 = Label(text="is equal to ")
label1.grid(column=0, row=1)

km = 0
label2 = Label(text=f"{km}")
label2.grid(column=1, row=1)

label3 = Label(text="km")
label3.grid(column=2, row=1)



#Buttons
def action():
     miles = float(miles_input.get())
     km = round(miles * 1.609)
     label2.config(text=f"{km}")


#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()

