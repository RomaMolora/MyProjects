import os
import platform
import threading
import time
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Progressbar

root = Tk()
m = messagebox.askyesnocancel('', '"yes(Да)" - english(Английский), "no(Нет)" - Русский(Russia)')

if not m:
    a = 'Перезагрузите или выключите компьютер'
    q = 'Если «Да» - выключить компьютер, если «Нет» - перезагрузить компьютер.'
    c = 'Правила'
    d = 'Если поле пустое - оставьте его пустым.'
    f = 'Нажмите ОК и эта операция начнется'
    g = 'Прогресс -'
    h = 'Часы -'
    m = 'Минуты -'
    s = 'Секунды -'
    p = 'Нажать Кнопку'

elif m:
    a = 'Restart or shutdown the computer '
    q = 'If "yes" - shut down the computer, if "no" - restart the computer.'
    c = 'Rules'
    d = 'if the field is empty - leave the field blank.'
    f = 'Enter \'ok\' and this operation will start'
    g = 'Progress is - '
    h = 'Hours - '
    m = 'Minutes - '
    s = 'Seconds - '
    p = 'press button'

else:
    quit()

messagebox.showinfo(c, d.title())

root.wm_attributes('-alpha', 0.9)
root.iconbitmap('')  # указать путь к иконке
root.title(d.title())
root.resizable(False, False)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')

System = platform.system()


def message():
    return messagebox.askquestion('', f)


def ent():
    def down_progress(arg):
        def progress():
            n = 0
            while True:
                time.sleep(1)
                bar['value'] += (200 / res) / 2
                n += 1

                if n == res:
                    if System == 'Linux':
                        if arg == 's':
                            os.system('systemctl poweroff')
                        elif arg == 'r':
                            os.system('reboot')

                    if System == 'Windows':
                        if arg == 's':
                            os.system('shutdown -s')
                        elif arg == 'r':
                            os.system('shutdown -r')

        l_bar.grid(column=2, row=2)
        bar.grid(column=3, row=2)
        threading.Thread(target=progress).start()

    if hour.get() == '':
        h = 0
    else:
        h = int(hour.get())

    if minutes.get() == '':
        m = 0
    else:
        m = int(minutes.get())

    if second.get() == '':
        s = 1
    else:
        s = int(second.get())

    if isinstance(h < 25, int) and h < 25 or h > 0:
        if isinstance(m, int) and m < 61 or m > 0:
            if isinstance(s, int) and s < 61 or s != 0 or s > 0:
                if message() == 'yes':
                    h *= 3600
                    m *= 60
                    s *= 1
                    res = h + m + s

                    bar = Progressbar(root, length=200, style='green.Horizontal.TProgressbar')
                    l_bar = Label(root, text=g)

                    sms = messagebox.askyesnocancel(a, q)
                    if sms:
                        down_progress('s')
                    if not sms:
                        down_progress('r')
                    if sms is None:
                        pass


b = Button(root, text=p, command=ent)

l = Label(root, text=' ')
l_hour = Label(root, text=h)
l_minutes = Label(root, text=m)
l_second = Label(root, text=s)
l_e = Label(root, text=' ')

hour = Entry(root, width=2)
minutes = Entry(root, width=2)
second = Entry(root, width=2)

l.grid(column=0, row=0)
l_hour.grid(column=1, row=0)
hour.grid(column=2, row=0)
l_minutes.grid(column=3, row=0)
minutes.grid(column=4, row=0)
l_second.grid(column=6, row=0)
second.grid(column=7, row=0)
l_e.grid(column=8, row=0)
b.grid(column=3, row=1)

root.mainloop()
