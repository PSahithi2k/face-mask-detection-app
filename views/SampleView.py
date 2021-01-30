from tkinter import *
from tkinter import ttk

class SampleView:

    def __init__(self):

        #create tk window
        window = Tk()

        #create tab based container
        tab_control = ttk.Notebook(window)

        page1_frame = ttk.Frame(tab_control)
        tab_control.add(page1_frame, text='page1')

        page2_frame = ttk.Frame(tab_control)
        tab_control.add(page2_frame, text='page2')

        page3_frame = ttk.Frame(tab_control)
        tab_control.add(page3_frame, text='page3')

        tab_control.pack()
        

        print("this is constrictor")
        self.page1(page1_frame)
        self.page2(page2_frame)
        self.page3(page3_frame)
        window.mainloop()

    def page1(self, page1_frame):
        l = Label(page1_frame, text='this is page 1')
        l.pack()
    
    def page2(self, page2_frame):
        l = Label(page2_frame, text='this is page 2')
        l.pack()

    def page3(self, page3_frame):
        l = Label(page3_frame, text='this is page 3')
        l.pack()

sv = SampleView()