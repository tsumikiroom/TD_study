#config:utf-8
import random

a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9)]
print(str(a[0])+str(a[1])+str(a[2])+str(a[3]))

while True:
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
    print("hit"+str(hit))
    print("blow"+str(blow))

    if hit==4:
        print("True!")
        break
                                     
