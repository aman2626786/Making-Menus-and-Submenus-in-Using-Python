from tkinter import *

def command_info():
    print("This is exicuted")
root = Tk()
root.geometry('600x500')
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='Edit', command=command_info)
m1.add_separator()
m1.add_command(label='Cut', command=command_info)
m1.add_command(label='Copy', command=command_info)
m1.add_command(label='Paste', command=command_info)
m1.add_command(label='Undo', command=command_info)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help',menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='Save as', command=command_info)
m2.add_command(label='Save', command=command_info)
m2.add_separator()
m2.add_command(label='Open', command=command_info)
m2.add_command(label='Files', command=command_info)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Manage',menu=m2)

root.mainloop()