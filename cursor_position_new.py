import tkinter as tk
from tkinter import ttk
from pyautogui import position

def run():
  show = tk.Toplevel()
  show.title('show')
  show.attributes('-topmost', True)
  show.overrideredirect(True)
  label = ttk.Label(show, textvariable= pos)
  label.pack()
  btn_run.configure(state='disable')

  def update_label():
    pos.set(f'{position()[0]} - {position()[1]}')
    show.geometry(f'+{position()[0] + 15}+{position()[1] + 30}')
    show.attributes('-alpha', v_transparency.get())
    label.configure(font=("Helvetica", v_size.get(), 'bold'),
                    background=v_bg.get(), foreground=v_text_color.get())
    show.after(50, update_label)

  update_label()

win = tk.Tk()
win.title('Cursor position')
win.geometry('280x150')
win.resizable(False,False)

pos = tk.StringVar()
v_transparency = tk.DoubleVar()
v_size = tk.IntVar()
v_size.set(25)
v_transparency.set(1)
v_bg = tk.StringVar()
v_bg.set('#FFFFFF')
v_text_color = tk.StringVar()
v_text_color.set('#000000')

frm_main = tk.Frame(win)
frm_main.pack()

label_color = tk.Label(frm_main, text='COLOR: ')
label_color.grid(row=0, column=0, sticky='w', ipady=5)
menubtn_bg_color = ttk.Menubutton(frm_main,text='Background')
menubtn_bg_color.grid(row=0,column=1)
menu_bg = tk.Menu(menubtn_bg_color,tearoff=0)
menubtn_bg_color['menu'] = menu_bg
menu_bg.add_radiobutton(background='Red',command= lambda: v_bg.set('Red'))
menu_bg.add_radiobutton(background='Green',command= lambda: v_bg.set('Green'))
menu_bg.add_radiobutton(background='Blue',command= lambda: v_bg.set('Blue'))
menu_bg.add_radiobutton(background='Yellow',command= lambda: v_bg.set('Yellow'))
menu_bg.add_radiobutton(background='White',command= lambda: v_bg.set('White'))
menu_bg.add_radiobutton(background='Black',command= lambda: v_bg.set('Black'))

menubtn_txt_color = ttk.Menubutton(frm_main,text='Text')
menubtn_txt_color.grid(row=0,column=4)
menu_txt = tk.Menu(menubtn_txt_color,tearoff=0)
menubtn_txt_color['menu'] = menu_txt
menu_txt.add_radiobutton(background='White',command= lambda: v_text_color.set('White'))
menu_txt.add_radiobutton(background='Black',command= lambda: v_text_color.set('Black'))

label_transparency = tk.Label(frm_main, text='TRANS: ')
label_transparency.grid(row=2, column=0, sticky='w', ipady=5)
scale_transparency = ttk.Scale(frm_main, variable=v_transparency, from_=0.1, to=1, orient="horizontal",length=100)
scale_transparency.grid(row=2, column=1, sticky='w', columnspan=2)

label_size = tk.Label(frm_main, text='SIZE: ')
label_size.grid(row=3, column=0, sticky='w', ipady=5)
scale_size = ttk.Scale(frm_main, variable= v_size, from_=5, to=50, orient="horizontal",length=100)
scale_size.grid(row=3, column=1, sticky='w', columnspan=2)

frm_btn = tk.Frame(win)
frm_btn.pack(pady=10)

btn_run = ttk.Button(frm_btn, text='Run', command=run)
btn_run.pack(side='left')

btn_stop = ttk.Button(frm_btn, text='Close', command=lambda: exit())
btn_stop.pack()

win.mainloop()




