# coding:utf-8

import tkinter as tk

class Ball:
    def __init__(self,x,y,dx,dy,color):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.color=color

        
    def move(self,canvas):

        self.erase(canvas)
        
        self.x=self.x+self.dx
        self.y=self.y+self.dy

        self.draw(canvas)

        if self.x >= canvas.winfo_width():
            self.dx=-1
        if self.x <= 0:
            self.dx=+1

        if self.y >= canvas.winfo_height():
            self.dy=-1
        if self.y <= 0:
            self.dy = +1

    def erase(self,canvas):
            canvas.create_oval(self.x-20,self.y-20,self.x+20,self.y+20,fill="white",width=0)
    
    def draw(self,canvas):
        canvas.create_oval(self.x-20,self.y-20,self.x+20,self.y+20,fill=self.color,width=0)

class Rectangle(Ball):
    def erase(self,canvas):
        canvas.create_rectangle(self.x-20,self.y-20,self.x+20,self.y+20,fill="white",width=0)
    def draw(self,canvas):
        canvas.create_rectangle(self.x-20,self.y-20,self.x+20,self.y+20,fill=self.color,width=0)

class Triangle(Ball):
    def erase(self,canvas):
        canvas.create_polygon(self.x-20,self.y-20,self.x+20,self.y+20,self.x-20,self.y+20,fill="white",width=0)
    def draw(self,canvas):
        canvas.create_polygon(self.x-20,self.y-20,self.x+20,self.y+20,self.x-20,self.y+20,fill=self.color,width=0)
        

balls=[
    Ball(400,300,1,1,"red"),
    Rectangle(400,300,-1,1,"blue"),
    Triangle(400,300,1,-1,"green")
    ]



def loop():
    for b in balls:
        b.move(canvas)
        
    root.after(10,loop)
        

        

root=tk.Tk()

root.geometry("600x400")

canvas=tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0,y=0)

root.after(10,loop)

root.mainloop()

