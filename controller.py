import logger
import model
import view

def ask_variant(enter):
    while True:
        try:
            a = int(input(enter))
            if a == 1:
                return True
            elif a == 2:
                return False
            else:
                view.error_choise()
        except:
            view.error_choise()

def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()

def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()

def operation():
    match (model.ops):
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')

opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

def normalization(string: str):
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    string = string.split()
    return string

def get_string(string: list):
    text = ''
    for item in string:
        text += str(item) + ' '
    return text + '= '

def deleteElement(string, i):
    string.pop(i + 1)
    string.pop(i)

def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
        deleteElement(string, i)
        return True
    
def input_viragenie(enter):
    string = normalization(input(enter))
    string_exp = get_string(string)
    while len(string)>1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if operation(string, i, '*'): break
                if operation(string, i, '/'): break
        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if operation(string, i, '+'): break
                if operation(string, i, '-'): break
   
    if string[0] != None:
        r = string[0]
        r = int(r) if float(r) == int(r) else float(r)
        logger.logger(f'{string_exp}{r}')
        return r
    else:
        view.error_value()