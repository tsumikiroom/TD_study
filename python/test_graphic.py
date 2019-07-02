import random
import tkinter as tk
import tkinter.messagebox as tmsg

def ButtonClick():
    b=editbox1.get()

    isok=False
    while isok==False:
        b=input("すうじをいれてね＞＞")
        if len(b) !=4:
            print("4桁の数字をいれてね")
        else:
            kazuok=True
            for i in range(4):
                if(b[i]<"0")or(b[i]>"9"):
                    print("すうじじゃないよー")
                    kazuok=False
                    break
            if kazuok==True:
                isok=True

    hit=0
    for i in range(4):
        if a[i]==int(b[i]):
            hit=hit+1

    blow=0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
              blow = blow + 1
              break


    if hit==4:
        tmsg.showinfo("あたり！","あたりです！おめでとうございます！！")
        root.destroy()

    else:
        tmsg.showinfo("いきるヒント","ヒット"+str(hit)+"/"+"ブロー"+str(blow))
        

a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9)]

    
root=tk.Tk()
root.geometry("400x150")
root.title("すうじあてげーむ")

label1=tk.Label(root,text="すうじをいれてね",font=("Helvetica",14))
label1.place(x=20,y=20)

editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)

button1=tk.Button(root,text="チェック",font=("Helvetica",14),command=ButtonClick)
button1.place(x=220,y=60)


    
root.mainloop()
