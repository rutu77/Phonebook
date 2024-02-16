from tkinter import *
from tkinter import messagebox
import ast
from tkinter import ttk
from views import *
        
#Main Login Window
root = Tk()
root.title("Login")
root.geometry("1000x680+170+4")
root.configure(bg="#fff")
root.resizable(False, False)

#Sign in code
def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r+')
    d = file.read()
    r: object = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:

#############################PHONE-BOOK-CODE####################################
            #colors
            co0 = "#ffffff"
            co1 = "#000000"
            co2 = "#4456F0"

            #main window
            window = Toplevel(root)
            window.title("")
            window.geometry("1000x680+170+4")
            window.configure(background=co0)
            window.resizable(width=True,height=True)
           
            ###############input frames interface###################
            frame_up = Frame(window,width=1000,height=60,bg=co2)
            frame_up.grid(row=0,column=0,padx=0,pady=1)

            frame_down = Frame(window, width=1000, height=320, bg=co0)
            frame_down.grid(row=1, column=0, padx=0, pady=1)

            img = PhotoImage(file="phone.png")
            Label(frame_down, image=img, border=0, bg='white').place(x=400, y=40)

            frame_table = Frame(window, width=1500, height=100, bg=co0, relief='flat')
            frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky='')

            ############functions##############

            def show():
                global tree

                listheader = ['Name','Gender','Phone No.','Email','DOB']

                demo_list = view()

                tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

                vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
                hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

                tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

                #attaching the scroll bars
                tree.grid(column=0, row=0, sticky='nsew')
                vsb.grid(column=1, row=0, sticky='ns')
                hsb.grid(column=0, row=1, sticky='ew')

                #tree head (initializing the headings)
                tree.heading(0, text='Name', anchor=NW)
                tree.heading(1, text='Gender', anchor=NW)
                tree.heading(2, text='Phone No.', anchor=NW)
                tree.heading(3, text='Email', anchor=NW)
                tree.heading(4, text='DOB', anchor=NW)

                #tree column (initializing the data the columns)
                tree.column(0, width=120, anchor='nw')
                tree.column(1, width=50, anchor='nw')
                tree.column(2, width=100, anchor='nw')
                tree.column(3, width=180, anchor='nw')
                tree.column(4,width=100, anchor='nw')


                for item in demo_list:
                    tree.insert('','end',values=item)
            show()

            #insert function
            def insert():
                Name=e_name.get()
                Gender=c_gender.get()
                Telephone=e_telephone.get()
                Email=e_email.get()
                DOB =c_dob.get(),c_dobm.get(),c_doby.get()

                data=[Name,Gender,Telephone,Email,DOB]

                if Name==''or Gender=='' or Telephone=='' or Email =='' or DOB=='':
                    messagebox.showwarning('data','please fill in all the starred fieds')
                else:
                    add(data)
                    messagebox.showinfo('data','data added successfully')

                    e_name.delete(0,'end')
                    c_gender.delete(0,'end')
                    e_telephone.delete(0,'end')
                    e_email.delete(0,'end')
                    c_dob.delete(0,'end')
                    c_dobm.delete(0,'end')
                    c_doby.delete(0,'end')

                show()
                
           # Update function
            def to_update():
                try:
                    tree_data = tree.focus()
                    tree_dictionary = tree.item(tree_data)
                    tree_list = tree_dictionary['values']

                    Name = str(tree_list[0])
                    Gender = str(tree_list[1])
                    Telephone = int(tree_list[2])
                    Email = str(tree_list[3])

                    e_name.insert(0, Name)
                    c_gender.insert(0, Gender)
                    e_telephone.insert(0, Telephone)
                    e_email.insert(0, Email)

                    def confirm():
                        new_name = e_name.get()
                        new_gender = c_gender.get()
                        new_telephone = e_telephone.get()
                        new_email = e_email.get()

                        data = [new_name, new_gender, new_telephone, new_email]

                        success = update(data)

                        if success:
                            messagebox.showinfo('Success', 'Data updated successfully')
                            e_name.delete(0, 'end')
                            c_gender.delete(0, 'end')
                            e_telephone.delete(0, 'end')
                            e_email.delete(0, 'end')

                            # Refresh the table with updated data
                            for widget in frame_table.winfo_children():
                                widget.destroy()
                            b_confirm.destroy()
                            show()  # Assuming this function reloads data into the table
                        else:
                            messagebox.showerror('Error', 'No matching record found')

                    b_confirm = Button(frame_down, text='Confirm', width=10, height=1, command=confirm, bg=co2, fg=co0,
                                    font=('Ivy 8 bold'))
                    b_confirm.place(x=230, y=290)
                except IndexError:
                    messagebox.showerror('error', 'Select one of them from the table')



            #remove function
            def to_remove():
                try:
                    tree_data = tree.focus()
                    tree_dictionary = tree.item(tree_data)
                    tree_list = tree_dictionary['values']
                    tree_telephone =str(tree_list[2])

                    remove(tree_telephone)

                    messagebox.showinfo('Success','Data has been deleted successfully')

                    for widget in frame_table.winfo_children():
                            widget.destroy()
                except IndexError:
                    messagebox.showerror('error','Select one of them from the table')
                show()

            #remove all function
            def to_remove_all():
                tree_data = tree
                remove_all(tree_data)

                messagebox.showinfo('Success','All data has been deleted successfully')
                show()

            #search function
            def to_search():
                telephone = e_search.get()

                data = search(telephone)

                def delete_command():
                    tree.delete(*tree.get_children())
                delete_command()

                for item in data:
                    tree.insert('','end',values=item)
                    
                e_search.delete(0,'end')


            #####################################

            #frame_up code
            app_name = Label(frame_up, text="Phonebook",justify='center',height=1, font=('verdana 30 bold'), fg= co1)
            app_name.place(x=380,y=3)

            #frame_down code
            l_name = Label(frame_down, text="Name *", width=20, height=1, font=('Ivy 15'), bg=co0, anchor=NW)
            l_name.place(x=30,y=50)
            e_name = Entry(frame_down, width=25,justify='left', highlightthickness=2, relief='solid')
            e_name.place(x=150,y=50)

            l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=('Ivy 15'), bg=co0, anchor=NW)
            l_gender.place(x=30,y=90)
            c_gender = ttk.Combobox(frame_down, width=22)
            c_gender['values'] = ['','Male','Female']
            c_gender.place(x=150,y=90)

            l_telephone = Label(frame_down, text="Phone No. *", width=20, height=1, font=('Ivy 15'), bg=co0, anchor=NW)
            l_telephone.place(x=30,y=130)
            e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
            e_telephone.place(x=150,y=130)

            l_email = Label(frame_down, text="Email *", height=1, font=('Ivy 15'), bg=co0, anchor=NW)
            l_email.place(x=30,y=170)
            e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
            e_email.place(x=150,y=170)


            l_dob= Label(frame_down, text="DOB *", width=20, height=1, font=('Ivy 15'), bg=co0, anchor=NW)
            l_dob.place(x=30,y=210)

            c_dob = ttk.Combobox(frame_down, width=4)
            c_dob['values'] = [*range(1,31)]
            c_dob.place(x=150,y=210)

            c_dobm = ttk.Combobox(frame_down, width=6)
            c_dobm['values'] = ['','Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
            c_dobm.place(x=198,y=210)

            c_doby = ttk.Combobox(frame_down, width=5)
            c_doby['values'] = [*range(1900,2025)]
            c_doby.place(x=258,y=210)

            l_search = Label(frame_down,text="Search No.",height=1,font=('Ivy 15'),bg=co0,anchor=NW)
            l_search.place(x=30,y=250)
            e_search = Entry(frame_down, width=16 , justify='left',font=('Ivy',11), highlightthickness=1, relief='solid')
            e_search.place(x=150,y=250)
            ###############Feature interface#####################3
            heading = Label(frame_down,text='Features',fg='#57a1f8',bg='white',font=('Sitka Text Semibold',17,'bold'))
            heading.place(x=764,y=10)

            b_add = Button(frame_down,width=25,pady=7,text='Add Contact',bg='#57a1f8',fg='white',border=0,command=insert)
            b_add.place(x=730,y=45)

            b_remove = Button(frame_down,width=25,pady=7,text='Remove Contact',bg='#57a1f8',fg='white',border=0,command=to_remove)
            b_remove.place(x=730,y=95)

            b_update = Button(frame_down,width=25,pady=7,text='Update Contact',bg='#57a1f8',fg='white',border=0,command=to_update)
            b_update.place(x=730,y=145)

            b_search = Button(frame_down,width=25,pady=7,text='Search Contact',bg='#57a1f8',fg='white',border=0,command=to_search)
            b_search.place(x=730,y=195)

            b_Delall = Button(frame_down,width=25,pady=7,text='Delete all Contact',bg='#57a1f8',fg='white',border=0,command=to_remove_all)
            b_Delall.place(x=730,y=245)

            window.after(1000,mainloop)     

            window.mainloop()
######################################################################################
    else:
        messagebox.showerror('Invalid', 'invalid username and password')
###################################################################################
def signup_command():
    window1 = Toplevel(root)
    window1.title("SignUp")
    window1.geometry("1000x680+170+4")
    window1.configure(bg="#fff")
    window1.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfully Sign up')

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', 'Both  password should  match')

    def sign():
        window1.destroy()

    img = PhotoImage(file="signup.png")
    Label(window1, image=img, border=0, bg='white').place(x=10, y=90)

    frame = Frame(window1, width=350, height=400, bg='#fff')
    frame.place(x=600, y=100)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Sitka Text Semibold', 33, 'bold'))
    heading.place(x=100, y=5)

    #####--------------------------------------------------------

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=80, y=100)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=1, bg='black').place(x=75, y=127)

    #####----------------------------------------------------

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=80, y=170)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=1, bg='black').place(x=75, y=197)

    #####----------------------------------------------------

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        name = confirm_code.get()
        if name == '':
            confirm_code.insert(0, 'Confirm Password')

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=80, y=240)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=1, bg='black').place(x=75, y=267)

    ############################################
    Button(frame, width=35, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=90,
                                                                                                              y=300)
    label = Label(frame, text="I already have an account.", fg='black', bg='white',
                  font=('Microsoft YaHei UI Light', 9))
    label.place(x=115, y=340)

    signin = Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=260, y=340)

    window1.mainloop()

####################################################################################

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=400, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Sitka Text Semibold', 33, 'bold'))
heading.place(x=140, y=55)

###################------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=100, y=160)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=1, bg='black').place(x=100, y=187)

#################--------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=100, y=230)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=1, bg='black').place(x=100, y=257)
##################################################################3

Button(frame, width=35, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=100, y=284)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=135, y=320)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                 command=signup_command)
sign_up.place(x=270, y=320)

root.mainloop()
