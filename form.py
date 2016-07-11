#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
Your_name = form.getfirst("Name","unknown")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>What's your name pal?◉ _◉ </title>
        </head>
        <body>""")

print("<p>Hello, {}◉⥿◉ </p>".format(Your_name))


print("""</body>
        </html>""")
