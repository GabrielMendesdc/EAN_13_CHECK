x=0
from tkinter import *
import sys

def on_key_pressing(event, entry, label):
    ean = entry.get()
    init(ean)

    
class PrintToT1(object):
    def write(self, s):
        t1.insert(END, s)
        t1.tag_add("center", "1.0", "end")
        
        
root = Tk()
root.geometry('1220x500')
root.minsize(1220, 500)
root.config(bg='pink')
root.title("Ean13 Checker")
# root.attributes('-fullscreen', True)
root.resizable(True, True)
entry = Entry(root)
entry.pack(side="top")
entry.bind("<Return>", lambda e: on_key_pressing(e, entry, root))
t1 = Text(root, bg='black', fg='white')
t1.tag_configure("center", justify='center')
t1.config(font=("Courier", 40))
t1.pack(expand=True, fill='both')
sys.stdout = PrintToT1()

def dv(ean):
    ean = str(ean)
    sum1,sum3,soma,eanNovo = 0,0,0,''
    if len(ean) % 2 == 0:
        for i in range(len(ean)):
            if i % 2 == 0:
                sum1 += int(ean[i])
            else:
                sum3 += (int(ean[i]) * 3)
    else:
        for i in range(len(ean)):
            if i % 2 != 0:
                sum1 += int(ean[i])
            else:
                sum3 += (int(ean[i]) * 3)
    eanAux = ean[0:13]
    dig = (((sum1+sum3) // 10)*10+10) - (sum1+sum3)
    if dig == 10:
        dig = 0
    eanNovo = eanAux + str(dig)
    return eanNovo


def checa(ean):
    ean = str(ean)
    if len(ean) == 14:
        ean = ean[1:13]
        eanNovo = dv(ean)
    elif len(ean) == 13:
        ean = ean[0:13]
        eanNovo  = dv(ean)
    else:
        eanNovo = dv(ean)
    return eanNovo


def init(ean):
    global x
    if not x > 6:
        print(f'Dígito Verificador: {checa(ean)[-1]}')
        print(f'Ean: {checa(ean)}')
    x+=1

        
root.mainloop()
