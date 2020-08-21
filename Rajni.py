from tkinter import messagebox
from threading import *
import sys
sys.path.append("/myModule/")
import myModule
from myModule.functions import *
from time import sleep

#tkinter
global b_enter

#variable for mail
info="I am from Assistant"
#Setting Notification
def f_setting():
    messagebox.showinfo("Setting","Sorry Sir This part is under development. It Will be Complete Soon")

#Function for Power button 
def f_on():    
    l_result["text"] =greetings()
    b_enter["state"]=tk.NORMAL
    e_entry["state"]=tk.NORMAL
    l_status1["text"]="On"
    b_power["image"],b_power["command"]=blue_button,f_off
    mic_test()
    speak(greetings())
def f_off():
    l_result["text"] =speak(bye())
    b_power["image"],b_power["command"]=red_button,f_on
    b_mic["state"]=tk.DISABLED
    b_enter["state"]=tk.DISABLED
    e_entry.delete(0,tk.END)
    e_entry["state"]=tk.DISABLED
    l_status1["text"]="Off"
    l_status2["text"]=""
    l_status3["text"]=""

#function for enter button
def f_get_msg():
    
    l_status3["text"]="Getting Mail id of Recipient.."
    global info
    info=e_entry.get()
    l_result["text"] = speak("Please, Enter Mail id of Recipient")
    b_enter["command"]=f_get_mail
    
def f_get_mail():
    global info
    to_id=e_entry.get()
    #sendEmail(to_id,info)
    l_result["text"] = speak(sendEmail(to_id,info))
    b_mic["state"]=tk.NORMAL
    b_enter["command"]=f_enter
    l_status3["text"]="Done,Waiting for next command"

def f_enter():
    l_status3["text"]="Processing..."
    mic_test()
    m=e_entry.get().upper()
    e_entry.delete(0,tk.END)
    if len(m)==0:
        l_result["text"] = speak("Plz sir! Enter Some Command")
        l_status3["text"]="Done, Waiting For next Command"
    elif "SEND" in m and "MAIL" in m:
        if is_net():
            l_result["text"] = speak("Enter Your Message")
            b_enter["command"]=f_get_msg
            l_status3["text"]="Getting message to Send..." 
            b_mic["state"]=tk.DISABLED
        else :
            l_result["text"] = speak("Check your Internet Connection")
    elif "EXIT" in m or "QUIT" in m:
        speak(bye())
        exit()     

    else:
        result=lines(m)
        l_result["text"]=speak(result)
        l_status3["text"]="Done, Waiting for next command"
        #e_entry.delete(0,tk.END)

# function for mic button
def f_mic():
    b_enter["state"]=tk.DISABLED
    if mic_test():
        l_status3["text"]="Listening..."
        m=speech_to_text()
        if m=="NoVoice":
            l_result["text"]=speak("Sorry Sir, I am unable to Recgnize You")
        else:
            e_entry.delete(0,tk.END)
            e_entry.insert(0,m)
            l_status3["text"]="Process Done,Waiting for next command"
    
    else :
        l_result["text"]="Plz Check Your Connection and Try Again"
        speak("Plz Check Your Connection and Try Again")
        l_status3["text"]="Process Done,Waiting for next command"
    b_enter["state"]=tk.NORMAL
    return





def mic_test():
    if is_net():
        b_mic["state"]=tk.NORMAL
        l_status2["text"]="Internet Connected"
        return True
    else :
        b_mic["state"]=tk.DISABLED
        l_status2["text"]="No Active Internet Connection"
        return False

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Your Assistant-Rajni")
    root.iconbitmap("images/ikon.ico")
    root.minsize(500,656)
    b_color="cyan"

    #Pic object and buttons
    pic=ImageTk.PhotoImage(Image.open("images/robot.png"))
    red_button=ImageTk.PhotoImage(Image.open("images/p_red.png"))
    blue_button=ImageTk.PhotoImage(Image.open("images/p_blue.png"))
    mic_button=ImageTk.PhotoImage(Image.open("images/mic.png"))
    enter_button=ImageTk.PhotoImage(Image.open("images/n.png"))
    setting_button=ImageTk.PhotoImage(Image.open("images/setting.png"))
    exit_button=ImageTk.PhotoImage(Image.open("images/redcross.png"))

    mainframe=tk.LabelFrame(root,bg=b_color)

    #frame 1
    f1=tk.LabelFrame(mainframe,borderwidth=0,bg=b_color)
    r_pic=tk.Label(f1,image=pic,bg=b_color)
    r_pic.pack()
    f1.pack()

    #frame 2
    f2=tk.LabelFrame(mainframe,borderwidth=0,bg=b_color)
    b_mic=tk.Button(f2,image=mic_button,pady=10,borderwidth=0,bg=b_color,activebackground=b_color,state=tk.DISABLED,command=f_mic)
    e_entry=tk.Entry(f2,font=("Calibri 15"),width=35,state=tk.DISABLED)
    b_enter=tk.Button(f2,image=enter_button,pady=10,borderwidth=0,bg=b_color,activebackground=b_color,state=tk.DISABLED,command=f_enter)
    b_mic.grid(row=0,column=1,pady=10)
    e_entry.grid(row=0,column=2,pady=10,sticky=tk.W)
    b_enter.grid(row=0,column=3,pady=10)
    f2.pack(pady=15)
    
    #frame 3
    f3=tk.LabelFrame(mainframe,borderwidth=0,bg=b_color)
    l_result=tk.Label(f3,width =50,font=("Calibri 15"),text="",pady=5,bg=b_color)
    l_result.pack()
    f3.pack(pady=15)
    
    #frame 4
    f4=tk.LabelFrame(mainframe,borderwidth=0,bg=b_color)
    b_setting=tk.Button(f4,image=setting_button,padx=5,pady=10,borderwidth=0,bg=b_color,activebackground=b_color,anchor=tk.W,command=f_setting)
    b_power=tk.Button(f4,image=red_button,padx=10,pady=5,borderwidth=0,bg=b_color,activebackground=b_color,command=f_on)
    b_quit=tk.Button(f4,image=exit_button,padx=10,pady=5,borderwidth=0,bg=b_color,activebackground=b_color,command=Thread(target=root.quit).start)
    b_setting.grid(row=0,column=0,pady=10,padx=58)
    b_power.grid(row=0,column=1,pady=10,padx=58)
    b_quit.grid(row=0,column=4,pady=10,padx=58)
    f4.pack(pady=5)

    #Frame 5_status
    f5=tk.LabelFrame(mainframe,bg="red",borderwidth=0)

    l_status1=tk.Label(f5,text="Off",bd=1,relief=tk.SUNKEN,anchor=tk.S,padx=10,pady=1,font="Calibri 13 ")
    l_status2=tk.Label(f5,bd=1,relief=tk.SUNKEN,anchor=tk.S,padx=10,pady=1,font="Calibri 13 ")
    l_status3=tk.Label(f5,bd=1,relief=tk.SUNKEN,anchor=tk.S,padx=10,pady=1,font="Calibri 13 ")
    l_status1.pack(side=tk.RIGHT)
    l_status2.pack(side=tk.RIGHT)
    l_status3.pack(fill=tk.X,side=tk.RIGHT,expand=True)
    f5.pack(fill=tk.BOTH,side=tk.BOTTOM)

    mainframe.pack(fill=tk.BOTH,expand=True)

    root.mainloop()
