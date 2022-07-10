from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb 

#layout
root=Tk()
root.title("Steganography")
root.geometry("700x550+140+190")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select Image File',
                                        filetype=(("PNG file","*.png"),
                                                  ("JPG File","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    
def Hide():
    global secret
    message=txt1.get(1.0,END)
    secret = lsb.hide(str(filename), message)
    
def Show():
    clear_message = lsb.reveal(filename)
    txt1.delete(1.0,END)
    txt1.insert(END, clear_message)
    
def save():
    global secret
    secret.save("Hidden.png")


#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)


#logo
logo=PhotoImage(file="logo3.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=29)
Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font="arial 28 bold").place(x=150,y=30)


#frame
f=Frame(root,bd=3,bg="yellow",width=320,height=280,relief=GROOVE)
f.place(x=15,y=110)
lbl=Label(f,bg="yellow")
lbl.place(x=40,y=10)

#2nd frame
f1=Frame(root,bd=3,bg="white",width=320,height=280,relief=GROOVE)
f1.place(x=360,y=108)



#text in frame 2

txt1=Text(f1,font="arial 20 ",bg="white",fg="black",relief=GROOVE,wrap=WORD)
txt1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(f1)
scrollbar1.place(x=500,y=0,height=300)

scrollbar1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=scrollbar1.set)


#3rd frame

f3=Frame(root,bd=2,bg="#2f4155",width=330,height=90,relief=GROOVE)
f3.place(x=10,y=400)

Button(f3,text="OPEN IMAGE",width=10,height=1,font="arial 16 bold",command=showimage).place(x=20,y=30)
Button(f3,text="SAVE IMAGE",width=10,height=1,font="arial 16 bold",command=save).place(x=170,y=30)
Label(f3,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=25,y=5)

#4th

f4=Frame(root,bd=2,bg="#2f4155",width=330,height=90,relief=GROOVE)
f4.place(x=355,y=400)

Button(f4,text="HIDE DATA",width=10,height=1,font="arial 16 bold",command=Hide).place(x=20,y=30)
Button(f4,text="SHOW DATA",width=10,height=1,font="arial 16 bold",command=Show).place(x=170,y=30)
Label(f4,text="Picture,Image,Photo File",bg="#2f4155",fg="yellow").place(x=25,y=5)




root.mainloop()