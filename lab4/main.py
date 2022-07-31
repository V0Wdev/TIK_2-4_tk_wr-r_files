import math
import random
from tkinter import *

window = Tk()
window.geometry("1000x700")
window.title("Lab4")

sq_mat = []
pa = []
pb = []
pa_b = []
pb_a = []


def calc():
    h_a = 0
    h_b = 0
    h_ab = 0
    h_a_b = 0
    h_b_a = 0

    # Расчёт  и вывод вероятности р(а)
    for i in range(13):
        label = Label(window, text=" {:.3f}".format(sum(sq_mat[i])))
        pa.append(sum(sq_mat[i]))
        label.grid(column=13, row=i, padx=30)
    label_sum_h = Label(window, text="сумма")
    label_sum_h.grid(row=14, column=6)
    label_sum_v = Label(window, text="сумма")
    label_sum_v.grid(row=14, column=13)

    # Расчёт и вывод вероятности р(b)
    for i in range(13):
        temp = 0
        for j in range(13):
            temp += sq_mat[j][i]
        pb.append(temp)
        label_b = Label(window, text="{:.3f}".format(pb[i]))
        label_b.grid(row=15, column=i)

    # Расчёт вероятностей р(а/b) и р(b/а)
    for i in range(13):
        temp_a = []
        temp_b = []
        for j in range(13):
            temp_a.append(sq_mat[i][j] / pa[i])
            temp_b.append(sq_mat[i][j] / pb[i])
        pa_b.append(temp_a)
        pb_a.append(temp_b)
    label_sum = Label(window, text="p(a/b)\t\t\t\t\t\t\t\t\t\t\t\tp(b/a)")
    label_sum.grid(row=16, columnspan=26)

    # Вывод вероятностей
    for i in range(13):
        for j in range(13):
            label = Label(window, text="{:.3f}".format(pa_b[i][j]))
            label_b = Label(window, text="{:.3f}".format(pb_a[i][j]))
            label.grid(row=17 + i, column=j)
            label_b.grid(row=17 + i, column=j + 14)

    # Расчёт энтропий
    for i in range(13):
        h_a += - pa[i] * math.log2(pa[i])
        h_b += - pb[i] * math.log2(pb[i])
        for j in range(13):
            h_ab += -sq_mat[i][j] * math.log2(sq_mat[i][j])
            h_b_a += - sq_mat[i][j] * math.log2(pa_b[i][j])
            h_a_b += - sq_mat[i][j] * math.log2(pb_a[i][j])

    # Расчет пропускной способности
    c_a = (h_a * h_a_b) / 5
    c_b = (h_b * h_b_a) / 5

    # Расчет передачи информации
    i_ab = 0
    for i in range(13):
        for j in range(13):
            i_ab += -sq_mat[i][j] * math.log2(sq_mat[i][j])

    # Вывод энтропий
    label = Label(window, text="H(A)")
    label_res = Label(window, text="{:.3f}".format(h_a))
    label.grid(row=10, column=16)
    label_res.grid(row=10, column=17)

    label = Label(window, text="H(B)")
    label_res = Label(window, text="{:.3f}".format(h_b))
    label.grid(row=11, column=16)
    label_res.grid(row=11, column=17)

    label = Label(window, text="I(A,B)")
    label_res = Label(window, text="{:.3f}".format(i_ab))
    label.grid(row=12, column=16)
    label_res.grid(row=12, column=17)

    label = Label(window, text="H(A/B)")
    label_res = Label(window, text="{:.3f}".format(h_a_b))
    label.grid(row=13, column=16)
    label_res.grid(row=13, column=17)

    label = Label(window, text="H(B/A)")
    label_res = Label(window, text="{:.3f}".format(h_b_a))
    label.grid(row=14, column=16)
    label_res.grid(row=14, column=17)

    label = Label(window, text="C(A):")
    label_res = Label(window, text="{:.3f}".format(c_a))
    label.grid(row=8, column=16)
    label_res.grid(row=8, column=17)

    label = Label(window, text="C(B):")
    label_res = Label(window, text="{:.3f}".format(c_b))
    label.grid(row=9, column=16)
    label_res.grid(row=9, column=17)

    sq_mat.clear()
    pa.clear()
    pb.clear()
    pa_b.clear()
    pb_a.clear()


# Генерация массива
def gen():
    m = 1
    for i in range(13):
        temp = []
        for j in range(13):
            temp.append(random.uniform(0, m / 30))
            m -= temp[j]
        sq_mat.append(temp)
    for i in range(13):
        for j in range(13):
            label = Label(window, text="{:.3f}".format(sq_mat[i][j]))
            label.grid(column=j, row=i)


button_gen = Button(window, text="Генерировать массив", font=('Tahoma', 12), fg="black", bd=0, bg="purple", comman=gen)
button_gen.place(x=550, y=0)
button_math = Button(window, text="Посчитать энтропию", font=('Tahoma', 12), fg="black", bd=0, bg="purple", comman=calc)
button_math.place(x=550, y=30)

window.mainloop()