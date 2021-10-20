import tkinter
from gtts import gTTS
from playsound import playsound

window = tkinter.Tk()
window.title("Python Project")
window.geometry('420x350')
window.resizable(0,0)
label = tkinter.Label(window, text="Text to Speech Converter", font=("Chloe", 25, "bold"), fg="darkorchid").pack()


label1 = tkinter.Label(window, text = "Enter text : ", font=("Arial", 20)).place(x=50, y=70)

msg = tkinter.StringVar()
txt = tkinter.Entry(window, textvariable=msg, width=50)
txt.place(x=50, y=140)
language = "en"


def play():
    inp=txt.get()
    output = gTTS(text=inp)
    output.save('output.mp3')
    playsound('output.mp3')


def exit():
    window.destroy()


def reset():
    msg.set("")

bt1 = tkinter.Button(window, text="PLAY", command=play, bg="orchid2", fg="white", width=10).place(x=50, y=200)
bt2 = tkinter.Button(window, text="RESET", command=reset, bg="orchid2", fg="white",width=10).place(x=150, y=200)
bt2 = tkinter.Button(window, text="EXIT", command=exit, bg="orchid2", fg="white", width=10).place(x=250, y=200)
window.mainloop()
