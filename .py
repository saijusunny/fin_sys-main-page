from tkinter import *
import tkinter.ttk as ttk
# Create a window
window = Tk()
# Create a canvas
cnv = Canvas(window, borderwidth=1,width=1000)
frame = Frame(cnv)
# Create an object of horizontal scrollbar
hscrollbar = Scrollbar(window, orient="horizontal", command=cnv.xview)
hscrollbar.grid(row=1, column=0, sticky="nsew")

cnv.configure(xscrollcommand=hscrollbar.set)
cnv.grid(row=0, column=0, sticky="nsew")
# This method that helps to create canvas window
cnv.create_window((5,4), window=frame, anchor="nw", tags="frame")

tabsystem = ttk.Notebook(frame, width=100, height=100)
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=20,justify=CENTER, padding=5)
s.map('TNotebook.Tab',background=[("selected","#2f516f")])
        

tabControl = ttk.Notebook(tabsystem)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tab11 = ttk.Frame(tabControl)
tab12=  ttk.Frame(tabControl)
tab13 = ttk.Frame(tabControl)
tab14 = ttk.Frame(tabControl)
tab15 =  ttk.Frame(tabControl)
   
tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
tabControl.add(tab2,compound = LEFT, text ='Bancking')
tabControl.add(tab3,compound = LEFT, text ='Sales')
tabControl.add(tab4,compound = LEFT, text ='Expenses')
tabControl.add(tab5,compound = LEFT, text ='Payroll') 
tabControl.add(tab6,compound = LEFT, text ='Report')
tabControl.add(tab7,compound = LEFT, text ='Taxes')
tabControl.add(tab8,compound = LEFT, text ='Accounting')
tabControl.add(tab9,compound = LEFT, text ='My Account')
tabControl.add(tab10,compound = LEFT, text ='Cash Management')
tabControl.add(tab11,compound = LEFT, text ='Production')
tabControl.add(tab12,compound = LEFT, text ='Quality Management')
tabControl.add(tab13,compound = LEFT, text ='Project Management')
tabControl.add(tab14,compound = LEFT, text ='Usage Decisions')
tabControl.add(tab15,compound = LEFT, text ='Account & Payable')
tabControl.pack(expand = 1, fill ="both")


tabsystem.grid(row=0, column=0, sticky="ew")

def frame_configure(event):
    global cnv
    cnv.configure(scrollregion=cnv.bbox("all"))

frame.bind("<Configure>", frame_configure)

window.mainloop()