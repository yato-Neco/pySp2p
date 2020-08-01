def btn_click():
    msg = b"123"
    msg = txt.get()
    client.main(msg)

import prints
import client
import tkinter
from tkinter import ttk

#メインウィンドウ
main_win = tkinter.Tk()
main_win.title("test")
main_win.geometry("500x120")

#メインフレーム
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

#テキスト入力
txt = ttk.Entry(width=30)
txt.place(x=50, y=60)

#テキスト入手
btn = ttk.Button(main_win, text='Enter', command=btn_click)
btn.place(x=250, y=58)


main_win.mainloop()
