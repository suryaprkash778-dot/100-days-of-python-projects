logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def pro(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations={
    "+":add,
    "-":sub,
    "*":pro,
    "/":div
}

def calculator():
    print(logo)
    operation_in_progress = True
    num1 = float(input("What's the first number?:\n"))
    while operation_in_progress==True:
        op = input("+\n-\n*\n/\nPick an operation\n")
        num2 = float(input("What's the next number?\n"))
        answer=operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        yes_no=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
        if yes_no == "y":
            num1=answer
        else:
            operation_in_progress = False
            print("\n"*20)
            calculator()
            
calculator()

