#!/usr/bin/env python
# coding: shift-jis

import datetime
import cgi
import cgitb
cgitb.enable()

html_body = '''<html>
<head>
<meta charset="shift-JIN"/>
<title>今日の運勢</title>
</head>
<body>
{month}月生まれのあなたの今日の運勢は{fortune}です。
</body>
</html>'''

#　URLのパラメータから、monthを取得。文字列型なので、整数に変換。
param_data = cgi.FieldStorage()
month = int(param_data.getvalue('month'))
#　datetimeを利用して、現在の日時を取得。
today = datetime.date.today()

contents = {}
contents['month'] = month
contents['fortune'] = ['大吉','中吉','吉','末吉','凶','大凶'][today.day * month % 6]

print('Content-type: text/html')
print('')
print(html_body.format(**contents))