# Programmer: Mai Lillie
# Date: 11/21/24
# Program #3 Long-Distance Calls

import tkinter
import tkinter.messagebox
import math

# Creates a window and two buttons
class PhoneGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long-Distance Call Price")

        # Creates the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Creates the variable behind the radio buttons
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Creates radiobuttons
        self.rb1 = tkinter.Radiobutton(self.top_frame, text="Daytime (6:00 AM through 5:59 PM)", variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text="Evening (6:00 PM through 11:59 PM)", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text="Off-Peak (Midnight through 5:59 AM)", variable=self.radio_var, value=3)

        # Packs the check buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Creates the entry widget and label
        self.minutes_label = tkinter.Label(self.top_frame, text="Length of Phone Call (Minutes):")
        self.minutes_entry = tkinter.Entry(self.top_frame, width=10)
        self.minutes_label.pack(side='left')
        self.minutes_entry.pack(side='left')

        # Adds the buttons to the bottom frame
        # Show price button
        self.calculate = tkinter.Button(self.bottom_frame, text="Show Price", command=self.calculate)
        self.calculate.pack(side='left')
        # Quit Button
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # Runs the Program
        tkinter.mainloop()

    # Adds a function to the info button
    def calculate(self):
        price = 0
        minutes = float(self.minutes_entry.get())
        if self.radio_var.get() == 1:
            price = minutes * 0.02
        if self.radio_var.get() == 2:
            price = minutes * 0.12
        if self.radio_var.get() == 3:
            price = minutes * 0.05
        price = round(price, 3)
        tkinter.messagebox.showinfo("Total Cost", str(price) + " dollars.")

    # Runs the program
if __name__ == '__main__':
    phone_gui = PhoneGUI()
