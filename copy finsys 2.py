import matplotlib.pyplot as plt
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbilling", port="3306"
# )
# fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1366x768+0+0")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#-------------------------------------------------------------------------------------------------------------------------Images
# banking = PhotoImage(file="images/banking.PNG")
# sales = PhotoImage(file="images/sheet.PNG")
# expenses = PhotoImage(file="images/expense.PNG")
# payroll = PhotoImage(file="images/payroll.PNG")
# report = PhotoImage(file="images/reports.PNG")
# taxes = PhotoImage(file="images/taxes.PNG")
# accounts = PhotoImage(file="images/accounting.PNG")



imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

stn =PIL.Image.open("images\Settings.PNG")
stn_img=ImageTk.PhotoImage(stn)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

sig_up =PIL.Image.open("images/register.png")
resized_sign_up= sig_up.resize((500,400))
sign_up=ImageTk.PhotoImage(resized_sign_up)

#------------------------------------------------------------------------------------------------------------Login Button Function

def main_sign_in():
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_signin.pack_forget()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    Sys_top_frame.grid_columnconfigure(0,weight=1)
    Sys_top_frame.grid_rowconfigure(0,weight=1)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=400)#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1,sticky='nsew')

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1,sticky='nsew')
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2,sticky='nsew')
  
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    

    tp_lb_srh=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=700)#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2,sticky='nsew')
    def srh_fn(event):
        if srh_top.get()=="Search":
            srh_top.delete(0,END)
        else:
            pass

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Search")
    srh_top.bind("<Button-1>",srh_fn)
    srh_top.grid(row=2,column=1,padx=(30,0), pady=20,sticky='nsew')

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=2,column=4,padx=(0,30))

    srh_btn = Button(tp_lb_srh, image=stn_img, bg="#213b52", fg="black",border=0)
    srh_btn.grid(row=2,column=5,padx=(0,30))

    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=100)#-----------------------------Notification
    tp_lb_nm.grid(row=1,column=3,sticky='nsew')
    
    tp_lb_npr=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=200)#---------------------------profile area name
    tp_lb_npr.grid(row=1,column=4,sticky='nsew')
    label = Label(tp_lb_npr, text="Errors",bg="#213b52", fg="white", anchor="center",width=10,font=('Calibri 16 bold'),border=0)
    label.grid(row=1,column=1,sticky='nsew')
    label = Label(tp_lb_npr, text="Online",bg="#213b52", fg="white",width=15,font=('Calibri 12 bold'),border=0)
    label.grid(row=2,column=1,sticky='nsew')

    pro =PIL.Image.open("images/user.png")
    resized_pro= pro.resize((20,20))
    pro_pic= ImageTk.PhotoImage(resized_pro)
    
    def lst_frt():
        lst_prf.place_forget()
        srh_btn3 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
        srh_btn3.grid(row=2,column=2,padx=15)
    def lst_prf_slt(event):
        def edit_profile():
            def responsive_widgets_edit(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget


                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.53

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                              

                
                # dcanvas.coords("bg_polygen_pr",dwidth/16,dheight/.6,dwidth/1.07,dheight/9)
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("pr_crpass_lb",dwidth/17.075,dheight/1.33)
                dcanvas.coords("pr_crpass_ent",dwidth/17.075,dheight/1.26)
                dcanvas.coords("pr_re_pass_lb",dwidth/17.075,dheight/1.16)
                dcanvas.coords("pr_re_pass_ent",dwidth/17.075,dheight/1.1)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)
                dcanvas.coords("pr_new_pass_lb",dwidth/1.92,dheight/1.33)
                dcanvas.coords("pr_new_pass_ent",dwidth/1.92,dheight/1.26)

                
                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/0.93)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/0.89)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/0.84)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/0.81)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/0.77)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.745)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.712)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.69)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.66)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.64)
                dcanvas.coords("cmp_file_lb",dwidth/17.075,dheight/.615)
                dcanvas.coords("cmp_file_ent",dwidth/17.075,dheight/.6)
                

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/0.93)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/0.89)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/0.84)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/0.81)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/0.77)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.745)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.712)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.69)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.66)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.64)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.57)
           
            Sys_mains_frame_pr.place_forget()

            global Sys_mains_frame_pr_ed
            Sys_mains_frame_pr_ed=Frame(tab1, height=750)
            Sys_mains_frame_pr_ed.place(x=0,y=0)
            

            pr_canvas_ed=Canvas(Sys_mains_frame_pr_ed,height=700,width=1340,scrollregion=(0,0,700,1450),bg="#2f516f",border=0)
            pr_canvas_ed.bind("<Configure>", responsive_widgets_edit)
            
            pr_myscrollbar_ed=Scrollbar(Sys_mains_frame_pr_ed,orient="vertical",command=pr_canvas_ed.yview)
            pr_canvas_ed.configure(yscrollcommand=pr_myscrollbar_ed.set)

            pr_myscrollbar_ed.grid(row=0,column=1,sticky='ns')
            pr_canvas_ed.grid(row=0,column=0,sticky='nsew')

            rth2 = pr_canvas_ed.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_pr"),smooth=True,)

            grd1c=Label(pr_canvas_ed, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas_ed.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas_ed, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas_ed, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas_ed, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            pr_crpass_lb=Label(pr_canvas_ed, text="Enter your Current Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_lb,tag=("pr_crpass_lb"))

            pr_crpass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_crpass_ent,tag=("pr_crpass_ent"))

            pr_re_pass_lb=Label(pr_canvas_ed, text="Re-type new Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_lb,tag=("pr_re_pass_lb"))

            pr_re_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_re_pass_ent,tag=("pr_re_pass_ent"))


            em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas_ed, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas_ed, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            pr_new_pass_lb=Label(pr_canvas_ed, text="Enter New Password",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_lb,tag=("pr_new_pass_lb"))

            pr_new_pass_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=pr_new_pass_ent,tag=("pr_new_pass_ent"))


            # #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas_ed, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas_ed, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas_ed, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas_ed, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas_ed, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas_ed, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            # #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas_ed, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas_ed, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas_ed, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas_ed, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas_ed, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))

            cmp_file_lb=Label(pr_canvas_ed, text="File",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_lb,tag=("cmp_file_lb"))

            cmp_file_ent=Entry(pr_canvas_ed,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=cmp_file_ent,tag=("cmp_file_ent"))


            btn_edit = Button(pr_canvas_ed, text='Update Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas_ed.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))

        def curve_pr(x1, y1, x2, y2, radius=25, **kwargs):
            
            points = [x1+radius, y1,
                    x1+radius, y1,
                    x2-radius, y1,
                    x2-radius, y1,
                    x2, y1,
                    x2, y1+radius,
                    x2, y1+radius,
                    x2, y2-radius,
                    x2, y2-radius,
                    x2, y2,
                    x2-radius, y2,
                    x2-radius, y2,
                    x1+radius, y2,
                    x1+radius, y2,
                    x1, y2,
                    x1, y2-radius,
                    x1, y2-radius,
                    x1, y1+radius,
                    x1, y1+radius,
                    x1, y1]
        
            return pr_canvas.create_polygon(points, **kwargs, smooth=True)
        
        selected_indices = lst_prf.curselection()
        selected_langs = ",".join([lst_prf.get(i) for i in selected_indices])
        lst_prf.place_forget()
        if selected_langs=="Profile":
            
            Sys_mains_frame.pack_forget()
            global Sys_mains_frame_pr
            def responsive_widgets(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/13
                y2 = dheight/.6

                dcanvas.coords("bg_polygen_pr",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )                   

                
                
                dcanvas.coords("my_pro",dwidth/2.3,dheight/12.5)

                dcanvas.coords("pr_hr_l",dwidth/16,dheight/7,dwidth/1.07,dheight/7)
                dcanvas.coords("pr_hd",dwidth/20,dheight/2.2)
                dcanvas.coords("pr_1_nm",dwidth/17.075,dheight/1.9)
                dcanvas.coords("fr_name_ent",dwidth/17.075,dheight/1.75)
                dcanvas.coords("pr_em_lb",dwidth/17.075,dheight/1.56)
                dcanvas.coords("em_ent",dwidth/17.075,dheight/1.47)
                dcanvas.coords("last_nm_lb",dwidth/1.92,dheight/1.9)
                dcanvas.coords("lst_nm_ent",dwidth/1.92,dheight/1.75)
                dcanvas.coords("usr_nm_lb",dwidth/1.92,dheight/1.56)
                dcanvas.coords("usr_nm_ent",dwidth/1.92,dheight/1.47)

                #-------------------------------------------------------------------------company section
                dcanvas.coords("cmp_hd",dwidth/20,dheight/1.32)
                dcanvas.coords("cmp_nm_lb",dwidth/17.075,dheight/1.22)
                dcanvas.coords("cmp_nm_ent",dwidth/17.075,dheight/1.16)
                dcanvas.coords("cmp_cty_lb",dwidth/17.075,dheight/1.07)
                dcanvas.coords("cmp_cty_ent",dwidth/17.075,dheight/1.02)
                dcanvas.coords("cmp_pin_lb",dwidth/17.075,dheight/.95)
                dcanvas.coords("cmp_pin_ent",dwidth/17.075,dheight/.91)
                dcanvas.coords("cmp_ph_lb",dwidth/17.075,dheight/.86)
                dcanvas.coords("cmp_ph_ent",dwidth/17.075,dheight/.83)
                dcanvas.coords("cmp_indest_lb",dwidth/17.075,dheight/.78)
                dcanvas.coords("cmp_indest_ent",dwidth/17.075,dheight/.755)

                #--------------------------------------------------------------------------company right

                dcanvas.coords("cmp_addr_lb",dwidth/1.92,dheight/1.22)
                dcanvas.coords("cmp_addr_ent",dwidth/1.92,dheight/1.16)
                dcanvas.coords("cmp_st_lb",dwidth/1.92,dheight/1.07)
                dcanvas.coords("cmp_st_ent",dwidth/1.92,dheight/1.02)
                dcanvas.coords("cmp_em_lb",dwidth/1.92,dheight/.95)
                dcanvas.coords("cmp_em_ent",dwidth/1.92,dheight/.91)
                dcanvas.coords("cmp_lg_nm",dwidth/1.92,dheight/.86)
                dcanvas.coords("cmp_lg_ent",dwidth/1.92,dheight/.83)
                dcanvas.coords("cmp_typ_lb",dwidth/1.92,dheight/.78)
                dcanvas.coords("cmp_typ_ent",dwidth/1.92,dheight/.755)
                dcanvas.coords("btn_edit",dwidth/2.4,dheight/.71)
                
                

                
                    
            Sys_mains_frame_pr=Frame(tab1, height=750,bg="#2f516f",)
            Sys_mains_frame_pr.place(x=0,y=0)
            # Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
            # Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

            pr_canvas=Canvas(Sys_mains_frame_pr,height=700,width=1340,scrollregion=(0,0,700,1300),bg="#2f516f",border=0)
            pr_canvas.bind("<Configure>", responsive_widgets)

            pr_myscrollbar=Scrollbar(Sys_mains_frame_pr,orient="vertical",command=pr_canvas.yview)
            pr_canvas.configure(yscrollcommand=pr_myscrollbar.set)

            Sys_mains_frame_pr.grid_rowconfigure(0,weight=1)
            Sys_mains_frame_pr.grid_columnconfigure(0,weight=1)

            pr_myscrollbar.grid(row=0,column=1,sticky='ns')
            pr_canvas.grid(row=0,column=0,sticky='nsew')

            rth2 = pr_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",smooth=True,tags=("bg_polygen_pr"))

            grd1c=Label(pr_canvas, text="MY PROFILE",bg="#213b52", fg="White", anchor="center",font=('Calibri 24 bold'))
            win_inv1 = pr_canvas.create_window(0, 0, anchor="nw", window=grd1c,tags=("my_pro"))

            pr_canvas.create_line(0,0, 0, 0,fill="gray",tags=("pr_hr_l") )
            #----------------------------------------------------------------------------------------Personal info
            pr_hd=Label(pr_canvas, text="Personal Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=pr_hd,tags=("pr_hd"))

            fir_name=Label(pr_canvas, text="First Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=fir_name,tags=("pr_1_nm"))

            fr_name_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=fr_name_ent,tags=("fr_name_ent"))

            pr_em_lb=Label(pr_canvas, text="E-Mail",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=pr_em_lb,tags=("pr_em_lb"))

            em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=em_ent,tag=("em_ent"))

            last_nm_lb=Label(pr_canvas, text="Last Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=last_nm_lb,tag=("last_nm_lb"))

            lst_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=lst_nm_ent,tag=("lst_nm_ent"))

            usr_nm_lb=Label(pr_canvas, text="Username",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_lb, tag=("usr_nm_lb"))

            usr_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=usr_nm_ent,tag=("usr_nm_ent"))

            #------------------------------------------------------------------------------------------------COMPANY SECTION
            cmp_hd=Label(pr_canvas, text="Company Info",bg="#213b52", fg="White", anchor="center",font=('Calibri 18 bold'))
            win_pr = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_hd,tag=("cmp_hd"))

            cmp_nm_lb=Label(pr_canvas, text="Company Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_lb,tag=("cmp_nm_lb"))

            cmp_nm_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_nm_ent,tag=("cmp_nm_ent"))

            cmp_cty_lb=Label(pr_canvas, text="City",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_lb,tag=("cmp_cty_lb"))

            cmp_cty_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_cty_ent,tag=("cmp_cty_ent"))

            cmp_pin_lb=Label(pr_canvas, text="Pincode",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_lb,tag=("cmp_pin_lb"))

            cmp_pin_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_pin_ent,tag=("cmp_pin_ent"))

            cmp_ph_lb=Label(pr_canvas, text="Phone Number",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_lb,tag=("cmp_ph_lb"))

            cmp_ph_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_ph_ent,tag=("cmp_ph_ent"))

            cmp_indest_lb=Label(pr_canvas, text="Your Industry",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_lb,tag=("cmp_indest_lb"))

            cmp_indest_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_indest_ent,tag=("cmp_indest_ent"))

            #----------------------------------------------------------------------------------------------------RIGHT SIDE
            cmp_addr_lb=Label(pr_canvas, text="Company Address",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_lb,tag=("cmp_addr_lb"))

            cmp_addr_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_addr_ent,tag=("cmp_addr_ent"))

            cmp_st_lb=Label(pr_canvas, text="State",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_lb,tag=("cmp_st_lb"))

            cmp_st_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_st_ent,tag=("cmp_st_ent"))

            cmp_em_lb=Label(pr_canvas, text="Email",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_lb,tag=("cmp_em_lb"))

            cmp_em_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_em_ent,tag=("cmp_em_ent"))

            cmp_lg_nm=Label(pr_canvas, text="Legal Business Name",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_nm,tag=("cmp_lg_nm"))

            cmp_lg_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_lg_ent,tag=("cmp_lg_ent"))

            cmp_typ_lb=Label(pr_canvas, text="Company Type",bg="#213b52", fg="White", anchor="center",font=('Calibri 14 bold'))
            win_info = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_lb,tag=("cmp_typ_lb"))

            cmp_typ_ent=Entry(pr_canvas,width=55,font=('Calibri 14 bold'))
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=cmp_typ_ent,tag=("cmp_typ_ent"))


            btn_edit = Button(pr_canvas, text='Edit Profile', command=edit_profile, bg="#213b52", fg="White",borderwidth = 3,height=2,width=30)
            win_info1 = pr_canvas.create_window(0, 0, anchor="nw", window=btn_edit,tag=("btn_edit"))
        elif selected_langs=="Log Out":
            
            Sys_top_frame2.pack_forget()
            Sys_top_frame.pack_forget()
            fun_sign_in()
        elif selected_langs== "Dashboard":
            try:
                Sys_mains_frame_pr_ed.place_forget()
            except:
                pass
            try:
                
                Sys_mains_frame_pr.place_forget()
            except:
                pass
           
            try:
                Sys_mains_frame.pack(fill=X)
            except:
                pass
         

        else:
            pass

    def profile():
        # create a list box
        langs = ("Dashboard","Profile","Log Out")

        langs_var = StringVar(value=langs)
        global lst_prf
        lst_prf = Listbox(root,listvariable=langs_var,height=3 ,selectmode='extended',bg="black",fg="white")

        lst_prf.place(x=1200,y=70)
        lst_prf.bind('<<ListboxSelect>>', lst_prf_slt)
        srh_btn.grid_forget()
        srh_btn2 = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=lst_frt)
        srh_btn2.grid(row=2,column=2,padx=15)
   
    srh_btn = Button(tp_lb_npr, bg="White", fg="black",height=2,width=5,border=0,command=profile)
    srh_btn.grid(row=2,column=2,padx=15)

    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
    Sys_top_frame2.pack(fill=X)
    
    
  
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
    def right_nav():
        
        tabControl.pack_forget()
        btn_nav.place_forget()
        tabControl2.pack(expand = 1, fill ="both")
        btn_nav2.place(x=0,y=0)
        try:
            btn_nav3.place_forget()
        except:
            pass
    def left_nav():
        
        tabControl2.pack_forget()
        btn_nav2.place_forget()
        tabControl.pack(expand = 1, fill ="both")
        global btn_nav3
        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
        btn_nav3.place(x=1325,y=0)

    tabControl = ttk.Notebook(Sys_top_frame2)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    
    
    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
    btn_nav.place(x=1325,y=0)
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Banking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    
    tabControl.pack(expand = 1, fill ="both")


    
    tabControl2 = ttk.Notebook(Sys_top_frame2)
    tab9 =  ttk.Frame(tabControl2)
    tab10=  ttk.Frame(tabControl2)
    tab11 = ttk.Frame(tabControl2)
    tab12=  ttk.Frame(tabControl2)
    tab13 = ttk.Frame(tabControl2)
    tab14 = ttk.Frame(tabControl2)
    tab15 =  ttk.Frame(tabControl2)

    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
    
        
    tabControl2.add(tab9,compound = LEFT, text ='My Account')
    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl2.add(tab11,compound = LEFT, text ='Production')
    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

   
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Dash Board}
    
    Sys_mains_frame=Frame(tab1, height=750,bg="#2f516f",)
    Sys_mains_frame.pack(fill=X)
    
    canvas=Canvas(Sys_mains_frame,height=700,scrollregion=(0,0,700,1200),bg="#2f516f",border=0)
    frame=Frame(canvas,bg="#2f516f")
    myscrollbar=Scrollbar(Sys_mains_frame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(fill=X)
    canvas.create_window((10,0),window=frame,anchor='nw')

    cmp_name=Label(canvas, text="Clown",bg="#213b52", fg="White",width=69, anchor="center",font=('Calibri 24 bold'))
  
    win_inv1 = canvas.create_window(80, 50, anchor="nw", window=cmp_name)
    def curve(x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    
        return canvas.create_polygon(points, **kwargs, smooth=True)

    rtg = curve(40, 30, 1300, 120, radius=20, fill="#213b52")#----------------------------heading
    #----------------------------------------------------------------------------------------------------------------grid 1
    rth1 = curve(40, 150, 460, 600, radius=20, fill="#213b52")
    grd1=Label(canvas, text="PROFIT AND LOSS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(60, 160, anchor="nw", window=grd1)

    canvas.create_line(50, 195, 450, 195,fill="gray" )

    grd1_1=Label(canvas, text="NET INCOME: ₹ 0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(60, 230, anchor="nw", window=grd1_1)

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Income"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Expense"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(50, 285, anchor="nw", window=canvasbar.get_tk_widget())
    #----------------------------------------------------------------------------------------------------------------grid 2
    rth2 = curve(480, 150, 880, 600, radius=20, fill="#213b52")

    grd1=Label(canvas, text="EXPENSES: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(500, 160, anchor="nw", window=grd1)
    canvas.create_line(490, 195, 870, 195,fill="gray" )
    #----------------------------------------------------------------------------------------------------------------grid 3
    rth3 = curve(900, 150, 1300, 600, radius=20, fill="#213b52")

    grd1=Label(canvas, text="BANK ACCOUNTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(920, 160, anchor="nw", window=grd1)
    canvas.create_line(910, 195, 1290, 195,fill="gray" )
    #----------------------------------------------------------------------------------------------------------------grid 4
    rth4 = curve(40, 620, 460, 1070, radius=20, fill="#213b52")

    grd1=Label(canvas, text="INCOME: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(60, 640, anchor="nw", window=grd1)
    canvas.create_line(50, 675, 450, 675,fill="gray" )
    #----------------------------------------------------------------------------------------------------------------grid 5
    rth5 = curve(480, 620, 880, 1070, radius=20, fill="#213b52")
    grd1=Label(canvas, text="INVOICE",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(500, 640, anchor="nw", window=grd1)
    canvas.create_line(490, 675, 870, 675,fill="gray" )
    grd1=Label(canvas, text="UNPAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(500, 690, anchor="nw", window=grd1)
    grd1=Label(canvas, text="PAID:₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
    win_inv1 = canvas.create_window(500,720 , anchor="nw", window=grd1)

    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Unpaid"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    x="Paid"
    y=100
    plt.barh(x,y, color="red") 
    plt.legend()
 
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()
              

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(480, 780, anchor="nw", window=canvasbar.get_tk_widget())
    #----------------------------------------------------------------------------------------------------------------grid 6
    rth6 = curve(900, 620, 1300, 1070, radius=20, fill="#213b52")#-----------------------------grid 6
    grd1=Label(canvas, text="SALES: ₹ 0.0",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))

    win_inv1 = canvas.create_window(920, 640, anchor="nw", window=grd1)
    
    canvas.create_line(910, 675, 1290, 675,fill="gray" )
    figlast = plt.figure(figsize=(8, 4), dpi=50)

    x="Income"
    y=10 
    plt.barh(x,y, label="Undefined", color="blue") 
    plt.legend()
  
    plt.ylabel("")
    axes=plt.gca()
    axes.xaxis.grid()

    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
    canvasbar
    canvasbar.draw()
    canvasbar.get_tk_widget()
    win_inv1 = canvas.create_window(900, 780, anchor="nw", window=canvasbar.get_tk_widget())
    
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

    tab_bank = ttk.Notebook(tab2)
    tab2_1 =  ttk.Frame(tab_bank)
    tab2_2=  ttk.Frame(tab_bank)
    tab2_3 = ttk.Frame(tab_bank)

    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

    
    tab_bank.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
    tab_sales = ttk.Notebook(tab3)
    tab3_1 =  ttk.Frame(tab_sales)
    tab3_2=  ttk.Frame(tab_sales)
    tab3_3 = ttk.Frame(tab_sales)
    tab3_4=  ttk.Frame(tab_sales)

    
        
    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
 
    tab_sales.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
    tab_exp = ttk.Notebook(tab4)
    tab4_1 =  ttk.Frame(tab_exp)
    tab4_2=  ttk.Frame(tab_exp)
    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
    tab_exp.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
    tab_payroll = ttk.Notebook(tab5)
    tab5_1 =  ttk.Frame(tab_payroll)
    tab5_2=  ttk.Frame(tab_payroll)
     
    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

    tab_payroll.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

    tab_report = ttk.Notebook(tab6)
    tab6_1 =  ttk.Frame(tab_report)
    tab6_2=  ttk.Frame(tab_report)
    tab6_3 = ttk.Frame(tab_report)
    tab6_4=  ttk.Frame(tab_report)

    
        
    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
 
    tab_report.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

    tab_tax = ttk.Notebook(tab7)
    tab7_1 =  ttk.Frame(tab_tax)
    tab7_2=  ttk.Frame(tab_tax)

    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
    tab_tax.add(tab7_2,compound = LEFT, text ='New')

    tab_tax.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
    tab_account = ttk.Notebook(tab8)
    tab8_1 =  ttk.Frame(tab_account)
    tab8_2=  ttk.Frame(tab_account)

    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
   
 
    tab_account.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
    tab_cash = ttk.Notebook(tab10)
    
    tab10_1 =  ttk.Frame(tab_cash)
    tab10_2=  ttk.Frame(tab_cash)
    tab10_3 = ttk.Frame(tab_cash)

    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

    tab_cash.pack(expand = 1, fill ="both")
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)

#---------------------------------------------------------------------------------------------------------------Company Second Portion
def cmpny_crt2():
    main_frame_cmpny.pack_forget()
    global main_frame_cmpny2
    main_frame_cmpny2=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny2.pack(fill=X,)

    cmpny_dt_frm2=Frame(main_frame_cmpny2, height=650, width=500,bg="white")
    cmpny_dt_frm2.pack(pady=105)

    def name_ent2(event):
        if nm_nm2.get()=="Legal Business Name":
            nm_nm2.delete(0,END)
        else:
            pass


    cmpny_hd=Label(cmpny_dt_frm2, text="Let's Start Building Your FinsYs",font=('Calibri 30 bold'),bg="white", fg="black")
    cmpny_hd.pack(padx=100,pady=20)

    

    nm_nm2 = Entry(cmpny_dt_frm2, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm2.insert(0,"Legal Business Name")
    nm_nm2.bind("<Button-1>",name_ent2)
    nm_nm2.pack(padx=100,pady=15)

    cmp_lbl1=Label(cmpny_dt_frm2, text="Your Industry",font=('Calibri 12'),bg="white" ,fg="black")
    cmp_lbl1.place(x=180,y=143)

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    cmpny_cntry.pack(padx=100,pady=15)
    cmpny_cntry['values'] = ('Accounting Services','Consultants, doctors, Lawyers and similar','Information Tecnology','Manufacturing','Professional, Scientific and Technical Services','Restaurant/Bar and similar','Retail and Smilar','Other Finanacial Services')
    cmpny_cntry.current(0)

    cmp_lbl2=Label(cmpny_dt_frm2, text="Company type",font=('Calibri 12'),bg="white" ,fg="black")
    cmp_lbl2.place(x=180,y=205)

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    cmpny_cntry.pack(padx=100,pady=15)
    cmpny_cntry['values'] = ('Private Limited Company','Public Limited Company','Joint-Venture Company','Partnership Firm Company','One Person Company','Branch Office Company','Non Government Organization')
    cmpny_cntry.current(0)
    
    cmp_lbl3=Label(cmpny_dt_frm2, text="Do you have an Accountant, Bookkeeper or Tax Pro ?",font=('Calibri 12'),bg="white" ,fg="black")
    cmp_lbl3.place(x=180,y=267)

    bs_cus_ct=StringVar()
    r1=Radiobutton(cmpny_dt_frm2, text = "Yes", variable = bs_cus_ct, value ="Yes",font=('Calibri 16'),bg="white")
    r1.select()
    r1.pack(padx=100,pady=(20,10))

    r1=Radiobutton(cmpny_dt_frm2, text = "No", variable = bs_cus_ct, value ="No",font=('Calibri 16'),bg="white")
    r1.select()
    r1.pack(padx=100,pady=(0,20))


    cmp_lbl4=Label(cmpny_dt_frm2, text="How do you like to get paid?",font=('Calibri 12'),bg="white" ,fg="black")
    cmp_lbl4.place(x=180,y=391)
    
    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm2,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    cmpny_cntry.pack(padx=100,pady=(15,70))
    cmpny_cntry['values'] = ('Cash','Cheque','Credit card/Debit card','Bank Transfer','Paypal/Other service')
    cmpny_cntry.current(0)

    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=cmpny_crt1,text="Previous",bg="#213b52")
    button_cmp2.place(x=215,y=470)
    button_cmp2 = customtkinter.CTkButton(master=cmpny_dt_frm2,command=fun_sign_in,text="Submit",bg="#213b52")
    button_cmp2.place(x=360,y=470)
#-------------------------------------------------------------------------------------------------------------------company creation
def cmpny_crt1():
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    global main_frame_cmpny
    main_frame_cmpny=Frame(root, height=750,bg="#213b52")
    main_frame_cmpny.pack(fill=X,)

    cmpny_dt_frm=Frame(main_frame_cmpny, height=650, width=500,bg="white")
    cmpny_dt_frm.pack(pady=50)

    def name_ent(event):
        if nm_nm.get()=="Company Name":
            nm_nm.delete(0,END)
        else:
            pass

    def cmp_add(event):
        if cmp_cmpn.get()=="Company Address":
                cmp_cmpn.delete(0,END)
        else:
            pass
    def cty_ent(event):
        if cmp_cty.get()=="City":
            cmp_cty.delete(0,END)
        else:
            pass

    def em_ent(event):
        if cmp_email.get()=="Email":
                cmp_email.delete(0,END)
        else:
            pass
    def ph_ent(event):
        if cmp_ph.get()=="Phone Number":
            cmp_ph.delete(0,END)
        else:
            pass

    def fil_ent(event):
        
        cmp_logo = askopenfilename(filetypes=(("png file ",'.png'),('PDF', '*.pdf',),("jpg file", ".jpg"),  ("All files", "*.*"),))
        
        cmp_files.delete(0,END)
        cmp_files.insert(0,cmp_logo)
    

    cmpny_hd=Label(cmpny_dt_frm, text="We're Happy you're Here!",font=('Calibri 30 bold'),bg="white", fg="black")
    cmpny_hd.pack(padx=100,pady=20)

    nm_nm = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    nm_nm.insert(0,"Company Name")
    nm_nm.bind("<Button-1>",name_ent)
    nm_nm.pack(padx=100,pady=15)

    cmp_cmpn = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cmpn.insert(0,"Company Address")
    cmp_cmpn.bind("<Button-1>",cmp_add)
    cmp_cmpn.pack(padx=100,pady=15)

    cmp_cty = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_cty.insert(0,"City")
    cmp_cty.bind("<Button-1>",cty_ent)
    cmp_cty.pack(padx=100,pady=15)

    invset_bg_var = StringVar()
    cmpny_cntry = ttk.Combobox(cmpny_dt_frm,textvariable=invset_bg_var,width=29,font=('Calibri 16'))
    cmpny_cntry.pack(padx=100,pady=15)
    cmpny_cntry['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
    cmpny_cntry.current(0)

    cmp_pin = Spinbox(cmpny_dt_frm,from_=1,to=1000000,width=29, font=('Calibri 16'),borderwidth=2)
    cmp_pin.delete(0,END)
    cmp_pin.insert(0,"Pincode")
    cmp_pin.pack(padx=100,pady=15)
   

    cmp_email = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_email.insert(0,"Email")
    cmp_email.bind("<Button-1>",em_ent)
    cmp_email.pack(padx=100,pady=15)

    cmp_ph = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_ph.insert(0,"Phone Number")
    cmp_ph.bind("<Button-1>",ph_ent)
    cmp_ph.pack(padx=100,pady=15)

    cmp_files = Entry(cmpny_dt_frm, width=30, font=('Calibri 16'),borderwidth=2)
    cmp_files.insert(0,"No file Chosen")
    cmp_files.bind("<Button-1>",fil_ent)
    cmp_files.pack(padx=100,pady=15)

    button = customtkinter.CTkButton(master=cmpny_dt_frm,command=cmpny_crt2,text="Next",bg="#213b52")
    button.pack(padx=100,pady=10)
    
#--------------------------------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    
    try:
        main_frame_signup.pack_forget()
    except:
        pass
    try:
        main_frame_cmpny2.pack_forget()
    except:
        pass
    global main_frame_signin
    main_frame_signin=Frame(root, height=750)
    main_frame_signin.pack(fill=X,)

    sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=900, y=220)


    def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

    def sig_pass(event):
            if pass_ent.get()=="Password":
                pass_ent.delete(0,END)
            else:
                pass
    nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    nm_ent.insert(0,"Username")
    nm_ent.bind("<Button-1>",sig_nm)
    nm_ent.place(x=820,y=300)

    pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    pass_ent.insert(0,"Password")
    pass_ent.bind("<Button-1>",sig_pass)
    pass_ent.place(x=820,y=350)

    but_sign2 = customtkinter.CTkButton(master=main_frame_signin,command=lambda:main_sign_in(),text="Log In",bg="#213b52")
    but_sign2.place(relx=0.69, rely=0.58)

    #----------------------------------------------------------------------------------------left canvas
    lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
    lf_signup.place(x=-700,y=0)

    lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

    label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
    label.place(x=0,y=150)

    lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=250, y=40)
    lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=150, y=80)

    btn2 = Button(main_frame_signin, text = 'Sign Up', command=lambda:func_sign_up(), bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn2.place(x=275,y=130)


#---------------------------------------------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    
    global main_frame_signup
    main_frame_signin.pack_forget()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.place(x=500,y=0)

    lf_signup.create_oval(1400,1400,150,-1700,fill="#213b52")

    #--------------------------------------------------------------------------------sign up section
    sign_in=Label(main_frame_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=260, y=100)

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    fst_nm.place(x=200,y=200)

    lst_nm = Entry(main_frame_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    lst_nm.place(x=200,y=250)

    sys_em = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    sys_em.place(x=200,y=300)

    sys_usr = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    sys_usr.place(x=200,y=350)

    sys_pass = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    sys_pass.place(x=200,y=400)

    sys_cf = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    sys_cf.place(x=200,y=400)

    

    label = Label(main_frame_signup, image = sign_up,bg="#213b52", width=800,anchor="w")
    label.place(x=730,y=200)
    
    button_sign = customtkinter.CTkButton(master=main_frame_signup, command=cmpny_crt1,text="Sign Up",bg="#213b52")
    button_sign.place(relx=0.2, rely=0.7) 

    lft_lab=Label(main_frame_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=900, y=40)
    lft_lab=Label(main_frame_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=820, y=80)

    btn_signup = Button(main_frame_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn_signup.place(x=920,y=130)


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)

sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
sign_in.place(x=900, y=220)

def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass
nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
nm_ent.place(x=820,y=300)

pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
pass_ent.place(x=820,y=350)

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
button.place(relx=0.65, rely=0.58)

#------------------------------------------------------------------------------------------------------------------------left canvas
lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
lf_signup.place(x=-700,y=0)

lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
label.place(x=0,y=150)

lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
lft_lab.place(x=250, y=40)
lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
lft_lab.place(x=150, y=80)

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
btn2.place(x=275,y=130)

root.mainloop()