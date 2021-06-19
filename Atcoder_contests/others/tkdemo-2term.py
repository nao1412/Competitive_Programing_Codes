import tkinter as tk

# 計算機能のための変数とイベント用の関数定義

# 2項演算のモデル
# 入力中の数字
current_number = 0
# 第一項
first_term = 0
# 第二項
second_term = 0
# memo
memo = 0
# 結果
result = 0

def do_plus():
    "+ キーが押された時の計算動作、第一項の設定と入力中の数字クリア"
    global current_number
    global first_term
    global memo

    first_term = current_number
    memo += first_term
    current_number = 0

def do_minus():
    global current_number
    global first_term
    global memo

    first_term = current_number
    memo -= first_term
    current_number = 0

    

def do_eq():
    "= キーが押された時の計算動作、第二項のせてい、加算の実施、入力中の数字クリア"

    global second_term
    global result
    global current_number
    global memo
    
    result = memo + current_number  # 足し算以外もできるように
    current_number = 0

# 数字キーの Call Back 関数
def key1():
    key(1)

def key2():
    key(2)

def key3():
    key(3)

def key4():
    key(4)

def key5():
    key(5)

def key6():
    key(6)

def key7():
    key(7)

def key8():
    key(8)

def key9():
    key(9)

def key0():
    key(0)

# 数字キーを一括処理する関数
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():
    global memo
    memo = 0
    show_number(memo)

def plus():
    do_plus()
    show_number(memo)

def minus():
    do_minus()
    show_number(memo)

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0, tk.END)
    e.insert(0, str(num))

# tkinter での画面の構成

root = tk.Tk()
f = tk.Frame(root, bg ='#ffffc0')
f.grid()

# ウィジェットの作成
b1 = tk.Button(f, text='1', command=key1, font=('Helvetica', 14), width=2, bg ='#ffffff')
b2 = tk.Button(f, text='2', command=key2, font=('Helvetica', 14), width=2, bg ='#ffffff')
b3 = tk.Button(f, text='3', command=key3, font=('Helvetica', 14), width=2, bg ='#ffffff')
b4 = tk.Button(f, text='4', command=key4, font=('Helvetica', 14), width=2, bg ='#ffffff')
b5 = tk.Button(f, text='5', command=key5, font=('Helvetica', 14), width=2, bg ='#ffffff')
b6 = tk.Button(f, text='6', command=key6, font=('Helvetica', 14), width=2, bg ='#ffffff')
b7 = tk.Button(f, text='7', command=key7, font=('Helvetica', 14), width=2, bg ='#ffffff')
b8 = tk.Button(f, text='8', command=key8, font=('Helvetica', 14), width=2, bg ='#ffffff')
b9 = tk.Button(f, text='9', command=key9, font=('Helvetica', 14), width=2, bg ='#ffffff')
b0 = tk.Button(f, text='0', command=key0, font=('Helvetica', 14), width=2, bg ='#ffffff')
bc = tk.Button(f, text='C', command=clear, font=('Helvetica', 14), width=2, bg ='#ff0000')
bp = tk.Button(f, text='+', command=plus, font=('Helvetica', 14), width=2, bg ='#00ff00')
bm = tk.Button(f, text='-', command=minus, font=('Helvetica', 14), width=2, bg ='#00ff00')
be = tk.Button(f, text='=', command= eq, font=('Helvetica', 14), width=2, bg ='#00ff00')

# Grid型ジオメトリマネージャによるウィジェットの割り付け


b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
bc.grid(row=1, column=3)
be.grid(row=4, column=3)
bp.grid(row=2, column=3)
bm.grid(row=3, column=3)


# 数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0, column=0, columnspan=4)
clear()

# ここからGUIがスタート
root.mainloop()
