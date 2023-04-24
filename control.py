from model import Model
from view import View
class Control:  
    obj_model = Model()
    obj_view = View()    
    obj_model.setNum1(obj_view.num1)
    obj_model.setNum2(obj_view.num2)
    num1 = float(obj_model.getNum1())
    num2 = float(obj_model.getNum2())
    option = int(obj_view.option)
    if option == 1:
        obj_model.add(num1, num2)
    elif option == 2:
        obj_model.substraction(num1, num2)
    elif option == 3:
        obj_model.multiply(num1, num2)
    elif option == 4:
        obj_model.divide(num1, num2)

