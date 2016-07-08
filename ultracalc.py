print("Welcome friend! You can use this tool, for calculations, invoke the spirits, and other stuff. Enjoy")
print("2 + 2 format")
#FUNCTIONS!

def add(n1, n2): return n1 + n2


def mult(n1, n2): return n1 * n2


def sub(n1, n2): return n1 - n2        #summons Sub-Zero


def dev(n1, n2): return n1 / n2
# Dictionary
opers = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": dev
}
while True:                                   #Loop for endless calculations
    expr = input('>')
    if expr:
        try:
            (oper1, oper, oper2) = expr.split(' ')
            print(opers[oper](int(oper1), int(oper2)))
        except Exception:
            print("Lol what?") #Protection from knights of 'Devided Zero Order'
    else:
        break #Breaks all doors in area, and exits the program

