from tkinter import*

root=Tk()
root.title('login page')
root.geometry('1000x600')
root.configure(bg='white')

def submit():
    uname=uname_entry.get('0.1',END).strip()
    pword=pword_entry.get('0.1',END).strip()
    if uname=="admin"and pword=='admin':
        root2=Tk()
        root2.title('feed')
        root2.geometry('1000x700')
    else:
        
        msg=Label(frame,bg='white',fg='red',text='Check your Username or Password')
        msg.place(x=75,y=250)

frame=Frame(root,width=350,height=430,border=1,bg='white',relief='solid')
frame.place(x=720,y=85)
head=Label(frame,text="Instagram",font=('times new roman',30,'normal'),bg='white')
head.place(x=85,y=20)

or_lb=Label(frame,text='---or---',bg='white',fg='gray80',font=('standard',10,'normal'))
or_lb.place(x=150,y=280)

fb_lb=Label(frame,text="Log in with Facebook",fg='royalblue',bg='white',font=('standard',10,'bold'))
fb_lb.place(x=100,y=320)

fp_lb=Label(frame,text="Forgot Password?",bg='white',fg='gray40')
fp_lb.place(x=120,y=370)

uname_label=Label(frame,text='username',bg='white',fg='gray50')
uname_label.place(x=33,y=85)

uname_entry=Text(frame,width=34,height=2,relief='flat',bg='gray95')

uname_entry.place(x=35,y=105)

pword_label=Label(frame,text='password',bg='white',fg='gray50')
pword_label.place(x=33,y=140)

pword_entry=Text(frame,relief='flat',width=34,height=2,bg='gray95')

pword_entry.place(x=35,y=160 )

btn=Button(frame,text='Log in',font=('Helvetica',10,'bold'),bg='deepskyblue2',fg='white',width=33,command=submit,relief='flat')
btn.place(x=36,y=210)

frame2=Frame(root,width=350,height=60,border=1,bg='white',relief='solid')
frame2.place(x=720,y=520)

sigin=Label(frame2,text="Don't have an account?",font=('Helvetica',10,'normal'),bg='white')
sigin.place(x=78,y=16)



sigin_btn=Button(frame2,text='Sign up',fg='royalblue',bg='white',relief='flat',font=('Helvetica',10,'bold'))
sigin_btn.place(x=215,y=13)

img_path=PhotoImage(file='c:/Users/Admin/Pictures/Screenshots/Screenshot (151).png')
img=Label(root,image=img_path,width=377,height=585)
img.place(y=60,x=300)
root.mainloop()
