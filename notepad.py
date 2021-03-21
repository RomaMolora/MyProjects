# from tkinter import *
# from tkinter import scrolledtext
# from tkinter import Menu
#
# w = Tk()
# txt = scrolledtext.ScrolledText(w, width=40, height=10)
# txt.insert(INSERT, 'Entry')
# # txt.pack()
# b = Button(w, command=lambda: clear())
# # b.pack()
#
# def clear():
#     txt.delete(1.0, END)
#
#
# menu = Menu(w)
# new_item = Menu(menu)
# new_item2 = Menu(menu)
# new_item.add_command(label='view file', command=lambda: [txt.pack(), b.pack()])
# new_item.add_command(label='remove', command=lambda: [txt.pack_forget(),
#                                                       b.pack_forget()])
# new_item.add_command(label='clear', command=lambda: clear())
# new_item.add_command(label='new file', command=lambda: [clear(), txt.insert(INSERT, 'Entry')])
# menu.add_cascade(label='New File', menu=new_item)
#
# new_item2.add_command(label='edit', command=lambda: [clear(), txt.insert(INSERT, 'New File')])
# menu.add_cascade(label='Edit', menu=new_item2)
#
# # menu.add_command(label='edit', command=lambda: [txt.pack_forget(), b.pack_forget()])
#
#
#
# # new_item.add_command(label='new file', command=lambda: [txt.pack(), b.pack()])
# # menu.add_cascade(label='new file')
#
# w.config(menu=menu)
#
#
#
#
# w.mainloop()


# from tkinter import *
#
# root = Tk()
# root.wm_attributes("-alpha", 0.8)
# # root.overrideredirect(True)  # делает окно неподвижным
# # root.wm_attributes("-topmost", 0.8)
#
# # root.config(bg='systemTransparent')
#
# # root.geometry("+250+250")
# # button = Button(root, text='example')
# # button.pack()
#
# root.mainloop()


# from tkinter import *
#
# TF = True
#
# def about():
#     a = Toplevel()
#     a.geometry('200x150')
#     a['bg'] = 'grey'
#     a.overrideredirect(TF)
#     Label(a, text="About this") \
#         .pack(expand=1)
#     a.after(5000, lambda: a.destroy())
#
#
# root = Tk()
# root.title("Главное окно")
# # TF = False
# Button(text="Button", width=20).pack()
# Label(text="Label", width=20, height=3) \
#     .pack()
# Button(text="About", width=20, command=about) \
#     .pack()
#
# root.mainloop()


#custom title bar for tkinter

# from tkinter import *
#
# root=Tk()
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('400x100+200+200') # set new geometry
#
# # make a frame for the title bar
# title_bar = Frame(root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
#
# # put a close button on the title bar
# close_button = Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
#
# # a canvas for the main area of the window
# window = Canvas(root, bg='#2e2e2e',highlightthickness=0)
#
# # pack the widgets
# title_bar.pack(expand=1, fill=X)
# close_button.pack(side=RIGHT)
# window.pack(expand=1, fill=BOTH)
# xwin=None
# ywin=None
# # bind title bar motion to the move window function
#
# def move_window(event):
#     root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
# def change_on_hovering(event):
#     global close_button
#     close_button['bg']='red'
# def return_to_normalstate(event):
#     global close_button
#     close_button['bg']='#2e2e2e'
#
#
# title_bar.bind('<B1-Motion>', move_window)
# close_button.bind('<Enter>',change_on_hovering)
# close_button.bind('<Leave>',return_to_normalstate)
# root.mainloop()

# from tkinter import *
# # import tklMessageBox as messagebox
# r = Tk()
# a = 1
# r.overrideredirect(0)
# r.resizable(a, a)
#
# def press():
#     r.resizable(0, 0)
#     r.overrideredirect(1)
#
# b = Button(r, text='sdfsdfsdfsdf', command=press).pack()
#
# r.mainloop()


# from tkinter import *
# import time
# root = Tk()
# a = True
# root.overrideredirect(a)
# root.geometry('200x200+100+100')
# root.resizable(False, False)
# root.update_idletasks()
# time.sleep(1)
# print(1)
# a = False
# root.mainloop()