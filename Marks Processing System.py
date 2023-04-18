from tkinter import *
from tkinter import messagebox as msg

stu_det = []

login = Tk()
login.geometry('1400x720')

l_un = Label(login, text='Username:', font=('Comic Sans MS', 20)).place(x=200, y=100)
l_pw = Label(login, text='Password:', font=('Comic Sans MS', 20)).place(x=200, y=150)

e_un = Entry(login, font=('Comic Sans MS', 20), width=20)
e_un.place(x=400, y=100)
e_pw = Entry(login, font=('Comic Sans MS', 20), width=20)
e_pw.place(x=400, y=150)


def login_submit():
    def mm_add():

        def add_add():
            stu_det.append([e_add_rn.get(), e_add_name.get(), e_add_me.get(), e_add_mp.get(), e_add_mch.get(),
                            e_add_mm.get(), e_add_mcs.get()])
            e_add_rn.delete(0, END)
            e_add_name.delete(0, END)
            e_add_me.delete(0, END)
            e_add_mp.delete(0, END)
            e_add_mch.delete(0, END)
            e_add_mm.delete(0, END)
            e_add_mcs.delete(0, END)

            msg.showinfo('Message!', 'Details Added')

            e_add_rn.focus_set()

        def add_back():
            add.withdraw()
            mm.deiconify()

        def add_qt():
            add.destroy()

        mm.withdraw()
        add = Tk()
        add.geometry('1400x720')
        add_head = Label(add, text='Add Window', font=('Comic Sans MS', 20)).pack()

        l_add_rn = Label(add, text='Enter Roll No:', font=('Comic Sans MS', 20)).place(x=200, y=100)
        l_add_name = Label(add, text='Enter Name:', font=('Comic Sans MS', 20)).place(x=200, y=150)
        l_add_me = Label(add, text='Enter English Mark:', font=('Comic Sans MS', 20)).place(x=200, y=200)
        l_add_mp = Label(add, text='Enter Physics Mark:', font=('Comic Sans MS', 20)).place(x=200, y=250)
        l_add_mch = Label(add, text='Enter Chemistry Mark:', font=('Comic Sans MS', 20)).place(x=200, y=300)
        l_add_mm = Label(add, text='Enter Maths Mark:', font=('Comic Sans MS', 20)).place(x=200, y=350)
        l_add_mcs = Label(add, text='Enter CS Mark:', font=('Comic Sans MS', 20)).place(x=200, y=400)

        e_add_rn = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_rn.place(x=500, y=100)
        e_add_name = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_name.place(x=500, y=150)
        e_add_me = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_me.place(x=500, y=200)
        e_add_mp = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_mp.place(x=500, y=250)
        e_add_mch = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_mch.place(x=500, y=300)
        e_add_mm = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_mm.place(x=500, y=350)
        e_add_mcs = Entry(add, font=('Comic Sans MS', 20), width=20)
        e_add_mcs.place(x=500, y=400)

        b_add_add = Button(add, command=add_add, text='Add', font=('Comic Sans MS', 15), width=9)
        b_add_add.place(x=0, y=600)
        b_add_back = Button(add, command=add_back, text='Back to\n Main Menu', font=('Comic Sans MS', 15),
                            width=9)
        b_add_back.place(x=600, y=600)
        b_add_qt = Button(add, command=add_qt, text='Exit', font=('Comic Sans MS', 15), width=9)
        b_add_qt.place(x=1100, y=600)

    def mm_disp():

        def disp_back():
            disp.withdraw()
            mm.deiconify()

        mm.withdraw()
        disp = Tk()
        disp.geometry('1400x720')
        disp_head = Label(disp, text='Display Window', font=('Comic Sans MS', 20)).pack()

        disp_tb = Text(disp, height=50, width=52, font=('Comic Sans MS', 20))
        disp_tb.place(x=100, y=100)
        disp_tb.insert(END, '=========================================================\n')
        disp_tb.insert(END, '                             STUDENT DETAILS\n')
        disp_tb.insert(END, '=========================================================\n')
        disp_tb.insert(END, 'Roll No\tName\tEnglish\tPhysics\tChem\tMath\tCS\n')
        for i in stu_det:
            disp_tb.insert(END, i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3] + '\t' + i[4] + '\t' + i[5] + '\t' + i[
                6] + '\n')

        b_disp_back = Button(disp, command=disp_back, text='Back to\n Main Menu', font=('Comic Sans MS', 15),
                             width=9)
        b_disp_back.place(x=1000, y=200)

    def mm_upd():

        def upd_upd():
            stu_det[ind] = [e_upd_rn.get(), e_upd_name.get(), e_upd_me.get(), e_upd_mp.get(),
                            e_upd_mch.get(), e_upd_mm.get(), e_upd_mcs.get()]
            msg.showinfo('Display Popup', 'Details Updated')
            upd.withdraw()
            mm.deiconify()

        def upd_back():
            upd.withdraw()
            mm.deiconify()

        rn_list = [i[0] for i in stu_det]

        if e_mm_upd.get() in rn_list:
            ind = rn_list.index(e_mm_upd.get())

            e_mm_upd.delete(0, END)
            mm.withdraw()
            upd = Tk()
            upd.geometry('1400x720')
            upd_head = Label(upd, text='Update Window', font=('Comic Sans MS', 20)).pack()

            l_upd_rn = Label(upd, text='Update Roll No:', font=('Comic Sans MS', 20)).place(x=200, y=100)
            l_upd_name = Label(upd, text='Update Name:', font=('Comic Sans MS', 20)).place(x=200, y=150)
            l_upd_me = Label(upd, text='Update English Mark:', font=('Comic Sans MS', 20)).place(x=200, y=200)
            l_upd_mp = Label(upd, text='Update Physics Mark:', font=('Comic Sans MS', 20)).place(x=200, y=250)
            l_upd_mch = Label(upd, text='Update Chemistry Mark:', font=('Comic Sans MS', 20)).place(x=200, y=300)
            l_upd_mm = Label(upd, text='Update Maths Mark:', font=('Comic Sans MS', 20)).place(x=200, y=350)
            l_upd_mcs = Label(upd, text='Update CS Mark:', font=('Comic Sans MS', 20)).place(x=200, y=400)

            e_upd_rn = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_rn.place(x=500, y=100)
            e_upd_rn.insert(0, stu_det[ind][0])
            e_upd_name = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_name.place(x=500, y=150)
            e_upd_name.insert(0, stu_det[ind][1])
            e_upd_me = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_me.place(x=500, y=200)
            e_upd_me.insert(0, stu_det[ind][2])
            e_upd_mp = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_mp.place(x=500, y=250)
            e_upd_mp.insert(0, stu_det[ind][3])
            e_upd_mch = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_mch.place(x=500, y=300)
            e_upd_mch.insert(0, stu_det[ind][4])
            e_upd_mm = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_mm.place(x=500, y=350)
            e_upd_mm.insert(0, stu_det[ind][5])
            e_upd_mcs = Entry(upd, font=('Comic Sans MS', 20), width=20)
            e_upd_mcs.place(x=500, y=400)
            e_upd_mcs.insert(0, stu_det[ind][6])

            b_upd_upd = Button(upd, command=upd_upd, text='Update', font=('Comic Sans MS', 15), width=9)
            b_upd_upd.place(x=0, y=600)
            b_upd_back = Button(upd, command=upd_back, text='Back to\n Main Menu', font=('Comic Sans MS', 15),
                                width=9)
            b_upd_back.place(x=600, y=600)


        else:
            msg.showinfo('Error', 'Roll No not Found!')
            e_mm_upd.delete(0)
            e_mm_upd.focus_set()

    def mm_del():

        def del_del():
            stu_det.remove(stu_det[ind])
            del_conf.withdraw()
            msg.showinfo('Popup', 'Entry Deleted')
            mm.deiconify()

        def del_back():
            del_conf.withdraw()
            mm.deiconify()

        rn_list = [i[0] for i in stu_det]

        if e_mm_del.get() in rn_list:
            mm.withdraw()

            ind = rn_list.index(e_mm_del.get())

            e_mm_del.delete(0, END)

            del_conf = Tk()
            del_conf.geometry('300x300')

            del_head = Label(del_conf, text='Confirm deletion?', font=('Comic Sans MS', 20)).pack()
            del_but = Button(del_conf, command=del_del, text='Confirm', font=('Comic Sans MS', 15), width=9).pack()

            b_upd_back = Button(del_conf, command=del_back, text='Back to\n Main Menu', font=('Comic Sans MS', 15),
                                width=9).pack()


        else:
            msg.showinfo('Error', 'Roll No not Found!')
            e_mm_del.delete(0)
            e_mm_del.focus_set()

    def mm_log():
        mm.withdraw()
        login.deiconify()

    def mm_qt():
        mm.destroy()

    if e_un.get() == 'a' and e_pw.get() == 'a':
        login.withdraw()
        mm = Tk()
        mm.geometry('1400x720')
        mm_head = Label(mm, text='Main Menu', font=('Comic Sans MS', 20)).pack()

        b_mm_add = Button(mm, command=mm_add, text='Add', font=('Comic Sans MS', 15), width=8)
        b_mm_disp = Button(mm, command=mm_disp, text='Display', font=('Comic Sans MS', 15), width=8)
        b_mm_upd = Button(mm, command=mm_upd, text='Update', font=('Comic Sans MS', 15), width=8)
        b_mm_del = Button(mm, command=mm_del, text='Delete', font=('Comic Sans MS', 15), width=8)
        b_mm_log = Button(mm, command=mm_log, text='Back to\n Login', font=('Comic Sans MS', 15), width=8)
        b_mm_qt = Button(mm, command=mm_qt, text='Quit', font=('Comic Sans MS', 15), width=8)

        l_mm_upd = Label(mm, text='Enter Roll No to Update:', font=('Comic Sans MS', 15))
        e_mm_upd = Entry(mm, font=('Comic Sans MS', 20), width=10)

        l_mm_del = Label(mm, text='Enter Roll No to Delete:', font=('Comic Sans MS', 15))
        e_mm_del = Entry(mm, font=('Comic Sans MS', 20), width=10)

        b_mm_add.place(x=450, y=200)
        b_mm_disp.place(x=450, y=250)
        b_mm_upd.place(x=450, y=300)
        l_mm_upd.place(x=600, y=300)
        e_mm_upd.place(x=900, y=300)
        b_mm_del.place(x=450, y=350)
        l_mm_del.place(x=600, y=350)
        e_mm_del.place(x=900, y=350)
        b_mm_log.place(x=100, y=650)
        b_mm_qt.place(x=1300, y=650)
    else:
        msg.showinfo('Error', 'Incorrect Password')


b_sub = Button(login, command=login_submit, text='Submit', font=('Comic Sans MS', 15), width=8)
b_sub.place(x=600, y=400)

login.mainloop()
