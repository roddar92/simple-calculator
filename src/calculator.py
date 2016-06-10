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
        """Evaluate input data by unary property"""
        try:
            if unary:
                data[1] = data[1].lower()
                if data[1] == "e":
                    data[1] = m.e
                elif data[1] == "pi":
                    data[1] = m.pi
                else:
                    data[1] = float(data[1])
            else:
                data[0] = data[0].lower()
                data[2] = data[2].lower()
                if data[0] == "e":
                    data[0] = m.e
                elif data[0] == "pi":
                    data[0] = m.pi
                else:
                    data[0] = float(data[0])

                if data[2] == "e":
                    data[0] = m.e
                elif data[2] == "pi":
                    data[2] = m.pi
                else:
                    data[2] = float(data[2])
        except ValueError:
            return "Input operands is not numbers"

        operation = data[0] if unary else data[1]
        if operation in self.operations:
            op = self.operations[operation]
            if op.unary:
                result = op.eval_unary(data[1])
            else:
                result = op.eval_binary(data[0], data[2])
        else:
            return "Unknown operation"

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
    assert calculator.evaluate("sqroot 49") == "Unknown operation"
