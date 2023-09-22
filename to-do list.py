import tkinter as tk
from tkinter import Frame, Listbox
from tkinter import *
from tkinter.messagebox import askyesno
import sqlite3

conn = sqlite3.connect('Tasks.db')
cr = conn.cursor()
cr.execute('CREATE TABLE IF NOT EXISTS today (tasks)')
cr.execute('CREATE TABLE IF NOT EXISTS tomorrow (tasks)')
cr.execute('CREATE TABLE IF NOT EXISTS plan (tasks)')

main_window = tk.Tk()
main_window.geometry('400x520+340+100')
main_window.resizable(False, False)
main_window.title('To_do')
icon = tk.PhotoImage(file=r"d:\MSA\python projects\to-do list\photos\to-do-list.png")
main_window.iconphoto(False, icon)

class Today():

    list_of_tasks = []

    def __init__(self):
        self.window_today = tk.Toplevel()
        self.window_today.geometry('400x520+340+100')
        self.window_today.resizable(False, False)
        self.window_today.title('Today')
        icon_today = tk.PhotoImage(file=r"d:\MSA\python projects\to-do list\photos\today.png")
        self.window_today.iconphoto(False, icon_today)
        self.window_today.protocol("WM_DELETE_WINDOW", self.save)

        self.my_frame = Frame(self.window_today)
        self.my_frame.pack(pady= 10)

        self.my_list_box = Listbox(self.my_frame, font=8, width=35, height=15, bg='cadetblue3', bd=0)
        self.my_list_box.pack()

        self.tasks()

        self.b_1_today = tk.Button(self.window_today, text='⬆', width=5, bg='cornflowerblue', font=8, command=self.real_add)
        self.b_1_today.place(x=330, y=440)

        self.b_1_today = tk.Button(self.window_today, text='❌', width=5, bg='cornflowerblue', font=8, command=self.delete)
        self.b_1_today.place(x=260, y=440)

        self.e_today = tk.Entry(self.window_today, width=20, bg='cornflowerblue', fg='white', font=8)
        self.e_today.place(x=19, y=440, height=36)

    def delete(self):
        selected_indices = self.my_list_box.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            task = self.my_list_box.get(selected_index)
            self.my_list_box.delete(selected_index)
            cr.execute('DELETE FROM today WHERE tasks=(?)', (task,))
        else:
            print("No item selected.")


    def add(self):
        task = self.e_today.get()
        self.list_of_tasks.append(task)
        self.my_list_box.insert(END, task)
        self.e_today.delete(0, END)
        return self.list_of_tasks
    
    def real_add(self):
        tasks = self.add()
        for t in tasks:
            cr.execute('INSERT INTO today VALUES (?)', (t,))

    def save(self):
        if askyesno(title='Exit', message='Do you want to exit ?'):
            conn.commit()
            conn.close()
            self.window_today.destroy()
            main_window.destroy()


    def tasks(self):
        cr.execute('SELECT * FROM today')
        for t in cr.fetchall():
            self.my_list_box.insert(END, t[0])

class Tomorrow(Today):

    def __init__(self):
        self.window_tomorrow = tk.Toplevel()
        self.window_tomorrow.geometry('400x520+340+100')
        self.window_tomorrow.resizable(False, False)
        self.window_tomorrow.title('Tomorrow')
        icon_tomorrow = tk.PhotoImage(file=r"d:\MSA\python projects\to-do list\photos\tomorrow.png")
        self.window_tomorrow.iconphoto(False, icon_tomorrow)
        self.window_tomorrow.protocol("WM_DELETE_WINDOW", self.save)

        self.my_frame = Frame(self.window_tomorrow)
        self.my_frame.pack(pady= 10)

        self.my_list_box = Listbox(self.my_frame, font=8, width=35, height=20, bg='cadetblue3', bd=0)
        self.my_list_box.pack()

        self.tasks()

        self.b_1_today = tk.Button(self.window_tomorrow, text='⬆', width=5, bg='cornflowerblue', font=8, command=self.add)
        self.b_1_today.place(x=330, y=440)

        self.b_1_today = tk.Button(self.window_tomorrow, text='❌', width=5, bg='cornflowerblue', font=8, command=self.delete)
        self.b_1_today.place(x=260, y=440)

        self.e_today = tk.Entry(self.window_tomorrow, width=25, bg='cornflowerblue', fg='white', font=8)
        self.e_today.place(x=19, y=440, height=30)

    def delete(self):
        return super().delete()
    
    def add(self):
        return super().add()
    
    def real_add(self):
        tasks = self.add()
        for t in tasks:
            cr.execute('INSERT INTO tomorrow VALUES (?)', (t,))
        raise NotImplementedError('you shoul change the table')

    def save(self):
        if askyesno(title='Exit', message='Do you want to exit ?'):
            conn.commit()
            conn.close()
            self.window_tomorrow.destroy()
            main_window.destroy()
    
    def tasks(self):
        return super().tasks()
    
class plan(Today):

    def __init__(self):
        self.window_Plan = tk.Toplevel()
        self.window_Plan.geometry('400x520+340+100')
        self.window_Plan.resizable(False, False)
        self.window_Plan.title('Plan')
        icon_plan = tk.PhotoImage(file=r"D:\MSA\python projects\to-do list\photos\plan.png")
        self.window_Plan.iconphoto(False, icon_plan)
        self.window_plan.protocol("WM_DELETE_WINDOW", self.save)

        self.my_frame = Frame(self.window_Plan)
        self.my_frame.pack(pady= 10)

        self.my_list_box = Listbox(self.my_frame, font=8, width=35, height=20, bg='cadetblue3', bd=0)
        self.my_list_box.pack()

        self.tasks()

        self.b_1_today = tk.Button(self.window_Plan, text='⬆', width=5, bg='cornflowerblue', font=8, command=self.add)
        self.b_1_today.place(x=330, y=440)

        self.b_1_today = tk.Button(self.window_Plan, text='❌', width=5, bg='cornflowerblue', font=8, command=self.delete)
        self.b_1_today.place(x=260, y=440)

        self.e_today = tk.Entry(self.window_Plan, width=25, bg='cornflowerblue', fg='white', font=8)
        self.e_today.place(x=19, y=440, height=30)

    def delete(self):
        return super().delete()
    
    def add(self):
        return super().add()
    
    def real_add(self):
        tasks = self.add()
        for t in tasks:
            cr.execute('INSERT INTO plan VALUES (?)', (t,))
        raise NotImplementedError('you shoul change the table')

    def save(self):
        if askyesno(title='Exit', message='Do you want to exit ?'):
            conn.commit()
            conn.close()
            self.window_plan.destroy()
            main_window.destroy()
    
    def tasks(self):
        return super().tasks()

text_1 = tk.Label(text='Hello, in your To-Do-list.\n Choose any option, please.', bg='cadetblue3', fg='black', font=2)
text_1.pack(fill='x')

button_1 = tk.Button(text='Today', width=32, height=1, bg='cornflowerblue', fg='white', font=9, command=Today)
button_1.place(x=19, y=240)
button_2 = tk.Button(text='Tomorrow', width=32, height=1, bg='cornflowerblue', fg='white', font=9, command=Tomorrow)
button_2.place(x=19, y=290)
button_3 = tk.Button(text='Plan', width=32, height=1, bg='cornflowerblue', fg='white', font=9, command=plan)
button_3.place(x=19, y=340)
button_4 = tk.Button(text='quit', width=32, height=1, bg='cornflowerblue', fg='white', font=9, command=main_window.destroy)
button_4.place(x=19, y=390)

image = tk.PhotoImage(file=r"D:\MSA\python projects\to-do list\photos\task.png")
resized_image = image.subsample(3)
label = tk.Label(main_window, image=resized_image)
label.pack()

main_window.mainloop()