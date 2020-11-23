from tkinter import *
import calendar
root = Tk()
root.title("My  Own  Gui Calendar")
year = 2021
mycal = calendar.calendar(year)
cal_year = Label(root, text =mycal, font="Consolas 10 bold")
cal_year.pack()
root.mainloop()