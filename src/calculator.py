# -*- coding: utf-8 -*-

""" Simple calculator """
import math as m
import operations as ops


class Calculator(object):

    def __init__(self):
        """Create dictionary with arithmetic operations"""
        self.operations = dict()

        self.operations["plus"] = ops.AdditionOperation()
        self.operations["minus"] = ops.SubtractOperation()
        self.operations["mult"] = ops.MultiplicateOperation()
        self.operations["divide"] = ops.DivisionOperation()
        self.operations["mod"] = ops.ModOperation()
        self.operations["div"] = ops.DivOperation()
        self.operations["pow"] = ops.PowOperation()
        self.operations["log_by"] = ops.LogarithmByAnyBaseOperation()
        self.operations["log"] = ops.LogarithmBy2Operation()
        self.operations["lg"] = ops.LogarithmBy10Operation()
        self.operations["ln"] = ops.LogarithmByEOperation()
        self.operations["exp"] = ops.ExponentOperation()
        self.operations["inv"] = ops.InverseOperation()
        self.operations["sqrt"] = ops.SquaredRootOperation()
        self.operations["sin"] = ops.SinOperation()
        self.operations["cos"] = ops.CosOperation()
        self.operations["tan"] = ops.TanOperation()
        self.operations["ctan"] = ops.CtanOperation()
        self.operations["asin"] = ops.AsinOperation()
        self.operations["acos"] = ops.AcosOperation()
        self.operations["atan"] = ops.AtanOperation()



    def operation(self, data, unary=False):
        try:
            if unary:
                data[1] = m.e if data[1].lower() == "e" else float(data[1])
                data[1] = m.pi if data[1].lower() == "pi" else float(data[1])
            else:
                data[0] = m.e if data[0].lower() == "e" else float(data[0])
                data[0] = m.pi if data[0].lower() == "pi" else float(data[0])
                data[2] = m.e if data[2].lower() == "e" else float(data[2])
                data[2] = m.pi if data[2].lower() == "pi" else float(data[2])
        except ValueError:
            return "Input operands is not numbers"

        result = 0.0
        if unary:
            if data[0] == "inv":
                result = 1 / data[1]
            elif data[0] == "sqrt":
                result = m.sqrt(data[1])
            elif data[0] == "log":
                result = m.log2(data[1])
            elif data[0] == "lg":
                result = m.log10(data[1])
            elif data[0] == "ln":
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
    assert calculator.evaluate("1 plus pi") == 4.141592653589793
    assert calculator.evaluate("1 minus 2") == -1
    assert calculator.evaluate("3 mult 2") == 6
    assert calculator.evaluate("1 divide 2") == 0.5
    assert calculator.evaluate("5 mod 2") == 1
    assert calculator.evaluate("5 div 2") == 2
    assert calculator.evaluate("sqrt 4") == 2
    assert calculator.evaluate("sqrt 4a") == "Input operands is not numbers"
    assert calculator.evaluate("sin 30") == -0.9880316240928618