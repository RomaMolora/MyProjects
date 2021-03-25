import tkinter
from tkinter import messagebox
import datetime
import csv
import time


class Window:
    """Create window"""
    count_attr = 0

    def __init__(self):
        Window.count_attr += 1
        if Window.count_attr > 1:
            raise AttributeError

        self.root = tkinter.Tk()

        self.root.protocol("WM_DELETE_WINDOW", [
            messagebox.showinfo('', 'Press "escape" to exit'),
            self.root.iconify,
        ])
        self.root.bind('<Escape>', lambda a: self.root.destroy())

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f"+{width}+{height}")

        self._saved = tkinter.Label(self.root, text='saved')
        self.root.resizable(0, 0)
        self.root.title('tick tack')

        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.9)
        self.root.attributes("-topmost", True)

        self.f_temp = ''

        self.__temp = 0  # time
        self.__id = ''  # I have no idea, but without it it doesn't work
        self.time = tkinter.Label(self.root,
                                  font=('Ubuntu', 30),
                                  text='00:00:00'
                                  )

        self.start_button = tkinter.Button(self.root,
                                           command=self.start_program,
                                           text='start'
                                           )

        self.stop_ = tkinter.Button(self.root,
                                    command=self.stop,
                                    text='stop'
                                    )

        self.continue_ = tkinter.Button(self.root,
                                        command=self.cont,
                                        text='continue'
                                        )

        self.save = tkinter.Button(self.root,
                                   text='save',
                                   command=self.save_
                                   )

        self.move_ = tkinter.Button(self.root,
                                    text='move',
                                    command=self.move
                                    )

        self.packs()  # accommodation packs this methods

    # def __setattr__(self, key, value):
    #     print(key, value)

    def packs(self):
        """packs one label(time) and 4 buttons"""
        self.time.pack()
        self.start_button.pack()
        self.move_.pack()

    def move(self):
        """move window"""
        if self.root.wm_overrideredirect():
            self.root.overrideredirect(False)
        else:
            self.root.overrideredirect(True)
        self.root.update()

    def start_program(self):
        """start timer"""
        self.start_button.pack_forget()  # hide button start
        self.stop_.pack()  # show button stop
        self.tick()  # recursion method tick

    def stop(self):
        """stop timer"""
        self.root.after_cancel(self.__id)  # something like a while loop
        self.stop_.pack_forget()  # hide button stop
        self.continue_.pack()  # show button continue
        self.save.pack()  # show button save

    def cont(self):
        """continue work this program"""
        self.tick()  # recursion method tick
        self.continue_.pack_forget()  # hide button continue
        self.stop_.pack()  # show button stop
        self.save.pack_forget()  # hide button save
        self._saved.pack_forget()

    def save_(self):
        """saves time to file with csv extension"""
        today = datetime.date.today()  # today date
        today = str(today)  # transform in type str
        list_today = [today]  # append
        self.temp_replace = str(int(self.__temp / 60 / 60))  # int hours
        self._saved.pack()

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
        with open('Time work.csv', 'a') as time_work:
            csv.writer(time_work, delimiter=',').writerow(list_everything)
        self.__temp = 0

    def tick(self):
        """something like a while loop"""
        time.sleep(0.1)
        self.__id = self.root.after(1000, self.tick)
        self.f_temp = datetime.datetime.utcfromtimestamp(self.__temp).strftime('%H:%M:%S')
        self.time.configure(text=str(self.f_temp))  # replace text label time
        self.__temp += 1

    def run(self):
        """run program"""
        self.root.mainloop()


# self.root.wait_visibility(self.root)
# self.root.attributes("-alpha", 0.9)
# root.geometry("+0+0")


if __name__ == '__main__':  # main
    Window().run()  # run program
