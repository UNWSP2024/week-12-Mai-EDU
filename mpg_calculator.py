# Programmer: Mai Lillie
# Date: 11/21/24
# Program #1 Miles per Gallon Calculator

import tkinter
import tkinter.messagebox

# Creates a window and two buttons
class MilesGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        # Creates the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Entry widget labels
        self.gallon_label = tkinter.Label(self.top_frame, text="Number of gallons your car holds:")
        self.mile_label = tkinter.Label(self.middle_frame, text="How far your car can go on full tank:")

        #Entry widgets
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)
        self.mile_entry = tkinter.Entry(self.middle_frame, width=10)

        #Packs labels and widgets
        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')
        self.mile_label.pack(side='left')
        self.mile_entry.pack(side='left')

        # Adds the buttons to the bottom frame
        # Show info button
        self.calculate = tkinter.Button(self.bottom_frame, text="Calculate MPG", command=self.calculate)
        self.calculate.pack(side = 'left')
        # Quit Button
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side = 'left')

        # Runs the Program
        tkinter.mainloop()

    # Adds a function to the info button
    def calculate(self):
        mile = float(self.mile_entry.get())
        gallon = float(self.gallon_entry.get())
        mpg = mile/gallon
        tkinter.messagebox.showinfo("Miles per Gallon", str(mpg) + " mpg.")

# Runs the program
if __name__ == '__main__':
    miles_gui = MilesGUI()
