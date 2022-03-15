from logging import root
import tkinter
from tkinter import *
from tkinter import messagebox


# ...............................login.....................................

def login():
    root=Toplevel(screen)
    root.title("Email Login")
    root.geometry('600x800')
    
    
    # label1=Label(root,text="Login to Account",fg='#ff9912' , width='20',font=('bold',20))
    # label1.pack(pady=50)
    
    bordcolr=LabelFrame(root,bg='black',width=500,height=300)
    bordcolr.pack()
    
    border=LabelFrame(bordcolr,text="login",bg='darkorchid',width=500,height=300)
    border.pack(padx=20,pady=20)

    label2=Label(border,text="mail_id/phone_no ",width='15',font=('TimesNew Roman',10),bg='slateblue')
    label2.place(x=100,y=110)
    entry1=Entry(border,width='30')
    entry1.place(x=250,y=110)

    label3=Label(border,text="password ",width='15',font=('TimesNew Roman',10),bg='slateblue')
    label3.place(x=100,y=160)
    entry2=Entry(border,width='30',show="*")
    entry2.place(x=250,y=160)
   
    
    def log():
        if entry1.get()!="" or entry2.get()!="":
            messagebox.showinfo("signup successfully")
        else:
            messagebox.showinfo("please type username,password")
            
    button1=Button(border,text='login',width='15',bg='darkslategray',font=('TimesNew Roman',10),command=log)
    button1.place(x=200,y=200)       
    
    
    root.mainloop()
    
# ..................................registr......................
def register():
    reg=Toplevel(screen)
    reg.geometry('800x900')
    reg.title("Register")
    
    borcolr=LabelFrame(reg,bg='black',width=500,height=600)
    borcolr.pack()
    
    borde=LabelFrame(borcolr,text="Register",bg='saddlebrown',width=500,height=500)
    borde.pack(padx=20,pady=20)
    
    label2=Label(borde,text="First_Name ",width='15',font=('TimesNew Roman',10),bg='pink')
    label2.place(x=100,y=50)
    entry1=Entry(borde,width='30')
    entry1.place(x=250,y=50)
    
    label3=Label(borde,text="Last_Name",width='15',font=('TimesNew Roman',10),bg='pink')
    label3.place(x=100,y=100)
    entry2=Entry(borde,width='30')
    entry2.place(x=250,y=100)
    
    label4=Label(borde,text="Age",width='15',font=('TimesNew Roman',10),bg='pink')
    label4.place(x=100,y=150)
    entry3=Entry(borde,width='30')
    entry3.place(x=250,y=150)
    
    label=Label(borde,text="Gender",width='15',font=('TimesNew Roman',10),bg='pink')
    label.place(x=100,y=200)
    rb1=Radiobutton(borde,text='male',variable='var',value=1,command='sel',bg='lavender')
    rb1.place(x=250,y=200)
    rb2=Radiobutton(borde,text='female',variable='var',value=2,command='sel',bg='lavender')
    rb2.place(x=320,y=200)
    
            
    
    
    
    def r(): 
        re=Toplevel(reg)
        re.geometry('800x900')
        re.title("user")
    
        bor=LabelFrame(re,bg='black',width=500,height=600)
        bor.pack()
    
        bord=LabelFrame(bor,text="Register",bg='goldenrod',width=500,height=500)
        bord.pack(padx=20,pady=20)
        
        lab=Label(bord,text='userid',width=15,font=('TimesNew Roman',10),bg='green')
        lab.place(x=100,y=100)
        entr=Entry(bord,width='30')
        entr.place(x=250,y=100)
        
        label5=Label(bord,text="Password",width='15',font=('TimesNew Roman',10),bg='green')
        label5.place(x=100,y=150)
        entry4=Entry(bord,width='30',show="*")
        entry4.place(x=250,y=150)
    
        label6=Label(bord,text="Confirm_Password",width='15',font=('TimesNew Roman',10),bg='green')
        label6.place(x=100,y=200)
        entry5=Entry(bord,width='30',show="*")
        entry5.place(x=250,y=200)
        
        def s():
            if entr.get()!="" or entry4.get()!="" or entry5.get()!="":
                if entry4.get() == entry5.get():
                    messagebox.showinfo("Successfully registered")
                else:
                    messagebox.showinfo("password are incorrect")
            else:
                messagebox.showinfo("fill the fields properly")
                
        
        button=Button(bord,text='Register',width='15',bg='olive',font=('TimesNew Roman',10),command=s) 
        button.place(x=180,y=300)
        
    
    button=Button(borde,text='Register',width='15',bg='darkred',font=('TimesNew Roman',10),command=r)
    button.place(x=180,y=300)
    
    
    
    
    reg.mainloop()
    

# ..........................window page.....................................

screen=Tk()
screen.geometry('500x400')
screen.title("Home Page")

# Wlab=Label(screen,text="Email Home",width='25',bg='gray',font=('BookmanOld Style',15))
# Wlab.pack(pady=150)

bor=LabelFrame(screen,bg='black',width=500,height=600)
bor.pack()
    
bord=LabelFrame(bor,text="Mail Home",bg='teal',width=300,height=300)
bord.pack(padx=20,pady=20)



wb1=Button(bord,text="Login",width='15',height='1', bg='gray',font=('BookmanOld Style',15),command=login)
wb1.place(x=60,y=100)
wb2=Button(bord,text="Register",width='15',height='1', bg='gray',font=('BookmanOld Style',15),command=register)
wb2.place(x=60,y=150)



screen.mainloop()


