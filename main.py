from tkinter import *


def miles_to_km_converter():
    miles = float(user_miles_input.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

user_miles_input = Entry(width=7)
user_miles_input.grid(column=1, row=0)
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to:")
is_equal_to_label.grid(column=0, row=1)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)
calculate_button = Button(text="Calculate", command=miles_to_km_converter)
calculate_button.grid(column=1, row=3)


window.mainloop()

