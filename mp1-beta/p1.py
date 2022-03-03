# -*- encoding=utf-8 -*-

import os

from tkinter import *
from tkinter import ttk

mw = Tk()

width = 1200
height = 700

mw.title('My PC')
mw.geometry('{}x{}+{}+{}'.format(width, height, 0, 0))

columns = ['Type', 'Size', 'Date' ]

tr = ttk.Treeview(
           master=mw,
           height=10,
           columns=columns,
           #show='tree',
           selectmode='browse',
           #xscrollcommand=xscroll.set,
           #yscrollcommand=yscroll.set,
                     )
                
tr.heading('#0'  , text='Name')
tr.heading('Type', text='Type')  
tr.heading('Size', text='Size')  
tr.heading('Date', text='Date')  

tr.column('#0'  , width=1200-80-80-160,anchor='w') 
tr.column('Type', width= 80)
tr.column('Size', width= 80)
tr.column('Date', width=160)

info = [ '', '', '', '',]

global img1
global img2
global img3

img1=PhotoImage(file='i1.png')
img2=PhotoImage(file='i2.png')
img3=PhotoImage(file='i3.png')

global sf1

sf1=tr.insert('', END, text="/", image=img2, open=True, values=info)

tr.pack(fill=BOTH,expand=True)

def trClick(event):
    item_text=['','','',]
    for item in tr.selection():
        item_text = tr.item(item,'text')
        print(item_text[0])
        
    if os.path.isdir(item_text[0]):
        print('dir')
        dirs = os.listdir(item_text[0])
        
        for files in dirs:
            print (files)
            info2= ['', '', '',]
            tr.insert(sf1, END, text=files, image=img2, open=True, values=info2)

tr.bind('<ButtonRelease-1>', trClick)

mw.mainloop()
   
