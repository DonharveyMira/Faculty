from tkinter import *
from tkinter.ttk import *
from tkinter import *
import os

root = Tk()
root.config(highlightthickness=0, background="#DFEEED")

window_width = 1250
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.overrideredirect(True)

sidebar_frame = Frame(root, bg="#FBF0D7")
sidebar_frame.place(relx=0, rely=0, relheight=1, relwidth=0.14)

# sidebar logo
cvsbrLogo = Canvas(root, width=100, height=80, highlightthickness=0) 
cvsbrLogo.pack()
imgsbrLogo = PhotoImage(file='images//sbrLogo.png')
cvsbrLogo.create_image(48, 44, image=imgsbrLogo, anchor=CENTER)
cvsbrLogo.configure(background='#FBF0D7')
cvsbrLogo.place(relx=0.03, rely=0.043)

# home icon/button
def homeBtn():
    root.withdraw() 
    os.system('python homepage.py')
    root.destroy() 

cvHomeIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvHomeIC.pack()
imgHome = PhotoImage(file='images//home.png')
cvHomeIC.create_image(25, 25, image=imgHome, anchor=CENTER)
cvHomeIC.configure(background='#FBF0D7')
cvHomeIC.place(relx=0.0069, rely=0.17)

home_label = Label(root, text="Home", bg="#FBF0D7", fg="#497687")
home_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
home_label.place(relx=0.065, rely=0.2, anchor=CENTER)
home_label.bind("<Button-1>", lambda event: homeBtn())

# patient icon/button
cvPtntIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvPtntIC.pack()
imgPtnt = PhotoImage(file='images//patient2.png')
cvPtntIC.create_image(25, 25, image=imgPtnt, anchor=CENTER)
cvPtntIC.configure(background='#FBF0D7')
cvPtntIC.place(relx=0.0069, rely=0.27)

patient_label = Label(root, text="Patient", bg="#FBF0D7", fg="#1E3037")
patient_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
patient_label.place(relx=0.065, rely=0.3, anchor=CENTER)

# staff icon/button
def staffBtn():
    root.withdraw() 
    os.system('python staff.py')
    root.destroy() 

cvStaffIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvStaffIC.pack()
imgStaff = PhotoImage(file='images//staff.png')
cvStaffIC.create_image(25, 25, image=imgStaff, anchor=CENTER)
cvStaffIC.configure(background='#FBF0D7')
cvStaffIC.place(relx=0.0069, rely=0.37)

staff_label = Label(root, text="Staff", bg="#FBF0D7", fg="#497687")
staff_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
staff_label.place(relx=0.057, rely=0.4, anchor=CENTER)
staff_label.bind("<Button-1>", lambda event: staffBtn())

# inventory icon/button
def invBtn():
    root.withdraw() 
    os.system('python inventory.py')
    root.destroy() 

cvinventoryIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvinventoryIC.pack()
imgInv = PhotoImage(file='images//inventory.png')
cvinventoryIC.create_image(25, 25, image=imgInv, anchor=CENTER)
cvinventoryIC.configure(background='#FBF0D7') 
cvinventoryIC.place(relx=0.007, rely=0.47)

inventory_label = Label(root, text="Inventory", bg="#FBF0D7", fg="#497687")
inventory_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
inventory_label.place(relx=0.078, rely=0.5, anchor=CENTER)
inventory_label.bind("<Button-1>", lambda event: invBtn())

# logout icon/button
def logoutBtn():
    root.withdraw() 
    os.system('python login_admin.py')
    root.destroy() 

cvLogoutIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvLogoutIC.pack()
imgLogout = PhotoImage(file='images//logout.png')
cvLogoutIC.create_image(25, 25, image=imgLogout, anchor=CENTER)
cvLogoutIC.configure(background='#FBF0D7') 
cvLogoutIC.place(relx=0.009, rely=0.88)

logout_label = Label(root, text="Logout", bg="#FBF0D7", fg="#497687")
logout_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
logout_label.place(relx=0.065, rely=0.91, anchor=CENTER) 

logout_label.bind("<Button-1>", lambda event: logoutBtn())

#main code - homepage ---------------------

patientID = Label(root, text="Patient ID", bg="#DFEEED", fg="#497687")
patientID.config(font=("Microsoft JhengHei", 13, "bold"))
patientID.place(relx=0.2, rely=0.059, anchor=CENTER)

patientID_entry = Entry(root, bg="#FFFFFF", fg="#497687", width=29)
patientID_entry.config(font=("Microsoft JhengHei", 13),cursor="hand2")
patientID_entry.place(relx=0.395, rely=0.059, anchor=CENTER)

#Patient Record
ptntRec_panel = Frame(root, bg="#FBF0D7")
ptntRec_panel.place(x=210, y=72, width=450, height=350)

ptntRec = Label(ptntRec_panel, text="PATIENT RECORD", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
ptntRec.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

name_label = Label(ptntRec_panel, text="Name", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687")
name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
name_entry = Entry(ptntRec_panel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
name_entry.grid(row=1, column=1, padx=20, pady=10)

address_label = Label(ptntRec_panel, text="Address", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
address_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
address_entry = Entry(ptntRec_panel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
address_entry.grid(row=2, column=1, padx=20, pady=10)

birthday_label = Label(ptntRec_panel, text="Birthday", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
birthday_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
birthday_entry = Entry(ptntRec_panel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
birthday_entry.grid(row=3, column=1, padx=20, pady=10)

age_label = Label(ptntRec_panel, text="Age", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
age_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
age_entry = Entry(ptntRec_panel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
age_entry.grid(row=4, column=1, padx=20, pady=10)

phone_label = Label(ptntRec_panel, text="Contact #", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
phone_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
phone_entry = Entry(ptntRec_panel, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
phone_entry.grid(row=5, column=1, padx=1, pady=10)

marital_label = Label(ptntRec_panel, text="Marital", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
marital_label.grid(row=6, column=0, padx=20, pady=10, sticky="w")
marital_combobox = Combobox(ptntRec_panel, font=("Microsoft JhengHei", 11), 
                            values=["Single", "Married", "Divorced", "Separated", "Widowed"], width=30)
marital_combobox.grid(row=6, column=1, padx=1, pady=10)

#Physical Exam
physExam_panel = Frame(root, bg="#FBF0D7")
physExam_panel.place(x=210, y=443, width=450, height=240)

ptntRec = Label(physExam_panel, text="PHYSICAL EXAM", font=("Microsoft JhengHei", 14, "bold"), 
                bg="#FBF0D7", fg="#497687")
ptntRec.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

height_label = Label(physExam_panel, text="Height", font=("Microsoft JhengHei", 11, "bold"), 
                     bg="#FBF0D7", fg="#497687")
height_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
height_entry = Entry(physExam_panel, font=("Microsoft JhengHei", 11), fg="#497687")
height_entry.grid(row=1, column=1, padx=20, pady=10)
cm_label = Label(physExam_panel, text="cm", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#FBF0D7", fg="#497687")
cm_label.grid(row=1, column=2, padx=1, pady=10, sticky="w")

weight_label = Label(physExam_panel, text="Weight", font=("Microsoft JhengHei", 11, "bold"), 
                     bg="#FBF0D7", fg="#497687")
weight_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
weight_entry = Entry(physExam_panel, font=("Microsoft JhengHei", 11), fg="#497687")
weight_entry.grid(row=2, column=1, padx=20, pady=10)
kg_label = Label(physExam_panel, text="kg", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#FBF0D7", fg="#497687")
kg_label.grid(row=2, column=2, padx=1, pady=10, sticky="w")

pr_label = Label(physExam_panel, text="Pulse Rate", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#FBF0D7", fg="#497687")
pr_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
pr_entry = Entry(physExam_panel, font=("Microsoft JhengHei", 11), fg="#497687")
pr_entry.grid(row=3, column=1, padx=20, pady=10)
bpm_label = Label(physExam_panel, text="bpm", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
bpm_label.grid(row=3, column=2, padx=1, pady=10, sticky="w")

bt_label = Label(physExam_panel, text="Body Temperature", font=("Microsoft JhengHei", 11, "bold"), 
                 bg="#FBF0D7", fg="#497687")
bt_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
bt_entry = Entry(physExam_panel, font=("Microsoft JhengHei", 11), fg="#497687")
bt_entry.grid(row=4, column=1, padx=20, pady=10)
cel_label = Label(physExam_panel, text="°C", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
cel_label.grid(row=4, column=2, padx=1, pady=10, sticky="w")

def reset():
    patientID_entry.delete(0, END)
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    birthday_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    marital_combobox.set("")
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    pr_entry.delete(0, END)
    bt_entry.delete(0, END)

btnReset = Button(root, text="Reset", command=reset, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.19, rely=0.91, anchor=CENTER)

def new():
    #tempo-command
    patientID_entry.delete(0, END)
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    birthday_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    marital_combobox.set("")
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    pr_entry.delete(0, END)
    bt_entry.delete(0, END)

btnNew = Button(root, text="New", command=new, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.235, rely=0.91, anchor=CENTER)

def save():
    #tempo-command
    patientID_entry.delete(0, END)
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    birthday_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    marital_combobox.set("")
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    pr_entry.delete(0, END)
    bt_entry.delete(0, END)

btnSave = Button(root, text="Save", command=save, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.278, rely=0.91, anchor=CENTER)

def sensor():
    #tempo-command
    patientID_entry.delete(0, END)
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    birthday_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    marital_combobox.set("")
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    pr_entry.delete(0, END)
    bt_entry.delete(0, END)

btnSensor = Button(root, text="Sensors", command=sensor, 
                      bg="#b12a2a", fg="#ffffff")
btnSensor.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSensor.place(relx=0.5, rely=0.91, anchor=CENTER)

#Login - Save nurse info ------------
loginPanel = Frame(root, bg="#FBF0D7")
loginPanel.place(x=680, y=443, width=530, height=240)

login = Label(loginPanel, text="Login", font=("Microsoft JhengHei", 14, "bold"), 
              bg="#FBF0D7", fg="#497687")
login.place(relx=0.5, rely=0.1, anchor="center")

def login():
    username = loginName_entry.get()
    password = loginPass_entry.get()

    if username == "username" and password == "1234":
        message_label.config(text="Login successful!", fg="green")
    else:
        message_label.config(text="Login failed. Please try again.", fg="#b12a2a")

loginIC = Canvas(root, width=150, height=150, highlightthickness=0) 
loginIC.pack()
imgLogin = PhotoImage(file='images//shield.png')
loginIC.create_image(75, 75, image=imgLogin, anchor=CENTER)
loginIC.configure(background='#FBF0D7')
loginIC.place(relx=0.57, rely=0.63)

loginNameLabel = Label(loginPanel, text="Name", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
loginNameLabel.place(relx=0.35, rely=0.37)
loginName_entry = Entry(loginPanel, font=("Microsoft JhengHei", 11), fg="#497687", width=24)
loginName_entry.place(relx=0.50, rely=0.37)

loginPassLabel = Label(loginPanel, text="Password", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
loginPassLabel.place(relx=0.35, rely=0.60)
loginPass_entry = Entry(loginPanel, show="•", font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=19)
loginPass_entry.place(relx=0.50, rely=0.60)

def passVisibility():
    if loginPass_entry['show'] == '':
        loginPass_entry.configure(show='•')
        btnShow.configure(text='Show')
    else:
        loginPass_entry.configure(show='')
        btnShow.configure(text='Hide')

btnShow = Button(loginPanel, text='Show', command=passVisibility,
                              bg='#497687', fg='#ffffff')
btnShow.config(font=("Microsoft JhengHei", 8),cursor="hand2")
btnShow.place(relx=0.88, rely=0.649, anchor=CENTER)

message_label = Label(root, text="", bg="#FBF0D7")
message_label.config(font=("Microsoft JhengHei ", 11))
message_label.place(relx=0.84, rely=0.79, anchor=CENTER)

login_button = Button(root, text="Login", command=login, 
                      bg="#497687", fg="#ffffff")
login_button.config(font=("Microsoft JhengHei", 11), cursor="hand2")
login_button.place(relx=0.614, rely=0.91, anchor=CENTER)

def resetLogin():
    loginName_entry.delete(0, END)
    loginPass_entry.delete(0, END)

btnReset = Button(root, text="Reset", command=resetLogin, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.565, rely=0.91, anchor=CENTER)

#Exit Form
def exitForm():
    root.destroy() 

exitLogo = Canvas(root, width=30, height=30, highlightthickness=0) 
exitLogo.pack()
imgExitLogo = PhotoImage(file='images//exit.png')
exitLogo.create_image(15, 15, image=imgExitLogo, anchor=CENTER)
exitLogo.configure(background='#DFEEED', cursor="hand2")
exitLogo.place(relx=0.97, rely=0.009)
exitLogo.bind("<Button-1>", lambda event: exitForm())


root.mainloop()
