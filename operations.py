import math as m


class Operation(object):
    def __init__(self):
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return 0


class AdditionOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a + b


class SubtractOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a - b


class MultiplicateOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a * b


class DivisionOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a / b


class ModOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a % b


class DivOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a // b


class PowOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return a ** b


class LogarithmByAnyBaseOperation(Operation):
    def __init__(self):
        super().__init__()

    def eval_binary(self, a, b):
        return m.log(a, b)


class LogarithmBy2Operation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.log2(a)


class LogarithmBy10Operation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.log10(a)


class LogarithmByEOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.log(a, m.e)


class SquaredRootOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.sqrt(a)


class InverseRootOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return 1 / a


class SinOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.sin(a)


class CosOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.cos(a)


class TanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.tan(a)


class CtanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return 1 / (m.tan(a))


class AsinnOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.asin(a)


class AcosOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.acos(a)


class AtanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.atan(a)


class ExponentOperation(Operation):
    def __init__(self):
        super().__init__()
        self.unary = True

    def eval_unary(self, a):
        return m.exp(a)