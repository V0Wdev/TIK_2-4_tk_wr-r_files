import math
from tkinter import *
from tkinter import ttk, Text

window = Tk()
window.geometry("800x600")
window.title("Lab3")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
notebook.add(tab1, text="")
tab2 = Frame(notebook)
notebook.add(tab2, text="")
tab3 = Frame(notebook)
notebook.add(tab3, text="")
notebook.pack(expand=TRUE, fill="both")
mes2 = Label(tab2, text="Сообщение", font=('Tahoma', 14))
mes2.place(x=10, y=30)
alp2 = Label(tab2, text="Алфавит с вероятностями и кодами", font=('Tahoma', 14))
alp2.place(x=310, y=30)
text_in2 = Text(tab2, bg='white', font=('Tahoma', 9))
text_in2.place(x=10, y=70, height=200, width=280)
text_out2 = Text(tab2, bg="white", font=('Tahoma', 9))
text_out2.place(x=310, y=70, height=400, width=480)
dec_text2 = Text(tab2, bg='white', font=('Tahoma', 9))
dec_text2.place(x=10, y=320, height=200, width=280)

mes3 = Label(tab3, text="Сообщение", font=('Tahoma', 14))
mes3.place(x=10, y=30)
alp3 = Label(tab3, text="Алфавит с вероятностями и кодами", font=('Tahoma', 14))
alp3.place(x=310, y=30)
text_in3 = Text(tab3, bg='white', font=('Tahoma', 9))
text_in3.place(x=10, y=70, height=200, width=280)
text_out3 = Text(tab3, bg="white", font=('Tahoma', 9))
text_out3.place(x=310, y=70, height=400, width=480)
dec_text3 = Text(tab3, bg='white', font=('Tahoma', 9))
dec_text3.place(x=10, y=320, height=200, width=280)
probability = []
v = {}
dict = []
cod_mes = []
cod_dict = {}

with open('message.txt') as file:
    text_in2.insert(1.0, file.read())
    file.close()


def find(texts: str, letter: str) -> int:
    count = texts.count(letter, 0, len(texts))
    return count


def click2():
    a = text_in2.get("1.0", END)
    sl_n_count = 0
    v.clear()
    dict.clear()
    cod_mes.clear()
    probability.clear()
    t_out = ""
    text_out2.delete(1.0, END)
    dec_text2.delete(1.0, END)
    for let in a:
        if dict.count(let) < 1:
            if let != "\n":
                dict.append(let)
            else:
                sl_n_count += 1
    for fin in range(len(dict)):
        temp = find(a, dict[fin]) / (len(a) - sl_n_count)
        probability.append(temp)
        v.update({dict[fin]: temp})
    v_sort = list(v.items())
    v_sort.sort(key=lambda i: i[1], reverse=TRUE)
    probability.sort(reverse=TRUE)
    for i in range(len(probability)):
        cod_mes.append('')
    coding(0, len(probability) - 1)
    m = 0
    for i in v_sort:
        t_out += i[0] + "\t|\t" + str(i[1]) + "\t\t" + str(cod_mes[m]) + "\n"
        cod_dict.update({i[0]: cod_mes[m]})
        m = m + 1
    text_out2.insert(1.0, t_out)
    temp_mes = ""
    for i in range(len(a) - 1):
        temp_mes += cod_dict.get(a[i])
    dec_text2.insert(1.0, temp_mes)
    with open('config.txt', 'w') as file:
        for i, j in cod_dict.items():
            file.write(str(i) + "\n" + str(j) + "\n")
        file.close()


def coding(l, r):
    n = 0
    if l < r:
        n = div_array(l, r)
        for i in range(l, r + 1):
            if i <= n:
                cod_mes[i] += '1'
            else:
                cod_mes[i] += '0'
        coding(l, n)
        coding(n + 1, r)




def div_array(l, r):
    sum1 = 0
    for i in range(l, r + 1):
        sum1 = sum1 + probability[i]
    sum2 = probability[r]
    m = r
    while sum2 <= sum1:
        m = m - 1
        sum1 = sum1 - probability[m]
        sum2 = sum2 + probability[m]
    return m


def click3():
    cod_dict.clear()
    result = ""
    with open("code.txt") as file:
        dec_text = file.read()
        dec_text3.insert(1.0, dec_text)
        file.close()
    with open('config.txt') as file:
        while TRUE:
            line = file.readline()
            line1 = line.split("\n")
            line = file.readline()
            line2 = line.split("\n")
            if not line:
                break
            cod_dict.update({line1[0]: line2[0]})
        file.close()
    while dec_text != '':
        if dec_text == "\n":
            break
        for key, value in cod_dict.items():
            temp = dec_text.partition(value)
            if temp[0] == '':
                result += key
                dec_text = temp[2]
            else:
                if temp[0] == "\n":
                    break
                continue
    text_in3.insert(1.0, result)
    a = text_in3.get("1.0", END)
    sl_n_count = 0
    v.clear()
    dict.clear()
    cod_mes.clear()
    probability.clear()
    t_out = ""
    text_out3.delete(1.0, END)
    for let in a:
        if dict.count(let) < 1:
            if let != "\n":
                dict.append(let)
            else:
                sl_n_count += 1
    for fin in range(len(dict)):
        temp = find(a, dict[fin]) / (len(a) - sl_n_count)
        probability.append(temp)
        v.update({dict[fin]: temp})
    v_sort = list(v.items())
    v_sort.sort(key=lambda i: i[1], reverse=TRUE)
    probability.sort(reverse=TRUE)
    for i in range(len(probability)):
        cod_mes.append('')
    coding(0, len(probability) - 1)
    m = 0
    for i in v_sort:
        t_out += i[0] + "\t|\t" + str(i[1]) + "\t\t" + str(cod_mes[m]) + "\n"
        cod_dict.update({i[0]: cod_mes[m]})
        m = m + 1
    text_out3.insert(1.0, t_out)


prob1 = [1/26]*26
prob2 = []
for i in range(1, 27):
    prob2.append(math.pow(0.5, i))
entropy1 = 0
entropy2 = 0
for i in range(26):
    entropy1 -= math.log(prob1[i], 2)/26
    entropy2 -= prob2[i]*math.log(prob2[i], 2)
Hmax = math.log(len(prob2), 2)
T1 = 0
T2 = 0
prob1.clear()
prob1 = [1/16]*16
for i in range(16):
    T1 += (i+1)*prob1[i]
    T2 += (i+1)*prob2[i]
H = Hmax-entropy2
speed1 = Hmax/T1
speed2 = Hmax/T2
label1 = Label(tab1, text="Количество информации на символ\nКоличество символов в алфавите = 26", font=('Tahoma', 14))
label1.place(x=220, y=30)
label2 = Label(tab1, text="Вероятности появления символов\n равны", font=('Tahoma', 11))
label2.place(x=100, y=120)
labelH = Label(tab1, text="{:.3f}".format(entropy1), font=('Tahoma', 20))
labelH.place(x=170, y=180)
label3 = Label(tab1, text="Когда вероятность каждого\n последующего символа вдважды меньше", font=('Tahoma', 11))
label3.place(x=400, y=120)
labelSH = Label(tab1, text="{:.3f}".format(entropy2), font=('Tahoma', 20))
labelSH.place(x=550, y=180)
labelSp1 = Label(tab1, text="Скорость передачи информации", font=('Tahoma', 14))
labelSp1.place(x=250, y=280)
labelSp2 = Label(tab1, text="{:.4f}".format(speed1), font=('Tahoma', 14))
labelSp2.place(x=200, y=330)
labelUn = Label(tab1, text="{:.4f}".format(speed2), font=('Tahoma', 14))
labelUn.place(x=500, y=330)
labelUn = Label(tab1, text="Недогруженность", font=('Tahoma', 14))
labelUn.place(x=300, y=380)
labelUn = Label(tab1, text="{:.3f}".format(H), font=('Tahoma', 14))
labelUn.place(x=350, y=430)


click2()
click3()
with open('code.txt', 'w') as file:
    file.write(dec_text2.get(1.0, END))
    file.close()
window.mainloop()