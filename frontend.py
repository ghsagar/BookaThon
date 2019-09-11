from tkinter import *
#CONNECTING BACKEND AND RELATED FUNCTIONS
#TO VIEW ALL OF THE ITEMS




import backend

selected_tup = None

def get_entire_row(event):
        try:
                global selected_tup
                index=listbox1.curselection()[0]
                selected_tup=listbox1.get(index)
                
                e1.delete(0,END)
                e1.insert(END,selected_tup[1])
                e2.delete(0,END)
                e2.insert(END,selected_tup[2])
                e3.delete(0,END)
                e3.insert(END,selected_tup[3])
                e4.delete(0,END)
                e4.insert(END,selected_tup[4])
        except IndexError:
                pass


def delete_command():
        backend.delete_data(selected_tup[0])
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

def listview():
    listbox1.delete(0,END)
    for rows in backend.view_data():
        listbox1.insert(END,rows)

def searchitem():
    listbox1.delete(0, END)
    for rows in backend.search_data(IsbnText.get()):
        listbox1.insert(END, rows)

def insertdata():
    backend.insert_data(TitleText.get(),AuthorText.get(),YearText.get(),IsbnText.get())
    listbox1.delete(0,END)
    listbox1.insert(END,(TitleText.get(),AuthorText.get(),YearText.get(),IsbnText.get()))  


def update_command():
        try:
                backend.update_data(selected_tup[0],TitleText.get(),AuthorText.get(),YearText.get(),IsbnText.get())
        except:
                pass

         


window=Tk()
window.title("BookaD")

#We are Creating four Label, four Entry, one LisBox, scroll widget, and related Labels
# creating four Label
l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
# CREATING FOUR ENTRIES
TitleText=StringVar()
e1=Entry(window,textvariable=TitleText)
e1.grid(row=0,column=1)
AuthorText=StringVar()
e2=Entry(window,textvariable=AuthorText)
e2.grid(row=0,column=3)
YearText=IntVar()
e3=Entry(window,textvariable=YearText)
e3.grid(row=1,column=1)
IsbnText=IntVar()
e4=Entry(window,textvariable=IsbnText)
e4.grid(row=1,column=3)
#CREATING LISTBOX 
listbox1=Listbox(window, height=6,width=25)
listbox1.grid(row=2,column=0, rowspan=6,columnspan=2)
 

# SCROLL WIDGET CONNECTING LISTBOX
scroll1=Scrollbar()
scroll1.grid(row=2,column=2, rowspan=6)
listbox1.configure(yscrollcommand=scroll1.set)

scroll1.configure(command=listbox1.yview)
listbox1.bind("<<ListboxSelect>>",get_entire_row)
#CREATING SIX DIFFERENT ButtonS
b1=Button(window,text="View all",width=12, command=listview)
b1.grid(row=2, column=3)
b2=Button(window,text="Search Entry" , width=12, command=searchitem)
b2.grid(row=3, column=3)
b3=Button(window,text="Add Entry",width=12,command=insertdata)
b3.grid(row=4, column=3)
b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5, column=3)
b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6, column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)

b6.grid(row=7, column=3)

#END OF FRONT END

window.mainloop()
