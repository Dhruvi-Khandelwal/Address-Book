#Importing the tkinter library
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import mysql.connector
import os

#=======================================Splash Window================================#
#Create an instance of tkinter frame
splash_win= Tk()

#Set the title of the  Splash Window
splash_win.title("Splash Screen")

#Define the size of the window or frame
splash_win.geometry("1920x1080")

#Applying Background Image
splash_bg=ImageTk.PhotoImage(file='splashbg.jpg')
canvas1 = Canvas(splash_win,width = 1920, height = 1080)
canvas1.pack(fill='both',expand='True')
canvas1.create_image(0,0,image=splash_bg,anchor="nw")

#Applying Logo
my_image = ImageTk.PhotoImage(file="photo.jpg")
canvas1.create_image(800, 400, anchor= CENTER, image = my_image)

#Remove border of the splash Window
splash_win.overrideredirect(True)

#Splash Screen Effect(Entering Main Window)
def mainWin():
   splash_win.destroy()
   #======================================MAIN WINDOW=================================#
   global Label1,Label2,new_address_button,view_list_button
   root=Tk()
   root.title('Address Box')
   root.geometry('1920x1080')
   root.iconbitmap('pic2-1.ico')

   #Applying bg image
   bg=ImageTk.PhotoImage(file='bg pic.jpg')
   Canvas2=Canvas(root,height=1920,width=1080)
   Canvas2.pack(fill="both",expand="True")
   Canvas2.create_image(0,0,image=bg,anchor="nw")

   Frame_main=Frame(root,bg='#8cbbf1',bd=15,borderwidth=15,relief=RIDGE)
   Frame_main.place(x=350,y=150,width=900,height=540)


   #placing logo and title
   my_pic=Image.open('Pic2.jpg')
   resize_image=my_pic.resize((85,85),Image.ANTIALIAS)
   image1=ImageTk.PhotoImage(resize_image)
   Label1=Label(root,image=image1,borderwidth=0).place(x=630,y=200)

   my_pic2=Image.open('Pic1.jpg')
   resize_image2=my_pic2.resize((250,85),Image.ANTIALIAS)
   image2=ImageTk.PhotoImage(resize_image2)
   Label2=Label(root,image=image2,borderwidth=0).place(x=725,y=200)

   #MySQL connection
   mydb=mysql.connector.connect(
      host='localhost',
      user='root',
      passwd='root',
      auth_plugin='mysql_native_password'
      )
   my_cursor=mydb.cursor()

   #CREATING DATABASE
   my_cursor.execute("create database IF NOT EXISTS address_list")
   #MySQL connection part 2   
   mydb=mysql.connector.connect(
      host='localhost',
      user='root',
      passwd='root',
      database='address_list',
      auth_plugin='mysql_native_password'
      )
   my_cursor=mydb.cursor()

   #CREATING TABLE
   my_cursor.execute("create table IF NOT EXISTS Addresses(Contact_ID Int PRIMARY KEY,\
      First_Name Varchar(20),\
      Last_Name Varchar(20),\
      Address Varchar(350),\
      Gender Varchar(10),\
      Email_Address Varchar(40),\
      Contact_No Int(10))")

   #defining commmands
   def add_new():
       #===========================================NEW ADDRESS WINDOW========================================#
        new=Tk()
        new.title('New Address')
        new.geometry('1580x720+0+50')
        new.iconbitmap('pic2-1.ico')
        bg_color='#8cbbf1'

        #functions(commands)

        def add():
            if Contact_ID_Box.get()=='' or First_Name_Box.get()=='' or Last_Name_Box.get()=='' or Address_Box.get()=='' or Gender_Box.get()=='' or Email_Address_Box.get()=='' or Contact_No_Box.get()=='':
                messagebox.showerror('Error','All fields are required')
            else:
                 sqlStuff="INSERT INTO Addresses( Contact_Id,First_Name,Last_Name,Address,Gender,Email_Address,Contact_No)VALUES(%s,%s,%s,%s,%s,%s,%s)"
                 Record=(Contact_ID_Box.get(),First_Name_Box.get(),Last_Name_Box.get(),Address_Box.get(),Gender_Box.get(),Email_Address_Box.get(),Contact_No_Box.get())
                 my_cursor.execute(sqlStuff,Record)
                 mydb.commit()
                 messagebox.showinfo("Add Address","Record added successfully")
                 return
                 #Clear Fields
                 reset()

        def reset():
            Contact_ID_Box.delete(0,END)
            First_Name_Box.delete(0,END)
            Last_Name_Box.delete(0,END)
            Address_Box.delete(0,END)
            Gender_Box.set('Select Gender')
            Email_Address_Box.delete(0,END)
            Contact_No_Box.delete(0,END)
            
        def Exit1():
            i= messagebox.askyesno('Exit','Do you want to exit')
            if i>0:
                   new.destroy()

    

        #Heading
        title=Label(new,text='New Address',bg=bg_color,fg='black',font=('Cooper Std Black',35,'bold'),relief=GROOVE,bd=12)
        title.pack(fill=X)

        #left frame details
        F1=Frame(new,bg=bg_color,relief=RIDGE)
        F1.place(x=10,y=80,width=650,height=540)
        
        Contact_ID_Label=Label(F1,text='Contact  ID',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Contact_ID_Label.grid(row=0,column=0,padx=30,pady=10)
        Contact_ID_Box=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Contact_ID_Box.grid(row=0,column=1,pady=10,sticky='w')

        First_Name_Label=Label(F1,text='First Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        First_Name_Label.grid(row=1,column=0,padx=30,pady=10)
        First_Name_Box=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        First_Name_Box.grid(row=1,column=1,pady=10,sticky='w')

        Last_Name_Label=Label(F1,text='Last Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Last_Name_Label.grid(row=2,column=0,padx=30,pady=10)
        Last_Name_Box=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Last_Name_Box.grid(row=2,column=1,pady=10,sticky='w')

        Address_Label=Label(F1,text='Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Address_Label.grid(row=3,column=0,padx=30,pady=10)
        Address_Box=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Address_Box.grid(row=3,column=1,pady=10,sticky='w')

        Gender_Label=Label(F1,text='Gender',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Gender_Label.grid(row=4,column=0,padx=30,pady=10)
        Gender_Box=ttk.Combobox(F1,font=('times new rommon',18,'bold'),state='readonly')
        Gender_Box['values']=('Select Gender','Male','Female','Others')
        Gender_Box.current(0)
        Gender_Box.grid(row=4,column=1,pady=10,sticky='w')

        Email_Address_Label=Label(F1,text='Email Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Email_Address_Label.grid(row=5,column=0,padx=30,pady=10)
        Email_Address_Box=Entry(F1, font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Email_Address_Box.grid(row=5,column=1,pady=10)

        Contact_No_Label=Label(F1,text='Contact No.',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Contact_No_Label.grid(row=6,column=0,padx=30,pady=10)
        Contact_No_Box=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Contact_No_Box.grid(row=6,column=1,pady=10,sticky='w')

        #Right frame
        Frame2=Frame(new,bg=bg_color,relief=RIDGE,bd=15)
        Frame2.place(x=665,y=80,width=915,height=540)

        Label1_Heading=Label(Frame2,text='Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
        Label1_Heading.pack(fill=X)

        #Treeview Model
        scroll_x=ttk.Scrollbar(Frame2,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        Address_table=ttk.Treeview(Frame2,height=540)
        Address_table['columns']=('ContactID','FirstName','LastName','Address','Gender','EmailAddress','ContactNo')

        Address_table.column('#0',width=0,stretch=NO)
        Address_table.column('ContactID',anchor='center',width=70)
        Address_table.column('FirstName',anchor='center',width=100)
        Address_table.column('LastName',anchor='center',width=100)
        Address_table.column('Address',anchor='center',width=130)
        Address_table.column('Gender',anchor='center',width=100)
        Address_table.column('EmailAddress',anchor='center',width=120)
        Address_table.column('ContactNo',anchor='e',width=120)

        Address_table.heading('ContactID',text='Contact_ID')
        Address_table.heading('FirstName',text='First Name')
        Address_table.heading('LastName',text='Last Name')
        Address_table.heading('Address',text='Address')
        Address_table.heading('Gender',text='Gender')
        Address_table.heading('EmailAddress',text='Email Address')
        Address_table.heading('ContactNo',text='Contact No')

        #Fetching data  from MySql database
        my_cursor.execute('SELECT * FROM Addresses')
        data=my_cursor.fetchall()
        #Displaying  Data fetched
        a=0
        for b in data:
           Address_table.insert('',a,text='',values=(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
           a=a+1

        Address_table.pack()

        #Buttons
        F3=Frame(new,bg=bg_color,relief=RIDGE,bd=15)
        F3.place(x=10,y=615,width=1570,height=100)

        btn1=Button(F3,text='Add Address',font='arial 20 bold',bg='#f9cedf',fg='black',width=20,command=add)
        btn1.grid(row=0,column=0,padx=85,pady=7)

        btn3=Button(F3,text='Reset',font='arial 20 bold',bg='#f9cedf',fg='black',width=20,command=reset)
        btn3.grid(row=0,column=1,padx=45,pady=7)

        btn4=Button(F3,text='Exit',font='arial 20 bold',bg='#f9cedf',fg='black',width=20,command=Exit1)
        btn4.grid(row=0,column=2,padx=45,pady=7)


        new.mainloop()

        #defining commands

   def _list():
        #============ View  List ===========#
        view=Tk()
        view.title('List of  Addresses')
        view.geometry('1580x740+0+0')
        view.iconbitmap('pic2-1.ico')
        bg_color='#8cbbf1'

        mydb=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='address_list',
            auth_plugin='mysql_native_password'
            )
        my_cursor=mydb.cursor()

        title=Label(view,text='List of Addresses',bg=bg_color,fg='black',font=('Cooper Std Black',35,'bold'),relief=GROOVE,bd=12)
        title.pack(fill=X)
        #Display Frame
        F1=Frame(view,bg=bg_color,relief=RIDGE,bd=15)
        F1.place(x=0,y=80,width=1020,height=540)
        #Frame  Heading
        lbl_t=Label(F1,text='Addresses',font=('arial', 20, 'bold'),fg='black',bd=7,relief=GROOVE)
        lbl_t.pack(fill=X)

        #TreeView  Model
        Address_table=ttk.Treeview(F1,height=540)
        Address_table['columns']=('ContactID','FirstName','LastName','Address','Gender','EmailAddress','ContactNo')

        Address_table.column('#0',width=0,stretch=NO)
        Address_table.column('ContactID',anchor='center',width=70)
        Address_table.column('FirstName',anchor='center',width=100)
        Address_table.column('LastName',anchor='center',width=100)
        Address_table.column('Address',anchor='center',width=130)
        Address_table.column('Gender',anchor='center',width=100)
        Address_table.column('EmailAddress',anchor='center',width=120)
        Address_table.column('ContactNo',anchor='e',width=120)


        Address_table.heading('ContactID',text='Contact_ID')
        Address_table.heading('FirstName',text='First Name')
        Address_table.heading('LastName',text='Last Name')
        Address_table.heading('Address',text='Address')
        Address_table.heading('Gender',text='Gender')
        Address_table.heading('EmailAddress',text='Email Address')
        Address_table.heading('ContactNo',text='Contact No')


        #Fetching data  from MySql database
        my_cursor.execute('SELECT * FROM Addresses')
        data=my_cursor.fetchall()
        #Displaying  Data fetched
        a=0
        for b in data:
           Address_table.insert('',a,text='',values=(b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
           a=a+1

        Address_table.pack()   

        #Right Frame(Update Details)
        F2=Frame(view,bg=bg_color,relief=RIDGE,bd=15)
        F2.place(x=1021,y=80,width=560,height=660)

        lbl_S=Label(F2,text='Update Contact',font=('arial', 20, 'bold'),fg='black',bd=7,relief=GROOVE)
        lbl_S.grid(row=0,column=0)

        First_Name_Label=Label(F2,text='First Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        First_Name_Label.grid(row=1,column=0,padx=10,pady=10)
        First_Name_Box=Entry(F2,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        First_Name_Box.grid(row=1,column=1,pady=10,sticky='w')

        Last_Name_Label=Label(F2,text='Last Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Last_Name_Label.grid(row=2,column=0,padx=10,pady=10)
        Last_Name_Box=Entry(F2,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Last_Name_Box.grid(row=2,column=1,pady=10,sticky='w')

        Address_Label=Label(F2,text='Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Address_Label.grid(row=3,column=0,padx=10,pady=10)
        Address_Box=Entry(F2,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Address_Box.grid(row=3,column=1,pady=10,sticky='w')

        Gender_Label=Label(F2,text='Gender',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Gender_Label.grid(row=4,column=0,padx=10,pady=10)
        Gender_Box=ttk.Combobox(F2,font=('times new rommon',18,'bold'),state='readonly')
        Gender_Box['values']=('Select Gender','Male','Female','Others')
        Gender_Box.grid(row=4,column=1,pady=10,sticky='w')
        Gender_Box.current(0)

        Email_Address_Label=Label(F2,text='Email Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Email_Address_Label.grid(row=5,column=0,padx=10,pady=10)
        Email_Address_Box=Entry(F2, font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Email_Address_Box.grid(row=5,column=1,pady=10)

        Contact_No_Label=Label(F2,text='Contact No.',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
        Contact_No_Label.grid(row=6,column=0,padx=10,pady=10)
        Contact_No_Box=Entry(F2,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7)
        Contact_No_Box.grid(row=6,column=1,pady=10,sticky='w')



        #Buttons Frame
        F3=Frame(view,bg=bg_color,relief=RIDGE,bd=15)
        F3.place(x=0,y=615,width=1020,height=125)

        #Defining  Commands
        def Update_Contact():
            Update_win=Tk()
            Update_win.title('Update Contacts')
            Update_win.geometry('500x200+150+150')
            Update_win.iconbitmap('pic2-1.ico')
            Update_win.configure(bg='pink')
            Label1=Label(Update_win,text='Enter Contact ID',font='arial 15',bg='pink',fg='white',padx=25,pady=30)
            Label1.grid(row=1,column=1)
            global Entry_box1
            Entry_box1=Entry(Update_win,font=('times new rommon',12))
            Entry_box1.grid(row=1,column=2)
            def update():
                if Entry_box1.get()=='':
                    messagebox.showerror('Update Status','ID is compulsory for updating contact')
                else:
                    comm='SELECT * from Addresses where Contact_ID=%s'
                    global v
                    v=[Entry_box1.get(),]
                    my_cursor.execute(comm,v)
                    details=my_cursor.fetchall()
                    First_Name_Box.insert(0,details[0][1])
                    Last_Name_Box.insert(0,details[0][2])
                    Address_Box.insert(0,details[0][3])
                    if details[0][4]=='Male':
                      Gender_Box.current(1)
                    elif details[0][4]=='Female':
                      Gender_Box.current(2)
                    elif details[0][4]=='Others':
                      Gender_Box.current(3)
                    else:
                      Gender_Box.current(0)
                    Email_Address_Box.insert(0,details[0][5])
                    Contact_No_Box.insert(0,details[0][6])
                     
            Button_upd=Button(Update_win,text='Update',font='arial 12 bold',bg='#8cbbf1',fg='black',width=20,command=update)
            Button_upd.grid(row=2,column=2,padx=25,pady=7)
           
        def Delete_Contact():
            Delete_win=Tk()
            Delete_win.title('Delete Addresses')
            Delete_win.geometry('500x200+150+150')
            Delete_win.iconbitmap('pic2-1.ico')
            Delete_win.configure(bg='pink')
            Label2=Label(Delete_win,text='Enter Contact ID',font='arial 15',bg='pink',fg='white',padx=25,pady=30)
            Label2.grid(row=1,column=1)
            Entry_box2=Entry(Delete_win,font=('times new rommon',12))
            Entry_box2.grid(row=1,column=2)
            def delete():
                if Entry_box2.get()=='':
                    messagebox.showerror('Delete Status','ID is compulsory for deleting contact')
                else:    
                    if messagebox.askyesno('Delete Contact','Do you want to Delete the contact'):
                        com='delete from Addresses where Contact_ID=%s'
                        l=(Entry_box2.get(),)
                        my_cursor.execute(com,l)
                        mydb.commit()
                        Entry_box2.delete(0,END)
                        messagebox.showinfo('Delete Status','Contact Deleted Successfully')
                        Delete_win.destroy()
            Button_del=Button(Delete_win,text='Delete',font='arial 12 bold',bg='#8cbbf1',fg='black',width=20,command=delete)
            Button_del.grid(row=2,column=2,padx=25,pady=7)
                   
        def Final_Update():
            
            FirstNameBox=First_Name_Box.get()
            LastNameBox=Last_Name_Box.get()
            AddressBox=Address_Box.get()
            GenderBox=Gender_Box.get()
            EmailAddressBox=Email_Address_Box.get()
            ContactNoBox=Contact_No_Box.get()
 

            id_contact=v[0]
            print(id_contact)
            query=("UPDATE Addresses set First_Name='"+FirstNameBox+"',Last_Name='"+LastNameBox+"',Address='"+AddressBox+"',Gender='"+GenderBox+"',Email_Address='"+EmailAddressBox+"',Contact_No='"+ ContactNoBox +"' WHERE Contact_ID='"+id_contact+"'")
            my_cursor.execute(query)
            mydb.commit()
            First_Name_Box.delete(0,END)
            Last_Name_Box.delete(0,END)
            Address_Box.delete(0,END)
            Gender_Box.delete(0,END)
            Email_Address_Box.delete(0,END)
            Contact_No_Box.delete(0,END)

            messagebox.showinfo('Update Status','Contact Updated Successfully')
            
            
            
            
        def Exit2():
            k= messagebox.askyesno('Exit','Do you want to exit?')
            if k>0:
                view.destroy()   

            
        #Creating Buttons
        btn1=Button(F3,text='Update Contact',font='arial 20 bold',bg='#f9cedf',fg='black',width=15,command=Update_Contact)
        btn1.grid(row=1,column=1,padx=25,pady=15)

        btn2=Button(F3,text='Delete Contact',font='arial 20 bold',bg='#f9cedf',fg='black',width=15,command=Delete_Contact)
        btn2.grid(row=1,column=2,padx=25,pady=15)

        btn3=Button(F3,text='Exit',font='arial 20 bold',bg='#f9cedf',fg='black',width=15,command=Exit2)
        btn3.grid(row=1,column=3,padx=25,pady=15)

        btn4=Button(F2,text='Update',font='arial 20 italic bold',bg='#f9cedf',fg='black',width=10,command=Final_Update)
        btn4.grid(row=8,column=1,pady=15)

        view.mainloop()


   def Exit():
         m= messagebox.askyesno('Exit','Do you want to exit')
         if m>0:
                root.destroy()   

   #adding buttons
   new_address=ImageTk.PhotoImage(file='new_address.jpg')
   new_address_button=Button(root,image=new_address,command=add_new)
   new_address_button.place(x=480,y=350)
   label_n=Label(root,text='(Add new Address)',font=('times new roman',15,'bold'),fg='white',bg='light blue')
   label_n.place(x=480,y=580)              

   view_list=ImageTk.PhotoImage(file='view_list.jpg')
   view_list_button=Button(root,image=view_list,command=_list)
   view_list_button.place(x=900,y=350)
   label_v1=Label(root,text='(View List,Edit Addresses',font=('times new roman',15,'bold'),fg='white',bg='light blue')
   label_v1.place(x=900,y=580)
   label_v1=Label(root,text='Delete Addresses)',font=('times new roman',15,'bold'),fg='white',bg='light blue')
   label_v1.place(x=900,y=610) 

   

   exitbutton=ImageTk.PhotoImage(Image.open('exit_button.jpg'))
   exit_button=Button(root,image=exitbutton,command=Exit,bg='#f9cedf',borderwidth=0)
   exit_button.place(x=1500,y=10)
   
   root.mainloop()

   
splash_win.after(4000, mainWin)

mainloop()
