from tkinter import *
from tkinter.ttk import *

# create a new window
root = Tk()

# create a treeview with two columns
tree = Treeview(root, columns=('Name', 'Age'))

# set the column headings
tree.heading('#0', text='ID')
tree.heading('#1', text='Name')
tree.heading('#2', text='Age')

# add some data to the treeview
tree.insert('', 'end', text='001', values=('Alice', '25'))
tree.insert('', 'end', text='002', values=('Bob', '35'))
tree.insert('', 'end', text='003', values=('Charlie', '45'))
tree.insert('', 'end', text='004', values=('Dave', '55'))

# pack the treeview and show the window
tree.pack()
root.mainloop()
