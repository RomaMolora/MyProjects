from tkinter import *
import datetime
import csv


class Window:
    def __init__(self):
        self.root = Tk()
        self.__temp = 0
        self.__id = ''
        self.save = []

        self.l = Label(self.root,
                       font=('Ubuntu', 100),
                       text='00:00:00'
                       )

        self.b = Button(self.root,
                        command=self.start,
                        text='start'
                        )

        self.b_stop = Button(self.root,
                             command=lambda: self.stop(),
                             text='stop'
                             )

        self.b_cont = Button(self.root,
                             command=lambda: self.cont(),
                             text='continue'
                             )

        self.b_save = Button(self.root,
                             text='save',
                             command=lambda: self.save_()
                             )

        self.packs()

    def packs(self):
        self.l.pack()
        self.b.pack()

    def start(self):
        self.b.pack_forget()
        self.b_stop.pack()
        self.tick()

    def stop(self):
        self.root.after_cancel(self.__id)
        self.b_stop.pack_forget()
        self.b_cont.pack()
        self.b_save.pack()

    def cont(self):
        self.tick()
        self.b_cont.pack_forget()
        self.b_stop.pack()
        self.b_save.pack_forget()

    def save_(self):
        today = datetime.date.today()
        today = str(today)
        list_today = [today]
        self.temp_replace = str(int(self.__temp / 60 / 60))

        self.f_temp = str(self.f_temp)
        self.f_temp = list(self.f_temp)
        self.f_temp.pop(1)
        self.f_temp.insert(1, self.temp_replace)
        self.f_temp = ''.join(self.f_temp)

        list_time = [self.f_temp]
        list_everything = []
        list_everything.extend(list_today)
        list_everything.extend(list_time)

        with open('Time work.csv', 'a') as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(list_everything)

    def run(self):
        self.root.mainloop()

    def tick(self):
        import time
        time.sleep(1)
        self.__id = self.root.after(1, self.tick)
        self.f_temp = datetime.datetime.fromtimestamp(self.__temp).strftime('%H:%M:%S')
        self.l.configure(text=str(self.f_temp))
        self.__temp += 1


if __name__ == '__main__':
    w = Window()
    w.run()
