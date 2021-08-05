from tkinter import *
import socket
from tkinter import messagebox
c_box=0
import pyperclip
#----------------------constants----------------------

#-------------------------Backend logic---------------------------------#
#Buttons calls action() when pressed
def action():
    val=None
    k=None
    global c_box
    if len(entry.get())==0:
        messagebox.showwarning(title="No entry", message="Please make sure you have entered the data")
        entry.focus()
    else:
        r_entry.delete(0,END)
        if radio_state.get() == 1:   #ip to host
            try:
                val=socket.gethostbyaddr(entry.get())
                k=val[0]
            except:
                messagebox.showwarning(title="Invalid Entry!",message="Please enter Valid IP Address")
            r_entry.insert(0,k)
        elif radio_state.get() == 2: #host to ip
            try:
                val=socket.gethostbyname(entry.get())
            except:
                messagebox.showwarning(title="Invalid Entry!",message="Please enter Valid Hostname")
            r_entry.insert(0,val)
        else:
            messagebox.showinfo(title="Option not selected", message="Please select the type of conversion you want \n IP to host\n Host to IP")
    checkbutton_used()
#-------------------test-------------------------

#----------------------UI setup--------------------------------


#Creating a new window and configurations
window = Tk()
window.title("NSLookup-The Som Edition:)")
window.minsize(width=200, height=200)
window.config(padx=30,pady=30)

#Labels
label1 = Label(text="Enter Ip/Hostname")
label1.grid(column=1,row=1)

label2 = Label(text="Your Ip/Hostname is ")
label2.grid(column=1,row=2)

#Entries
entry = Entry(width=30)
entry.insert(0,"Enter data here")
r_entry=Entry(width=30)
r_entry.grid(column=2,row=2)
r_entry.insert(0,"Result here")
#Courasor initial placement
entry.focus()
#Gets text in entry
print(entry.get())
entry.grid(column=2,row=1)

#Radiobutton
def radio_used():
    if radio_state.get()==1:
        _extracted_from_radio_used_3("Enter IP Address", "Hostname is:  ")
    if radio_state.get()==2:
        _extracted_from_radio_used_3("Enter Hostname", "The IP address is:  ")

def _extracted_from_radio_used_3(text, arg1):
    label1.config(text=text)
    label2.config(text=arg1)
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="IP to Host", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Host to IP", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=2,row=3)
radiobutton2.grid(column=3,row=3)


#Buttons
#calls action() when pressed
button = Button(text="Find", command=action)
button.grid(column=2,row=4)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
    if checked_state.get()==1:
        pyperclip.copy(r_entry.get())


#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checked_state.set(1)
checkbutton = Checkbutton(text="Copy to clipboard", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=3,row=4)




window.mainloop()