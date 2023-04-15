from random import randint
from tkinter import*
from score import*
import keyboard
import tkinter
import time

WINDOW = tkinter.Tk()
WINDOW_HEIGHT = 362
WINDOW_WIDTH = 400
WINDOW.title('Greetings!')
WINDOW.geometry('400x362')
WINDOW.config(bg='#000045')
#ive somewhat fixed the cookie clicker, im working on it as well
cover_picture = PhotoImage(file='cover_picture.png')
toilet_picture = PhotoImage(file='toilet_image4.0 (1).png')
plunger_picture = PhotoImage(file='plunger4.0.png')
clogged_toilet_picture = PhotoImage(file='clogged_toilet4.0.png')

def toilet_click():
  
  global clicks
  clicks += 1

  score_label = Label(text = clicks, font = ('Times New Roman', 45))
  score_label.config(bg = '#FFCC03')
  score_label.config(fg = '#000000')
  score_label.pack() 
  score_label.place(x=270, y=15) 
def cover_name_clear(e):
  if cover_input.get() == 'Name':
    cover_input.delete(0, END)
def rank_click():
  plunger_label.destroy()
  toilet.destroy()
  rank_button.destroy()

  highscore_background = Label(WINDOW, image = clogged_toilet_picture)
  highscore_background.pack()
  
  WINDOW.title('High Scores')
  WINDOW.config(bg = '#FFFFFF')
  if get_highscore():
    highscore_label1 = Label(WINDOW, text = get_highscore())
    highscore_label1.config(bg = '#000000')
    highscore_label1.config(fg = '#FFFFFF')
    highscore_label1.pack()
    highscore_label1.place(x=150,y=15)
    
  else:
    highscore_label2 = Label(WINDOW, text = 'You are the first to play!', font = ('Times New Roman', 25))
    highscore_label2.config(bg = '#000000')
    highscore_label2.config(fg = '#FFFFFF')
    highscore_label2.pack()
    highscore_label2.place(x=90,y=15)
def start():
  start_button.destroy()
  cover_image.destroy()
  cover_input.destroy()
  greeting_label.destroy()
  cover_bg_size.destroy()
  
  WINDOW_HEIGHT = 600
  WINDOW_WIDTH = 600
  
  toilet.place(x=400, y=300)
  plunger_label.place(x=randint(0, WINDOW_HEIGHT), y=randint(0, WINDOW_WIDTH))
  rank_button.place(x=460, y=10)

  WINDOW.geometry('600x600')
  WINDOW.title('PLUNGE AWAY!')
  WINDOW.config(bg='#FFCC03')

  fake_label = Label(WINDOW, text = clicks, font = ('Times New Roman', 45))
  fake_label.config(bg = '#FFCC03')
  fake_label.config(fg = '#000000')
  fake_label.pack()
  fake_label.place(x=270, y=15)
while True:
  try:
    if keyboard.is_pressed('w'):
      plunger_label.place(x=1000,y=1000)
      break
    elif keyboard.is_pressed('a'):
      plunger_label.place(x=200,y=200)
      break
    elif keyboard.is_pressed('s'):
      plunger_label.place(x=100,y=100)
      break
    elif keyboard.is_pressed('d'):
      plunger_label.place(x=300,y=300)
      break
  except:
      break
cover_image = Label(WINDOW, image=cover_picture)
cover_image.config(bg='#000045')
cover_image.pack()

cover_bg_size = Canvas(WINDOW, height=WINDOW_HEIGHT, width=WINDOW_HEIGHT)
cover_bg_size.config(bg='#000045')
cover_bg_size.pack()

cover_input = tkinter.Entry(WINDOW, width=25)
cover_input.config(bg='#000045')
cover_input.config(fg='#FFFFFF')
cover_input.pack()
cover_input.place(x=100, y=50)
cover_input.insert(0, 'Name')
cover_input.bind('<Button-1>', cover_name_clear)

greeting_label = Label(WINDOW, text='Please Enter Your Name.', font=('Times New Roman', 20))
greeting_label.config(bg='#000045')
greeting_label.config(fg='#FFFFFF')
greeting_label.pack()
greeting_label.place(x=30, y=8)

start_button = Button(WINDOW, text='Start', font=('Times New Roman', 20))
start_button.config(bg='#00FF00')
start_button.config(fg='#FFFFFF')
start_button.config(activebackground='#009900')
start_button.config(activeforeground='#999999')
start_button.config(command=start)
start_button.pack()
start_button.place(x=152, y=240)

toilet = Button(WINDOW, image=toilet_picture)
toilet.config(bg='#FFCC03')
toilet.config(activebackground = '#99CC02')
toilet.config(command = toilet_click)
toilet.pack()
toilet.place(x=1000, y=1000)

plunger_label = Label(WINDOW, image=plunger_picture)
plunger_label.config(bg='#FFCC03')
plunger_label.pack()

rank_button = Button(WINDOW, text='Ranks', font=('Times New Roman', 25))
rank_button.config(bg='#FF0000')
rank_button.config(activebackground='#990000')
rank_button.config(command=rank_click)
rank_button.pack()

clicks = 0

#wont work!? dont know why? maybe for console now output window?
#plunger_label is suppossed to teleport a little to the direction of the key NOT THE CURRENT PLACEMENT.

WINDOW.mainloop()
