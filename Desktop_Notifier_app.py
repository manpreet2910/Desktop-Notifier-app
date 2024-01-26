from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Desktop Notifier')
t.geometry("500x350")
img = Image.open("icon.jpg")
img = img.resize((50,50), Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(img)


def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == " " or get_msg == " " or get_time == " ":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time*60
        messagebox.showinfo("set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Desktop Notifier",
                            app_icon="bell.ico",
                            toast=True,
                            timeout=20
                           )

img_label = Label(t, image=tkimage)
img_label.place(x=10,y=9)

title_label = Label(t, text="My Desktop Notifier", font=("poppins", 14, "bold"))
title_label.place(x=75, y=20)

t_label = Label(t, text="Title",font=("poppins", 10))
t_label.place(x=12, y=70)

title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

m_label = Label(t, text="Message", font=("poppins", 10))
m_label.place(x=12, y=120)


msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)


time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)


time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)


time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)


but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()