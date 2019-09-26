# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:44:45 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import tkinter as tk

# import full dataset 
data_all_raw = pd.read_csv('./data/listings/data_all.csv')


### TKINTER DEMO ###

# create window with button
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 

# create canvas area for graphics
master = tk.Tk() 
w = tk.Canvas(master, width=400, height=600) 
w.pack() 
canvas_height=100
canvas_width=200
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
tk.mainloop() 

# create check boxes
master = tk.Tk() 
var1 = tk.IntVar() 
tk.Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=tk.W) 
var2 = tk.IntVar() 
tk.Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=tk.W) 
tk.mainloop() 

# create radio buttons
root = tk.Tk() 
v = tk.IntVar() 
tk.Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=tk.W) 
tk.Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=tk.W) 
tk.mainloop() 

# create slider bar
master = tk.Tk() 
w = tk.Scale(master, from_=0, to=42) 
w.pack() 
w = tk.Scale(master, from_=0, to=200, orient=tk.HORIZONTAL) 
w.pack() 
tk.mainloop() 

# create window with organized buttons
root = tk.Tk() 
frame = tk.Frame(root) 
frame.pack() 
bottomframe = frame
bottomframe.pack(side = tk.BOTTOM ) 
redbutton = tk.Button(frame, text = 'Red', fg ='red') 
redbutton.pack(side = tk.LEFT) 
greenbutton = tk.Button(frame, text = 'Brown', fg='brown') 
greenbutton.pack(side = tk.LEFT ) 
bluebutton = tk.Button(frame, text ='Blue', fg ='blue') 
bluebutton.pack(side = tk.LEFT ) 
blackbutton = tk.Button(bottomframe, text ='Black', fg ='black') 
blackbutton.pack(side = tk.BOTTOM) 
root.mainloop() 

# create spinbox
master = tk.Tk() 
master.geometry("200x100")
w = tk.Spinbox(master, from_ = 0, to = 10) 
w.pack() 
tk.mainloop() 

# get style theme names
from tkinter import ttk
s = ttk.Style()
s.theme_names()

# create window with desired style
root = tk.Tk() 
root.style = ttk.Style()
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
root.style.theme_use("clam")
v = tk.IntVar() 
ttk.Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=tk.W) 
ttk.Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=tk.W) 
tk.mainloop() 