import client
def btn_send():
    setting = txt_settings.get()
    msg = txt_send.get()
    client.client(setting,msg)
def wind():

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
    global txt_send
    global txt_settings
    txt_send = ttk.Entry(width=30)
    txt_send.place(x=50, y=60)
    txt_settings = ttk.Entry(width=20)
    txt_settings.place(x=50, y=30)

    #テキスト入手
    btxt_send = ttk.Button(main_win, text='Enter', command=btn_send)
    btxt_send.place(x=250, y=58)


    main_win.mainloop()
wind()
