while True:

    height=input('身長(cm)?:')
    
    #入力は文字列なので、少数に変換します
    try:
        height=float(height)
    except:
        print('Error! 半角数字で入力してね！')
        break

    height=height / 100
    height=float(height)
    
    try:
        weight=float(input('体重(kg)?:'))
    except:
        print('Error! 半角数字で入力してね！')
        break

    #組み込み関数powで累乗を計算できます
    bmi=weight/pow(height,2)
    

    #小数点以下第一位までの出力にフォーマットしています
    print('BMI値は{:.1f}です。'.format(bmi))
    if bmi<18.5:
        print('すこしやせすぎです。')
    elif 18.5<=bmi<25.0:
        print('標準的な体型です。')
    elif 25.0<=bmi<30.0:
        print('少し太っています。')
    else:
        print('高度の肥満です。')