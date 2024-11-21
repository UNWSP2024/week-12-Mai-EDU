# Programmer: Mai Lillie
# Date: 11/21/24
# Program #1 Joe's Automotive

import tkinter
import tkinter.messagebox

# Creates a window and two buttons
class CarGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive Services")

        # Creates the frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Check box IntVar functions
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Sets all the IntVar to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        #Creates check button widgets
        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Oil Change", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Lube Job", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Radiator Flush", variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text="Transmission Fluid", variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text="Inspection", variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text="Muffler Replacement", variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text="Tire Rotation", variable=self.cb_var7)


        #Packs the check buttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Adds the buttons to the bottom frame
        # Show price button
        self.calculate = tkinter.Button(self.bottom_frame, text="Show Price", command=self.calculate)
        self.calculate.pack(side = 'left')
        # Quit Button
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side = 'left')

        # Runs the Program
        tkinter.mainloop()

    # Adds a function to the info button
    def calculate(self):
        price = 0
        if self.cb_var1.get() == 1:
            price += 30
        if self.cb_var2.get() == 1:
            price += 20
        if self.cb_var3.get() == 1:
            price += 40
        if self.cb_var4.get() == 1:
            price += 100
        if self.cb_var5.get() == 1:
            price += 35
        if self.cb_var6.get() == 1:
            price += 200
        if self.cb_var7.get() == 1:
            price += 20
        tkinter.messagebox.showinfo("Total Cost", str(price) + " dollars.")

# Runs the program
if __name__ == '__main__':
    car_gui = CarGUI()
