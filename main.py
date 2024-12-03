# GUI Application InstaBot
# Version 1.0

# Import Section
from instaloader import Instaloader, Profile
from tkinter import Tk, Entry, Button, END, Label, Text, DISABLED, NORMAL, messagebox
from pyshorteners import Shortener
from stdiomask import getpass
from threading import Thread

# Variables
## Colors
Black = "black"
Green = "green"
White = "white"
Red = "red"
Blue = "blue"
Orange = "orange"
Magenta = "magenta"

## Window Constants
window_size = "500x600"
window_title = "InstaBot GUI"
window_color = Black

## Information
File_Name = "root.txt" ### Pointless Definition
profile = None

## Login Information
USERNAME = str(input("Enter Instagram USERNAME: "))
PASSWORD = getpass("Enter Instagram PASSWORD: ", "*")

# Functions
## Multi Thread Functions (makes the application responsive while button functions run)
def Search_Thread(Mode):
    thread = Thread(target=Get_Stat, args=(Mode, ))
    thread.start()
    
def Download_Thread():
    thread = Thread(target=Get)
    thread.start()

## Returns the text in Input Entry Field and clears it.
def Get_Input():
    Text = Input.get()
    Input.delete(0, END)
    return Text

## Attempts to login to your instagram account and retrive target user information
def User_Stat(Input_Field, Mode=0):
    global File_Name, Folder_Name, profile, Loader
    
    Loader = Instaloader()
    Loader.login(USERNAME, PASSWORD)

    try:
        if Mode == 0:
            profile = Profile.from_username(Loader.context, Input_Field)
        else:
            profile = Profile.from_id(Loader.context, Input_Field)
    except Exception as Error:
        messagebox.showerror("error", "Unexpected Error Occurred!!")
        print(Error)
        return None

    Pro_Link = URL_Engine.tinyurl.short(profile.profile_pic_url)
    
    try:
        Ext_Link = URL_Engine.tinyurl.short(profile.external_url)
    except Exception as Error:
        Ext_Link = None

    Output_Text = f"USERNAME      : {profile.username}\nID            : {profile.userid}\nName          : {profile.full_name}\nProfile Pic   : {Pro_Link}\nFollowers     : {profile.followers}\nFollowing     : {profile.followees}\nBio           : {profile.biography}\nExternal link : {Ext_Link}\nPrivate Acc   : {profile.is_private}\nVerified      : {profile.is_verified}\n"
    
    if profile.is_private == False:
        Download_All_Button.config(state=NORMAL)
    else:
        Download_All_Button.config(state=DISABLED)
    
    File_Name = f"{profile.userid}.txt"
    
    Output.config(state=NORMAL)
    Output.delete(1.0, END)
    Output.insert(END, Output_Text)
    Output.config(state=DISABLED)

## Function attached with ID and USERNAME Button Objects        
def Get_Stat(Mode=0):
    Input_Data = Get_Input()
    if Mode == 1 and Input_Data != "" and Input_Data.isdigit() == True:
        User_Stat(Input_Data, Mode)
    elif Mode == 0 and Input_Data != "":
        User_Stat(Input_Data, Mode)

## Function to save details of the user to file with file name as <userid>.txt
def Save():
    try:
        TEXT = Output.get("1.0", END)
        if TEXT != "":
            with open(File_Name, "wb") as File_Object:
                File_Object.write(TEXT.encode())
        messagebox.showinfo("info", "Details Saved Successfully!")

    except Exception as Error:
        messagebox.showerror("error", "Failed to Save Details")

## Function to Destroy main window
def Quit():
    window.destroy()

## Function to Download all the posts of a user
def Get():
    try:
        Loader.download_profile(profile, profile_pic_only=False)
        messagebox.showinfo("info", "User Posts Downloaded Successfully!")
    except Exception as Error:
        messagebox.showerror("error", "Failed to Download User Posts")

# Objects
## URL Shortener Object
URL_Engine = Shortener()

## Window Object and configurations
window = Tk()
window.geometry(window_size)
window.title(window_title)
window.configure(background=window_color)
window.resizable(False, False)

## User or ID Label Object
User_or_ID_Label = Label(window, bg=Black, fg=White, text="Username or ID", font=("calibri", 12))
User_or_ID_Label.place(x=20,y=50)

## Input Entry Field Object
Input = Entry(window, bg=Black, fg=White, bd=8, width=30)
Input.place(x=160,y=45)

## Username Button Object
Username_Button = Button(window, text="USERNAME", bg=Green, fg=White, width=10, command=lambda:Search_Thread(0))
Username_Button.place(x=390,y=30)

## ID Button Object
ID_Button = Button(window, text="ID", bg=Red, fg=White, command=lambda:Search_Thread(1), width=10)
ID_Button.place(x=390, y=70)

## Output Text Field Object
Output = Text(window, bd=8, bg=Black, fg=White, height=20, width=55)
Output.place(x=20, y=150)
Output.config(state=DISABLED)

## Output Label Object
Output_Label = Label(window, bg=Black, fg=White, text="Output Screen", font=("calibri", 12))
Output_Label.place(x=210, y=120)

## SAVE Button Object
Save_Button = Button(window, text="SAVE", bg=Blue, fg=White, width=10, command=Save)
Save_Button.place(x=380, y=525)

## QUIT Button Object
Quit_Button = Button(window, text="QUIT", bg=Orange, fg=White, width=10, command=Quit)
Quit_Button.place(x=30,y=525)

## Download Button Object
Download_All_Button = Button(window, text="DOWNLOAD", bg=Magenta, fg=White, width=10, command=Download_Thread)
Download_All_Button.place(x=210, y=525)
Download_All_Button.config(state=DISABLED)

# Main Loop
window.mainloop()