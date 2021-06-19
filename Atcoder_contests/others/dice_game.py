import dice

num = input('4,6,8,12,20のどれで勝負しますか？：') #input関数で値を受け取る
num = int(num)              #文字列を整数に変換
my_dice = dice.Dice(num)    #ユーザー用のサイコロ
cpu_dice = dice.Dice(num)   #コンピュータ用のサイコロ

my_pip = my_dice.shoot()    #pipはサイコロの目の意味
cpu_pip = cpu_dice.shoot()  #コンピュータの出た目

#出た目を画面に出力　数字はstr関数を用いて文字列に変更
print('cpu:{} / あなた:{}'.format(cpu_pip,my_pip))
#状況によってメッセージを変える
if my_pip > cpu_pip:
    print('おめでとうございます。あなたの勝ちです！')
elif my_pip < cpu_pip:
    print('残念！あなたの負けです。')
else:
    print('引き分けです')