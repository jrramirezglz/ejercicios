from enum import Enum
class operaciones(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4

class calculadora:

    def set_val1(self):
        self.val1 =input('dame el primer valor: ')
        self.v1 = int(self.val1)

    def set_val2(self):
        self.val2 =input('dame el segundo valor: ')
        self.v2 = int(self.val2)

    def resultado(self,operacion):
        if operacion== operaciones.SUMA:
            v3 = self.v1 + self.v2
            return print('el resultado de la suma es ' , v3)
        elif  operacion == operaciones.RESTA:
            v3 = self.v1 - self.v2
            return print('el resultado de la resta es ' , v3)
        elif  operacion == operaciones.MULTIPLICACION:
            return print('el resultado de la multiplicacion es ' , v3)
            v3 = self.v1 * self.v2
        elif  operacion == operaciones.DIVISION:
            try:
                v3 = self.v1 / self.v2
                return print('el resultado de la division es ' , v3)
            except:
                print('divison entre 0 perro')
        else:
            return print ('nel')
