import tkinter
from tkinter import messagebox
from src.stocks_api import get_stocks


root = tkinter.Tk()
root.geometry('500x500')
root.title('Stock Grabber')
root.eval('tk::PlaceWindow . center')

def get_name():
    user_name = entry_field.get()
    tkinter.Label(bot_frame, text=user_name).pack()

def get_user_stocks():
    users_stocks = entry_field.get()
    messagebox.showinfo("Stock Info", get_stocks(users_stocks))

# Top Frame and it's contents
top_frame = tkinter.Frame(root, padx=20, pady=20, bg="Green")
top_frame.pack()
entry_field = tkinter.Entry(top_frame)
entry_field.pack(pady=30)
submit_btn = tkinter.Button(top_frame, text="Submit", command=get_user_stocks)
submit_btn.pack()

# Bottom Frame and it's contents
bot_frame = tkinter.Frame(root, padx=20, pady=20, bg="Blue")
bot_frame.pack()


root.mainloop()