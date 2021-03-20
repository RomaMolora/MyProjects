﻿from tkinter import *
import datetime
import csv
import time


class Window:
    """Create window"""

    def __init__(self):
        self.root = Tk()
        self.__temp = 0  # time
        self.__id = ''  # I have no idea, but without it it doesn't work

        self.time = Label(self.root,
                          font=('Ubuntu', 100),
                          text='00:00:00'
                          )

        self.start = Button(self.root,
                            command=self.start,
                            text='start'
                            )

        self.stop_ = Button(self.root,
                            command=lambda: self.stop(),
                            text='stop'
                            )

        self.continue_ = Button(self.root,
                                command=lambda: self.cont(),
                                text='continue'
                                )

        self.save = Button(self.root,
                           text='save',
                           command=lambda: self.save_()
                           )

        self.packs()  # accommodation packs this method

    def packs(self):
        """packs one label(time) and 4 buttons"""
        self.time.pack()
        self.start.pack()

    def start(self):
        """start timer"""
        self.start.pack_forget()  # hide button start
        self.stop_.pack()  # show button stop
        self.tick()  # recursion method tick

    def stop(self):
        """stop timer"""
        self.root.after_cancel(self.__id)  # something like a while loop(stops him)
        self.stop_.pack_forget()  # hide button stop
        self.continue_.pack()  # show button continue
        self.save.pack()  # show button save

    def cont(self):
        """continue work this program"""
        self.tick()  # recursion method tick
        self.continue_.pack_forget()  # hide button continue
        self.stop_.pack()  # show button stop
        self.save.pack_forget()  # hide button save

    def save_(self):
        """saves time to file with csv extension"""
        today = datetime.date.today()  # today date
        today = str(today)  # transform in type str
        list_today = [today]  # append
        self.temp_replace = str(int(self.__temp / 60 / 60))  # int hours

        # add a normal view of the result to the file
        self.f_temp = str(self.f_temp)
        self.f_temp = list(self.f_temp)
        self.f_temp.pop(1)
        self.f_temp.insert(1, self.temp_replace)
        self.f_temp = ''.join(self.f_temp)

        # this to add to the csv file
        list_time = [self.f_temp]
        list_everything = []
        list_everything.extend(list_today)
        list_everything.extend(list_time)

        # open csv file
        with open('Time work.csv', 'a') as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(list_everything)

    def run(self):
        """run program"""
        self.root.mainloop()

    def tick(self):
        """something like a while loop"""
        time.sleep(1)
        self.__id = self.root.after(1, self.tick)
        self.f_temp = datetime.datetime.fromtimestamp(self.__temp).strftime('%H:%M:%S')  #
        self.time.configure(text=str(self.f_temp))  # replace text label time
        self.__temp += 1


if __name__ == '__main__':  # main
    w = Window()
    w.run()  # run
