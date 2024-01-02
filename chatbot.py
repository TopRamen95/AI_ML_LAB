from tkinter import *
from datetime import date
import time
root = Tk()

def send():
    send ="you:"+a.get()
    text.insert('end',"\n"+send)
    if(a.get().lower() == 'hi'):
        text.insert('end','\n'+"Robot:HELLO")
    elif(a.get().lower() == 'hey'):
        text.insert('end','\n'+"Robot:HOW MAY I HELP YOU?")
    elif(a.get().lower() == 'hello'):
        text.insert('end','\n'+"Robot:HI!")
    elif(a.get().lower() == 'how are you?'):
        text.insert('end','\n'+"Robot:I AM FINE. HOW ARE YOU?")
    elif(a.get().lower() == 'i am fine'):
        text.insert('end','\n'+"Robot:NICE TO HEAR THAT")
    elif(a.get().lower() == 'how is your day?'):
        text.insert('end','\n'+"Robot:GOOD")
    elif(a.get().lower() == 'how can you help me?'):
        text.insert('end','\n'+"Robot:WHAT HELP DO YOU NEED?")
    elif(a.get().lower() == 'what is your name?'):
        text.insert('end','\n'+"Robot:MY NAME IS CHATBOTMAN")
    elif(a.get().lower() == 'are you a human?'):
        text.insert('end','\n'+"Robot:NO, I AM A ROBOT.")
    elif(a.get().lower() == "what is today's date?"):
        text.insert('end','\n'+"Robot:" + str(date.today()))
    elif(a.get().lower() == "what is the time now?"):
        text.insert('end','\n'+"Robot:"+str(time.strftime("%I:%M:%S %p")))
    else:
        text.insert('end','\n'+"Robot:I DIDN'T GET YOU.")
       
root.title("CHATBOTMAN")
text = Text(bg="violet")
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
Send=Button(root,bg="maroon",text="send",width=20,command=send)
Send.grid(row=1,column=1)
a.grid(row=1,column=0)
root.mainloop()
