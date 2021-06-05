#!/usr/bin/env python
# coding: shift-jis

import datetime
import cgi
import cgitb
cgitb.enable()

html_body = '''<html>
<head>
<meta charset="shift-JIN">
<title>�����̉^��</title>
</head>
<body>
{month}�����܂�̂��Ȃ��̍����̉^����{fortune}�ł��B
</body>
</html>'''

#�@URL�̃p�����[�^����Amonth���擾�B������^�Ȃ̂ŁA�����ɕϊ��B
param_data = cgi.FieldStorage()
month = int(param_data.getvalue('month'))
#�@datetime�𗘗p���āA���݂̓������擾�B
today = datetime.date.today()

contents = {}
contents['month'] = month
contents['fortune'] = ['��g','���g','�g','���g','��','�勥'][today.day * month % 6]

print('Content-type: text/html')
print('')
print(html_body.format(todays_fortune))