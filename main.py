import controller
import model
import view

def calc_all():
    while True:
        if model.init_viragenie():
            break

def calc_tradition():
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total

if (model.is_immediately()):
    calc_all()
else:
    calc_tradition()