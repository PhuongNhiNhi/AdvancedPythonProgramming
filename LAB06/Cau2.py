import tKinter

def increment(text):
  count = int(text.get())
  text.set(str(count + 1))
  
 window = tkinter.TK()
frame = tkinter.Frame(window)
frame.pack()

text = tkinter.StringVar()
text.set('0')

button = tkinter.Button(frame, textvariable=text,
 command=lambda: increment(text))
button.pack()
window.mainloop()

