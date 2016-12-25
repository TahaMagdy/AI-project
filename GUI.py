from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("450x450")

#Main label
Slabel = ttk.Label(root,text='Subtract A Square Game')
Slabel.place(x=165, y=0, width=200, height=50)

#User Label
Ulabel = ttk.Label(root,text='User')
Ulabel.place(x=200, y=50, width=200, height=50)

#User Entry
Uentry = ttk.Entry(root)
Uentry.place(x=90, y=100, width=300, height=80)

#Computer Label
Clabel = ttk.Label(root,text='Computer')
Clabel.place(x=200, y=200, width=200, height=50)

#Computer Entry
Centry = ttk.Entry(root)
Centry.place(x=90, y=250, width=300, height=80)

#Reset Button
Rbutton=ttk.Button(root,text='Reset')
Rbutton.place(x=140,y=360, width=200,height=50)

root.mainloop()