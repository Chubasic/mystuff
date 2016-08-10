#!/usr/bin/env python3
from decimal import Decimal
import cgi


def add(n1, n2): return n1 + n2


def mult(n1, n2): return n1 * n2


def sub(n1, n2): return n1 - n2        #summons Sub-Zero


def dev(n1, n2): return n1 / n2

# Dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": dev
}

form = cgi.FieldStorage()
first_Number = form['number1'].value
operator = form['operator'].value
second_Number = form['number2'].value

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")
try:
	result = operations[operator](Decimal(first_Number), Decimal(second_Number))
	print("<h1>{0} {1} {2} = {3}</h1>".
		format(first_Number, operator, second_Number, result))
except Exception:
	print("<h1>Error: division by zero</h1>")
print("""</body>
        </html>""")
