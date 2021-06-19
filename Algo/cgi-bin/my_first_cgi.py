#!/usr/bin/env python
# coding: shift-jis

html_body = '''<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="shift-JIS">
        <title>CGI</title>
    </head>
    <body>
    はじめてのCGI
    </body>
</html>'''

print('Content-type: text/html')
print('')
print(html_body)