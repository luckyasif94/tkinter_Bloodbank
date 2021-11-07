from tkinter import *
import mysql.connector

def regSql(): #registration submit button sql operation
    name_var = name_txt.get()
    age_var = age_txt.get()
    sex_var = sex_txt.get()
    phone_var = phone_txt.get()
    bgroup_var = bgroup_txt.get()

    myconn = mysql.connector.connect(host='localhost', user='root', password='', database='bloodbank')
    cur = myconn.cursor()
    query = "Insert into users (name,age,sex,phone,bgroup) values (%s,%s,%s,%s,%s)"
    values = [(name_var,age_var,sex_var,phone_var,bgroup_var)]
    cur.executemany(query, values)
    myconn.commit()
    myconn.close()
    new.destroy()

def newReport(): #Registration window
    global name_txt
    global age_txt
    global sex_txt
    global phone_txt
    global bgroup_txt
    global new

    new = Toplevel()
    new.geometry('500x500')
    new.title("New Report")

    name_label=Label(new,text="Enter Name",font=("bold",15)).grid(column=0,row=0)

    age_label = Label(new, text="Enter Age", font=("bold", 15)).grid(column=0, row=1)

    sex_label = Label(new, text="Enter Sex", font=("bold", 15)).grid(column=0, row=2)

    phone_label = Label(new, text="Enter Phone Number", font=("bold", 15)).grid(column=0, row=3)

    bgroup_label = Label(new, text="Enter Blood Group", font=("bold", 15)).grid(column=0, row=4)

    # entry1
    name_txt = Entry(new, width=40)
    name_txt.grid(column=1, row=0)

    # entry1
    age_txt = Entry(new, width=40)
    age_txt.grid(column=1, row=1)

    # entry1
    sex_txt = Entry(new, width=40)
    sex_txt.grid(column=1, row=2)

    # entry1
    phone_txt = Entry(new, width=40)
    phone_txt.grid(column=1, row=3)

    # entry1
    bgroup_txt = Entry(new, width=40)
    bgroup_txt.grid(column=1, row=4)

    submit_btn = Button(new,text="Submit",command=regSql).grid(column=1,row=5)

def viewAll(): #view all records in blood bank
    myconn = mysql.connector.connect(host='localhost', user='root', password='', database='bloodbank')
    cur = myconn.cursor()
    query = "Select * from users"
    cur.execute(query)
    data = cur.fetchall()
    myconn.close()

    allreport = Toplevel()
    allreport.geometry('500x500')
    allreport.title("View All Reports")

    for index, dat in enumerate(data):
        Label(allreport, text=dat[0]).grid(row=index + 1, column=1)
        Label(allreport, text=dat[1]).grid(row=index + 1, column=3)
        Label(allreport, text=dat[2]).grid(row=index + 1, column=5)
        Label(allreport, text=dat[3]).grid(row=index + 1, column=7)
        Label(allreport, text=dat[4]).grid(row=index + 1, column=9)
        Label(allreport, text=dat[5]).grid(row=index + 1, column=11)

def searchBSql(): #sql operation on searchblood group button
    blood = b_txt.get()

    myconn = mysql.connector.connect(host='localhost', user='root', password='', database='bloodbank')
    cur = myconn.cursor()
    query = "Select * from users where bgroup='%s'"
    cur.execute(query,blood)
    data = cur.fetchall()
    myconn.close()

    for index, dat in enumerate(data):
        Label(searchb, text=dat[0]).grid(row=index + 3, column=1)
        Label(searchb, text=dat[1]).grid(row=index + 3, column=3)
        Label(searchb, text=dat[2]).grid(row=index + 3, column=5)
        Label(searchb, text=dat[3]).grid(row=index + 3, column=7)
        Label(searchb, text=dat[4]).grid(row=index + 3, column=9)
        Label(searchb, text=dat[5]).grid(row=index + 3, column=11)

def searchBlood(): #Search using blood group
    searchb = Toplevel()
    searchb.geometry('500x500')
    searchb.title("Search with blood group")

    global b_txt

    Label(searchb, text="Enter Blood Group").grid(row=0, column=0)
    b_txt = Entry(searchb, width=40)
    b_txt.grid(column=1, row=0)
    searchb_btn = Button(searchb,text="Search",font=('Times', 15),command=searchBSql).grid(column=1,row=1)

def searchPSql(): #sql operation on search Phone number button
    phone = p_txt.get()

    myconn = mysql.connector.connect(host='localhost', user='root', password='', database='bloodbank')
    cur = myconn.cursor()
    query = "Select * from users where phone='%s'"
    cur.execute(query,phone)
    data = cur.fetchall()
    myconn.close()

    for index, dat in enumerate(data):
        Label(searchb, text=dat[0]).grid(row=index + 3, column=1)
        Label(searchb, text=dat[1]).grid(row=index + 3, column=3)
        Label(searchb, text=dat[2]).grid(row=index + 3, column=5)
        Label(searchb, text=dat[3]).grid(row=index + 3, column=7)
        Label(searchb, text=dat[4]).grid(row=index + 3, column=9)
        Label(searchb, text=dat[5]).grid(row=index + 3, column=11)

def searchPhone(): #Search using phone number
    global p_txt
    searchp = Toplevel()
    searchp.geometry('500x500')
    searchp.title("Search with phone number")

    Label(searchp, text="Enter Phone Number").grid(row=0, column=0)
    p_txt = Entry(searchp, width=40)
    p_txt.grid(column=1, row=0)
    searchb_btn = Button(searchp, text="Search", font=('Times', 15), command=searchPSql).grid(column=1, row=1)

#main window
window = Tk()
window.title("Blood Bank")
window.geometry('720x720')

welcome_label = Label(window,text="Welcome to Blood Group DataBase",font=('Times', 24))
welcome_label.grid(column=0,row=0)

new_report_btn = Button(window,text="Add New Report",font=('Times', 15),command=newReport).grid(column=0,row=1)

view_report_btn = Button(window,text="View All Reports",font=('Times', 15),command=viewAll).grid(column=0,row=2)

search_blood_btn = Button(window,text="Search Blood Group",font=('Times', 15),command=searchBlood).grid(column=0,row=3)

search_phone_btn = Button(window,text="Search With Phone Number",font=('Times', 15),command=searchPhone).grid(column=0,row=4)

window.mainloop()


