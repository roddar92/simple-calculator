# -*- coding: utf-8 -*-

""" Simple calculator """
import math as m


class Calculator(object):
    @staticmethod
    def operation(data, unary=False):
        try:
            if unary:
                data[1] = float(data[1])
            else:
                data[0] = float(data[0])
                data[2] = float(data[2])
        except ValueError:
            return "Input operands is not numbers"

        result = 0.0
        if unary:
            if data[0] == "inverse":
                result = 1 / data[1]
            elif data[0] == "sqroot":
                result = m.sqrt(data[1])
            elif data[0] == "log":
                result = m.log2(data[1])
            elif data[0] == "log_by_e":
                result = m.log(data[1], m.e)
            elif data[0] == "exp":
                result = m.exp(data[1])
            elif data[0] == "sin":
                result = m.sin(data[1])
            elif data[0] == "cos":
                result = m.cos(data[1])
            elif data[0] == "tan":
                result = m.tan(data[1])
            elif data[0] == "ctan":
                result = 1 / (m.tan(data[1]))
            elif data[0] == "asin":
                result = m.asin(data[1])
            elif data[0] == "acos":
                result = m.acos(data[1])
            elif data[0] == "atan":
                result = m.atan(data[1])
        else:
            if data[1] == "plus":
                result = data[0] + data[2]
            elif data[1] == "minus":
                result = data[0] - data[2]
            elif data[1] == "mult":
                result = data[0] * data[2]
            elif data[1] == "divide":
                result = data[0] / data[2]
            elif data[1] == "mod":
                result = data[0] % data[2]
            elif data[1] == "div":
                result = data[0] // data[2]
            elif data[1] == "pow":
                result = m.pow(data[0], data[2])
            elif data[1] == "log_by":
                result = m.log(data[0], data[2])
        return result

    def evaluate(self, expression):
        data = expression.split()
        return self.operation(data) if len(data) > 2 else self.operation(data, True)


if __name__ == "__main__":
    calculator = Calculator()
    assert calculator.evaluate("1 plus 2") == 3
    assert calculator.evaluate("1 minus 2") == -1
    assert calculator.evaluate("3 mult 2") == 6
    assert calculator.evaluate("1 divide 2") == 0.5
    assert calculator.evaluate("5 mod 2") == 1
    assert calculator.evaluate("5 div 2") == 2
    assert calculator.evaluate("sqroot 4") == 2
    assert calculator.evaluate("sqroot 4a") == "Input operands is not numbers"
    assert calculator.evaluate("sin 30") == -0.9880316240928618