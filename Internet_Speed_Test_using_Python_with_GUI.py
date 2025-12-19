from tkinter import *
import speedtest

def Speed_Check():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down= str(round(sp.download()/(10**6),3)) + " Mbps"
    up= str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    

SP=Tk()

SP.title("Internet Speed Test")
SP.geometry("500x650")
SP.config(bg="Blue")

lab=Label(SP,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="Black",fg="White")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(SP,text="Download Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(SP,text="00",font=("Time New Roman",30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(SP,text="Upload Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up=Label(SP,text="00",font=("Time New Roman",30,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)

button=Button(SP,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=Speed_Check)
button.place(x=60,y=460,height=50,width=380)


SP.mainloop()