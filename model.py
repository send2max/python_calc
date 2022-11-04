import controller
import view

first = 0
second = 0
ops = ''
total = 0
result = 0
exp = 0

def is_immediately():
    return controller.ask_variant('Выберите вариант вычисления: \n Ввести и вычислить выражение, нажмите 1 \n Пошаговый калькулятор, нажмите 2 \n:')

def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

def init_viragenie():
    global total
    total = controller.input_viragenie('Введите выражение целиком: ')
    if total != None:
        view.print_total()
        return True