from tkinter import *
import ttkbootstrap as tb
import os
from PIL import ImageTk,Image
import json

#This Scaling function helps handling scale of the windows across different resolutions

def s(x):
    global scalparam    
    return int(x*scalparam)

#foc_in is for focus in foc_out is for focus out
#ur is for username and pw is for password

def foc_in_ur(e):
   if(usrname_box.get().strip()=="" or usrname_box.get()=="Username"):
    usrname_box.delete(0,"end")

def foc_in_pw(e):
   if((pw_box.get().strip()!="")):
    pw_text.set(pw_box.get().strip())


def foc_ot_ur(e):
   if(usrname_box.get()==""):
      usrname_text.set("Username")

   print(usrname_box.get()=="",usrname_box.get())  

def foc_ot_pw(e):
   if(pw_box.get().strip()!=""):
    pw_box.delete(0,"end")   
    pw_box.config(show="*")
   

#Function to validate credentials

def signcheck():
   global username
   global password
   
   if((usrname_box.get().strip())==username and (pw_box.get()).strip()==password):
      pop=Toplevel(root)
      pop.geometry("500x200")
      label=Label(pop,image=imgab)
      label.place(relx=0)
      pop.title('Login Succeeded')
      lab=tb.Label(pop,text="Login Succeded",bootstyle="success",font=("Helvetica",20))
      lab.place(relx=0.4,rely=0.3)   
      pop.after(1500,lambda:pop.destroy())
   else:
      pop=Toplevel(root)
      pop.geometry("500x200")
      label=Label(pop,image=imgbc)
      label.place(relx=0)
      pop.title('Login Failed')
      lab=tb.Label(pop,text="Try Again",bootstyle="danger",font=("Helvetica",20))
      lab.place(relx=0.4,rely=0.3)
      pop.eval('tk::PlaceWindow . center')   
      pop.after(1400,lambda:pop.destroy())
      

#loading the credentials

f=open('credentials.json')
data=json.load(f)
username=data['username']
password=data['password']


#Initializing the Window


root=tb.Window(themename="sandstone")
screen_height = root.winfo_screenheight()
scalparam=(screen_height/1080)
root.geometry("1920x1080")
root.title('Login Screen')

p=(os.path.join(os.getcwd(),))+'/assets'

#place your own logo png here to use it


#root.iconbitmap(os.path.join(os.getcwd(),'logo.png'))

#heading place
heading=tb.Label(master=root,text="Login Portal by Subrahmanyam B H V S P",font=("segoe",s(25)),bootstyle='primary')
heading.place(relx=0.1,rely=0.05)

#opening popup images
tick=Image.open(os.path.join(p,"tick.png")).resize((int(462*scalparam*0.3),(int(417*scalparam*0.3))))
imgab=ImageTk.PhotoImage(tick)
cross=Image.open(os.path.join(p,"cross.png")).resize((int(435*scalparam*0.32),(int(441*scalparam*0.32))))
imgbc=ImageTk.PhotoImage(cross)


#side image
#replace this with your own custom image

side_image=Image.open(os.path.join(p,"replace_this.png")).resize((int(1125*scalparam),(int(1500*scalparam))))
img=ImageTk.PhotoImage(side_image)
label=Label(root,image=img)
label.place(relx=0.61)


#operator login text

heading=tb.Label(master=root,text="Operator Login",font=("segoe",s(20)),bootstyle='primary, inverse')
heading.place(relx=0.25,rely=0.33)

#username bar creation
usrname_text=StringVar()
usrname_box=tb.Entry(text="Username",bootstyle="primary",textvariable=usrname_text,width=15,justify=CENTER,font=('Helvetica',15)
                     ,foreground='Purple')
usrname_box.place(relx=0.27,rely=0.45)
usrname_text.set("Username")
flag1=False
usrname_box.bind("<FocusIn>", foc_in_ur)
usrname_box.bind("<FocusOut>", foc_ot_ur)

#usr image place

user_icon=Image.open(os.path.join(p,"u.png")).resize((int(512*(0.11*scalparam)),(int(512*(0.11*scalparam)))))
img2=ImageTk.PhotoImage(user_icon)
label=Label(root,image=img2)
label.place(relx=0.23,rely=0.44)

#password bar creation
pw_text=StringVar()
pw_box=tb.Entry(bootstyle="primary",textvariable=pw_text,width=15,justify=CENTER,font=('Helvetica',15),foreground='Purple')
pw_box.place(relx=0.27,rely=0.53)
pw_text.set("Password")
pw_box.bind("<FocusIn>",foc_in_pw)
usrname_box.bind("<FocusOut>", foc_ot_pw)

#pw image place
lock_icon=Image.open(os.path.join(p,"p.png")).resize((int(512*(0.111*scalparam)),(int(512*(0.111*scalparam)))))
img3=ImageTk.PhotoImage(lock_icon)
label2=Label(root,image=img3)
label2.place(relx=0.23,rely=0.515)

#login button
my_style=tb.Style()
my_style.configure('success.Outline.TButton',font=('Helvetica',15),bootstyle="success, outline")

log_but=tb.Button(style='success.Outline.TButton',text="Sign in",width=s(10),command=signcheck)
log_but.place(relx=0.28,rely=0.6)


if __name__=='__main__':

    root.mainloop()









#info_frame.pack()












