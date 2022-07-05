import tkinter
import math

canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

x0,y0=150,150
n=15
for uhol in range(0,360,360//n):
    x1 = x0 + 100*math.cos(math.radians(uhol))
    y1 = y0 + 100*math.sin(math.radians(uhol))
    x2 = x0 + 100*math.cos(math.radians(uhol+360//n))
    y2 = y0 + 100*math.sin(math.radians(uhol+360//n))
    canvas.create_line(x1,y1,x2,y2)

for uhol in range(0,360,360//n):
    x1 = x0 + 60*math.cos(math.radians(uhol))
    y1 = y0 + 60*math.sin(math.radians(uhol))
    x2 = x0 + 60*math.cos(math.radians(uhol+360//n))
    y2 = y0 + 60*math.sin(math.radians(uhol+360//n))
    canvas.create_line(x1,y1,x2,y2)

for uhol in range(0,360,360//n):
    x1 = x0 + 60*math.cos(math.radians(uhol))
    y1 = y0 + 60*math.sin(math.radians(uhol))
    x2 = x0 + 100*math.cos(math.radians(uhol))
    y2 = y0 + 100*math.sin(math.radians(uhol))
    canvas.create_line(x1,y1,x2,y2)

canvas.create_text(60,300,text=f'uhol skosenia je {(180-360//n)//2}°')
canvas.create_text(60,330,text=f'dĺžka prepony je {180//(math.sin(math.radians(80)))}')
canvas.create_text(60,360,text=f'dĺžka odvesny je {180//(math.tan(math.radians(80)))}')


tkinter.mainloop()