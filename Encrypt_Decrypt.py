from tkinter import*
from tkinter import messagebox
import base64


root=Tk()
root.title("Encryption and Decryption")
Canvas=Canvas(root)
root.geometry("1000x1000")
root.maxsize(width=1000,height=1000)
root.minsize(width=1000,height=1000)
root.configure(bg="grey")

def encrypt():
    password=code.get()
    if password=="1234": 
        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64encode(encode_message)
        encrypt = base64_byte.decode("ascii") 
        text2.insert(END,encrypt)
    
    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key") 
    elif(password!="1234"):
        messagebox.showerror("Oops","Invalid secret Key")
        
def decrypt():
    password=code.get()
    if password=="1234": 
        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64decode(encode_message)
        encrypt = base64_byte.decode("ascii") 
        text3.insert(END,encrypt)
        
    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key") 
    elif(password!="1234"):
        messagebox.showerror("Oops","Invalid secret Key") 
         
def reset():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    text3.delete(1.0,END)
    code.set("")

##label
Label(root,text=" Enter the text for encryption and decryption",bg="yellow", font="impact 16 ").place(x=20 , y= 6)

##TEXT
text1 = Text(root,font='20')
text1.place(x=10,y=45,width=400,height=120)

text2 = Text(root,font='20',bd=4,wrap=WORD)
text2.place(x=550,y=45,width=400,height=120)
# text2.insert(END,encrypt)

text3 = Text(root,font='20',bd=4,wrap=WORD)
text3.place(x=550,y=250,width=400,height=120)
## label
Label(root,text="Enter Secret Key " , font="impact 13").place(x=150,y=185)

label1=Label(root,text="Text is Encrypted",font="impact 16",bg="red")
label1.place(x=670, y=6)

label2=Label(root,text="Text is Decrypted",font="impact 16",bg="green")
label2.place(x=670, y=200)

label3 = Label( root , text="Developed by Rohit Sahni",font="impact 16",fg="red",bd=4)
label3.place(x=400,y=600)

code = StringVar()
##ENTRY
Entry(root, textvariable=code,bd=4,font="20",show="*").place(x=95,y=220)

## Button 
         
Button(root,text="ENCRYPT",font="arial 15 bold",bg="red",fg="black",bd="5", command=encrypt).place(x=15,y=280,width=180)
        
Button(root,text="DECRYPT",font="arial 15 bold",bg="green",fg="black",bd="5",command=decrypt).place(x=220,y=280,width=180)

Button(root,text="RESET",font="arial 15 bold",bg="blue",fg="black",bd="5", command=reset).place(x=60,y=350,width=280)

mainloop()
