''' 
Room-challenge
Author: Daniel Karandikar
App to calculate room volume, floor area, and paint required for walls
'''

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    '''The main room-resizing app'''
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Room Evaluation")
        self.geometry("300x400")

        self.dimensions = (0, 0, 0) #height, width, depth
        self.widgets = dict()
        self.vars = []

        self.myframe = tk.Frame(self)
        self.myframe.columnconfigure(0, weight=1)
        self.myframe.columnconfigure(1, weight=1)
        self.setup_widgets()


    def calculate(self):
        try:
            self.vars[0].set("")
            height = float(self.widgets["HeightE"].get())
            width = float(self.widgets["WidthE"].get())
            depth = float(self.widgets["DepthE"].get())

            volume = height*width*depth
            area = width*depth
            wall_area = 2*(height*width) + 2*(height*depth)
            vol_req = 2*wall_area/12   #Assumes 2 coats of paint at 12sqm per litre

            self.vars[1].set("Area of the floor: " + "%.2f" % area +  " metres-squared")
            self.vars[2].set("Volume of the room: " + "%.2f" % volume +  " metres-cubed")
            self.vars[3].set("Paint required for walls: " + "%.2f" % vol_req +  " litres")

        except ValueError:
            self.vars[0].set("Please insert only positive real numbers as dimensions")
            self.vars[1].set("Area of the floor: 0.00 metres-squared")
            self.vars[2].set("Volume of the room: 0.00 metres-cubed")
            self.vars[3].set("Paint required for walls: 0.00 litres")


    def setup_widgets(self):
        '''Setups the buttons, entry forms and labels'''

        entries = ["Height", "Width", "Depth"]

        self.widgets["title"] = ttk.Label(self.myframe, text="Please insert dimensions in meters")
        self.widgets["title"].grid(row=0, columnspan=2, pady=10)

        row_index = 1
        for key in entries:
            self.widgets[key+"L"] = ttk.Label(self.myframe, text=entries[row_index-1]+": ")
            self.widgets[key+"L"].grid(row=row_index, column=0, sticky="E", pady=5)
            self.widgets[key+"E"] = tk.Entry(self.myframe, justify="center")
            self.widgets[key+"E"].insert(0, "0")
            self.widgets[key+"E"].grid(row=row_index, column=1, sticky="W")
            row_index += 1

        self.widgets["calc_button"] = ttk.Button(self.myframe, text="Calculate",
                                                 command=self.calculate)
        self.widgets["calc_button"].grid(row=4, columnspan=2, pady=10)

        self.vars.append(tk.StringVar())
        self.vars[0].set("")
        self.widgets["error"] = ttk.Label(self.myframe, textvariable=self.vars[0])
        self.widgets["error"].grid(row=5, columnspan=2, pady=15)

        for _ in range(3):
            self.vars.append(tk.StringVar())

        self.vars[1].set("Area of the floor: 0.00 metres-squared")
        self.vars[2].set("Volume of the room: 0.00 metres-cubed")
        self.vars[3].set("Paint required for walls: 0.00 litres")

        self.widgets["area"] = ttk.Label(self.myframe, textvariable=self.vars[1])
        self.widgets["area"].grid(row=6, columnspan=2, pady=5)
        self.widgets["volume"] = ttk.Label(self.myframe, textvariable=self.vars[2])
        self.widgets["volume"].grid(row=7, columnspan=2, pady=5)
        self.widgets["paint"] = ttk.Label(self.myframe, textvariable=self.vars[3])
        self.widgets["paint"].grid(row=8, columnspan=2, pady=5)


        self.myframe.pack(fill=tk.BOTH, expand=tk.YES)



if __name__ == "__main__":
    APP = App()
    APP.mainloop()
