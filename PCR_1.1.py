import sys
import os
import tkinter as tk
from tkinter import filedialog

import datetime as date
import csv

import matplotlib
from matplotlib.widgets import Cursor
matplotlib.use("TkAgg")
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

# ==================================global==================================
xdata = []
a1data = []
a2data = []
a3data = []
a4data = []
b1data = []
b2data = []
b3data = []
b4data = []
ct = []
date_show = []
csv_open = False
ruler_on = False

# ==================================functions==================================
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def on_key_press(event):
    global annot
    if ruler_on:
        #global coord
        #coord.append((event.xdata, event.ydata))
        x = event.xdata
        y = event.ydata
        x = int(x)
        y = int(y)
        print("%d" %x, "%d" %y)
        
        annot.xy=(x, y)
        text = "({:d},{:d})".format(x,y)
        annot.set_text(text)
        annot.set_visible(True)
        my_canvas.draw()
    
    
def plt_config():
    global date_show
    if date_show.size > 0:
        plt.set_title(date_show[0], size=10)  # 设置表名为“表名”
    else:
        plt.set_title("No Date", size=10)
    
    plt.legend(loc='upper left')  # 线型示意说明
    plt.set_xlabel(u'cycle', size=10)  # 设置x轴名为“x轴名”
    plt.set_ylabel(u'value', size=10)  # 设置y轴名为“y轴名”
    plt.set_xlim(0)
    # 设置坐标轴刻度
    # my_x_ticks = np.arange(0, 50, 10)
    # my_y_ticks = np.arange(0, 8000, 1000)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)

    # plt.show()
    
    my_canvas.draw()
    my_canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)
   
    # my_canvas._tkcanvas.pack(expand=True)
    # toolbar.update() ??????????????
    # my_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # my_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # my_canvas.get_tk_widget().grid(row = 3, column = 1)
    
    
def show_well_all():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a1data, label='1A ct:{}'.format(ct[0]), color='red', linewidth=1)
        plt.plot(xdata, a2data, label='2A ct:{}'.format(ct[1]), color='orange', linewidth=1)
        plt.plot(xdata, a3data, label='3A ct:{}'.format(ct[2]), color='gold', linewidth=1)
        plt.plot(xdata, a4data, label='4A ct:{}'.format(ct[3]), color='brown', linewidth=1)
    
        plt.plot(xdata, b1data, label='1B ct:{}'.format(ct[4]), color='green', linewidth=1)
        plt.plot(xdata, b2data, label='2B ct:{}'.format(ct[5]), color='cyan', linewidth=1)
        plt.plot(xdata, b3data, label='3B ct:{}'.format(ct[6]), color='blue', linewidth=1)
        plt.plot(xdata, b4data, label='4B ct:{}'.format(ct[7]), color='purple', linewidth=1)

        plt_config()
        
        
    

    
def show_well_A():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a1data, label='1A ct:{}'.format(ct[0]), color='red', linewidth=1)
        plt.plot(xdata, a2data, label='2A ct:{}'.format(ct[1]), color='orange', linewidth=1)
        plt.plot(xdata, a3data, label='3A ct:{}'.format(ct[2]), color='gold', linewidth=1)
        plt.plot(xdata, a4data, label='4A ct:{}'.format(ct[3]), color='brown', linewidth=1)
    

        plt_config()

def show_well_B():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, b1data, label='1B ct:{}'.format(ct[4]), color='green', linewidth=1)
        plt.plot(xdata, b2data, label='2B ct:{}'.format(ct[5]), color='cyan', linewidth=1)
        plt.plot(xdata, b3data, label='3B ct:{}'.format(ct[6]), color='blue', linewidth=1)
        plt.plot(xdata, b4data, label='4B ct:{}'.format(ct[7]), color='purple', linewidth=1)

        plt_config()
            
def show_ch_1():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a1data, label='1A ct:{}'.format(ct[0]), color='red', linewidth=1)
        plt.plot(xdata, b1data, label='1B ct:{}'.format(ct[4]), color='green', linewidth=1)
    

        plt_config()

def show_ch_2():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a2data, label='2A ct:{}'.format(ct[1]), color='orange', linewidth=1)
        plt.plot(xdata, b2data, label='2B ct:{}'.format(ct[5]), color='cyan', linewidth=1)
    

        plt_config()

def show_ch_3():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a3data, label='3A ct:{}'.format(ct[2]), color='gold', linewidth=1)
        plt.plot(xdata, b3data, label='3B ct:{}'.format(ct[6]), color='blue', linewidth=1)
    

        plt_config()
        
def show_ch_4():
    global csv_open
    if csv_open:
        plt.clear()
        plt.plot(xdata, a4data, label='4A ct:{}'.format(ct[3]), color='brown', linewidth=1)
        plt.plot(xdata, b4data, label='4B ct:{}'.format(ct[7]), color='purple', linewidth=1)
    

        plt_config()     
    

   



def open_csv():
    global xdata, a1data, a2data, a3data, a4data, b1data, b2data, b3data, b4data, ct, date_show,csv_open
    root.fileName = filedialog.askopenfilename(filetypes=[("csv files", "*.csv")])
    # root.fileName = filedialog.askopenfilename( filetypes = ( ("csv files", "*.csv"), ("All files", "*.*")))
    # data = pd.read_csv(r'C:\Users\ForealSpectrum\Desktop\py\data01.csv')
    data = pd.read_csv(root.fileName)
    xdata = data.index[data['Type'] == "Original Data"]
    a1data = data.loc[data['Type'] == "Original Data", '1A'].astype("int64")
    a2data = data.loc[data['Type'] == "Original Data", '2A'].astype("int64")
    a3data = data.loc[data['Type'] == "Original Data", '3A'].astype("int64")
    a4data = data.loc[data['Type'] == "Original Data", '4A'].astype("int64")

    b1data = data.loc[data['Type'] == "Original Data", '1B'].astype("int64")
    b2data = data.loc[data['Type'] == "Original Data", '2B'].astype("int64")
    b3data = data.loc[data['Type'] == "Original Data", '3B'].astype("int64")
    b4data = data.loc[data['Type'] == "Original Data", '4B'].astype("int64")

    year = data.loc[data['Type'] == "Date", '1A'].values
    month = data.loc[data['Type'] == "Date", '2A'].values
    day = data.loc[data['Type'] == "Date", '3A'].values
    week = data.loc[data['Type'] == "Date", '4A'].values
    hour = data.loc[data['Type'] == "Date", '1B'].values
    minute = data.loc[data['Type'] == "Date", '2B'].values

    ct_read = data.loc[data['Type'] == "Ct Value"].to_numpy().tolist()
    ct = ct_read[0][:8]

    for index, value in enumerate(ct):
        if (value == '0.00') | (value == '0'):
            ct[index] = 'Nan'

    root.ct_show.set(ct)

    date_show = year + "-" + month + "-" + day + " " + week + " " + hour + ":" + minute

    csv_open = True
    if csv_open:
        btn_annot.config(state=tk.NORMAL)
        show_well_all()
        label_show.destroy()
def ruler():
    global ruler_on,csv_open,annot
    if ruler_var.get() == "ON":
        print("turning on...")
        ruler_on = True
        tkagg.cursord = Cursor(plt, useblit=True, color='black', linewidth=1)
        annot = plt.annotate("", xy=(0,0),
                     xytext=(-40,40),
                     textcoords="offset points",
                     bbox=dict(boxstyle='round4', fc='linen', ec='k', lw=1),
                     arrowprops=dict(arrowstyle="-|>")) 
        annot.set_visible(False)
        plt_config()
    else:
        print("turning off...")
        ruler_on = False
        tkagg.cursord = Cursor(plt, horizOn=False, vertOn=False, useblit=True, color='black', linewidth=1)
        plt_config()
        
        
def show_report():
    print('report')
    
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
# ==================================root==================================
root = tk.Tk()
#bg = root.cget("background")
#root.configure(background='SystemButtonFace')
root.configure(background='cyan')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

ui_width = screen_width*0.75
ui_height = screen_height*0.75
root.geometry('%dx%d' % (ui_width, ui_height))

# root.overrideredirect(True)
root.overrideredirect(False)
# root.attributes('-fullscreen',True)

# root.resizable(0, 0)

root.ct_show = tk.StringVar()

root.title('PCR Reader')
root.iconbitmap(resource_path(r'.\omec.ico'))
#icon = tk.PhotoImage(file="omeclogo.png")
#root.iconphoto(False, icon)
# ==================================Frames==================================

Top_section = tk.Frame(root, width=ui_width , height=ui_height / 7, bd=8, background = "white", relief="raise")
Top_section.grid(row=0, column=0, columnspan=3,  sticky=tk.N)

Button_group = tk.Frame(root, width=ui_width / 4, height=ui_height / 7 * 6, bd=4, relief="groove")
Button_group.grid(row=1, column=0, rowspan=3, sticky=tk.NW)

Well_section = tk.Frame(root, width=ui_width / 4 * 3, height=ui_height *6 / 35 , bd=4, relief="ridge")
Well_section.grid(row=1, column=1, columnspan=2, sticky=tk.NW)

show_width = ui_width / 4 * 3
show_height = ui_height/7*6/5*7/2

Show_section = tk.Frame(root, width=show_width, height=show_height,  background="white", bd=4, relief="groove")
Show_section.grid(row=2, column=1, columnspan=2, sticky=tk.NW)

Reserved_section = tk.Frame(root, width=show_width/2, height= ui_height / 7 * 6 - ui_height *6 / 35 - show_height, relief="ridge")
Reserved_section.grid(row=3, column=1, sticky=tk.S)

Tool_section = tk.Frame(root, width=show_width/2, height= ui_height / 7 * 6 - ui_height *6 / 35 - show_height)
Tool_section.grid(row=3, column=2, sticky=tk.S)
# ==================================define stuffs==================================



btn_file = tk.Button(Button_group,
                     text="Open",

                     font=('Helvetica', '30'),
                     command=open_csv
                     )
btn_1 = tk.Button(Button_group,
                  text="Report",

                  font=('Helvetica', '30'),
                  command=show_report
                  )

btn_2 = tk.Button(Button_group,
                  text="",

                  font=('Helvetica', '30')
                  )

btn_3 = tk.Button(Button_group,
                  text="",

                  font=('Helvetica', '30'),
                 
                  )

btn_4 = tk.Button(Button_group,
                  text="Exit",

                  font=('Helvetica', '30'),
                  command=_quit
                  )

btn_well_1 = tk.Button(Well_section,
                  text="All",

                  font=('Helvetica', '20'),
                  command=show_well_all
                  )

btn_well_2 = tk.Button(Well_section,
                  text="Channel A",

                  font=('Helvetica', '20'),
                  command=show_well_A
                  )

btn_well_3 = tk.Button(Well_section,
                  text="Channel B",

                  font=('Helvetica', '20'),
                  command=show_well_B
                  )

btn_ch_1 = tk.Button(Well_section,
                  text="Well 1",

                  font=('Helvetica', '20'),
                  command=show_ch_1
                  )

btn_ch_2 = tk.Button(Well_section,
                  text="Well 2",

                  font=('Helvetica', '20'),
                  command=show_ch_2
                  )

btn_ch_3 = tk.Button(Well_section,
                  text="Well 3",

                  font=('Helvetica', '20'),
                  command=show_ch_3
                  )

btn_ch_4 = tk.Button(Well_section,
                  text="Well 4",

                  font=('Helvetica', '20'),
                  command=show_ch_4
                  )

ruler_var = tk.StringVar()

btn_annot = tk.Checkbutton(Reserved_section,
                  onvalue="ON",
                  offvalue="OFF",
                  variable=ruler_var,
                  text="Ruler",
                  font=('Helvetica', '20'),
                  indicatoron=False,
                  state=tk.DISABLED,
                  command=ruler
                  )
ruler_var.set("OFF")


btn_reset = tk.Button(Reserved_section,
                  text="Reset",

                  font=('Helvetica', '20'),
                  command=show_well_all
                  )

btn_list = [btn_file, btn_1, btn_2, btn_3, btn_4, btn_well_1, btn_well_2, btn_well_3, btn_ch_1, btn_ch_2, btn_ch_3, btn_ch_4, btn_annot, btn_reset]
for btn in btn_list:
        btn.configure(bg = 'white',
                      fg = 'blue',
                      relief = 'solid',
                      bd = 1,
                      activebackground = 'blue',
                      activeforeground = 'white',
                      )

figdpi = 100
wave = Figure(figsize=(show_width / figdpi, show_height/ figdpi), dpi=figdpi)

plt = wave.add_subplot(111)

my_canvas = FigureCanvasTkAgg(wave, Show_section)
label_show = tk.Label(Show_section, font=('Helvetica', 30),
                      text = f"Click \"Open\" to choos a report file",
                      bg = "white")
#label_date = tk.Label(Top_section, font=('Helvetica', 20), text=f"Date: {date.datetime.date(date.datetime.now())}\n ")
label_title = tk.Label(Top_section, font=('Times New Roman', 30, 'bold'),
                       text = f"PCR Result Reader",
                       bg = "white")
# label_ct = tk.Label(root, textvariable =root.ct_show, font=('Helvetica', '20'))


# ==================================pack==================================

#label_date.place(relx=0.5, rely=0.5, anchor="center")
label_title.place(relx=0.5, rely=0.5, anchor="center")
label_show.place(relx=0.5, rely=0.5, anchor="center")
#my_canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)
toolbar = NavigationToolbar2Tk(my_canvas, Tool_section, pack_toolbar=False)
toolbar.place(relx=0, rely=0, relwidth=1)
wave.canvas.mpl_connect("button_press_event", on_key_press)

btn_file.place(relx=0, rely=0, relwidth=1, relheight=0.2)
btn_1.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)
btn_2.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)
btn_3.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)
btn_4.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

btn_well_1.place(relx=0, rely=0, relwidth=0.25, relheight=0.5)
btn_well_2.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.5)
btn_well_3.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.5)

btn_ch_1.place(relx=0, rely=0.5, relwidth=0.25, relheight=0.5)
btn_ch_2.place(relx=0.25, rely=0.5, relwidth=0.25, relheight=0.5)
btn_ch_3.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.5)
btn_ch_4.place(relx=0.75, rely=0.5, relwidth=0.25, relheight=0.5)

btn_annot.place(relx=0.25, rely=0.1, relwidth=0.25, relheight=0.5)
btn_reset.place(relx=0.5, rely=0.1, relwidth=0.25, relheight=0.5)

root.mainloop()
