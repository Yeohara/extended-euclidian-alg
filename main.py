from tkinter import *
from model import *

window = Tk()
window.title("Расширенный алгоритм Евклида и возведение в степень по модулю")
window.geometry("430x330")
window.resizable(0, 0)

def euclidian():
    output_gcd.delete(0, END)
    output_smoll.delete(0, END)
    output_big.delete(0, END)
    A = int(input_A.get())
    B = int(input_B.get())
    gcd, Y, X = eea(A, B)
    if A > B:
        output_gcd.insert(END, gcd)
        output_smoll.insert(END, Y)
        output_big.insert(END, X)
    else:
        output_gcd.insert(END, gcd)
        output_smoll.insert(END, X)
        output_big.insert(END, Y)

def fp():
    output_fp.delete(0, END)
    a = int(input_a_fp.get())
    b = int(input_b_fp.get())
    n = int(input_n_fp.get())
    res = fast_power(a, b, n)
    output_fp.insert(END, res)


label = Label(window, text="Расширенный алгоритм Евклида").place(x=120, y=10)

label = Label(window, text="Введите А")
label.place(x=70, y=40)
input_A = Entry(window, width=20)
input_A.place(x=40, y=60)

label = Label(window, text="Введите B")
label.place(x=310, y=40)
input_B = Entry(window, width=20)
input_B.place(x=280, y=60)

button_eea = Button(window, text="Вычислить", width=10, command=euclidian).place(x=184, y=90)

label = Label(window, text="НОД").place(x=206, y=120)
output_gcd = Entry(window, width=16)
output_gcd.place(x=174, y=140)

label = Label(window, text="Коэф-т перед меньшим числом").place(x=6, y=160)
output_big = Entry(window, width=20)
output_big.place(x=40, y=180)

label = Label(window, text="Коэф-т перед большим числом").place(x=236, y=160)
output_smoll = Entry(window, width=20)
output_smoll.place(x=280, y=180)

label = Label(window, text="Быстрое возведение в степень по модулю").place(x=120, y=210)

label = Label(window, text="a = ").place(x=18, y=238)
input_a_fp = Entry(window, width=20)
input_a_fp.place(x=40, y=240)

label = Label(window, text="b = ").place(x=18, y=268)
input_b_fp = Entry(window, width=20)
input_b_fp.place(x=40, y=270)

label = Label(window, text="n = ").place(x=18, y=298)
input_n_fp = Entry(window, width=20)
input_n_fp.place(x=40, y=300)

label_= Label(window, text="aᵇ mod n").place(x=196, y=248)
button_fp = Button(window, text="Вычислить", width=10, command=fp).place(x=184, y=268)

label = Label(window, text="Результат").place(x=314, y=250)
output_fp = Entry(window, width=20)
output_fp.place(x=280, y=270)

window.mainloop()
