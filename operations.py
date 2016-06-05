import math as m


class Operation(object):
    def __init__(self):
        self.name = "unknown"
        self.unary = False

    def eval_unary(self, a):
        return None

    def eval_binary(self, a, b):
        return None


class AdditionOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "plus"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a + b


class SubtractOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "minus"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a - b


class MultiplicateOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "mult"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a * b


class DivisionOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "divide"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a / b


class ModOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "mod"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a % b


class DivOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "div"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a // b


class PowOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "pow"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return a ** b


class LogarithmByAnyBaseOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "log_by"
        self.unary = False

    def eval_unary(self, a):
        return 0

    def eval_binary(self, a, b):
        return m.log(a, b)


class LogarithmBy2Operation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "log"
        self.unary = True

    def eval_unary(self, a):
        return m.log2(a)

    def eval_binary(self, a, b):
        return 0


class LogarithmBy10Operation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "log"
        self.unary = True

    def eval_unary(self, a):
        return m.log10(a)

    def eval_binary(self, a, b):
        return 0


class LogarithmByEOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "ln"
        self.unary = True

    def eval_unary(self, a):
        return m.log(a, m.e)

    def eval_binary(self, a, b):
        return 0


class SquaredRootOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "sqrt"
        self.unary = True

    def eval_unary(self, a):
        return m.sqrt(a)

    def eval_binary(self, a, b):
        return 0


class InverseRootOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "inv"
        self.unary = True

    def eval_unary(self, a):
        return 1 / a

    def eval_binary(self, a, b):
        return 0


class SinOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "sin"
        self.unary = True

    def eval_unary(self, a):
        return m.sin(a)

    def eval_binary(self, a, b):
        return 0


class CosOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "cos"
        self.unary = True

    def eval_unary(self, a):
        return m.cos(a)

    def eval_binary(self, a, b):
        return 0


class TanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "tan"
        self.unary = True

    def eval_unary(self, a):
        return m.tan(a)

    def eval_binary(self, a, b):
        return 0


class CtanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "ctan"
        self.unary = True

    def eval_unary(self, a):
        return 1 / (m.tan(a))

    def eval_binary(self, a, b):
        return 0


class AsinnOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "asin"
        self.unary = True

    def eval_unary(self, a):
        return m.asin(a)

    def eval_binary(self, a, b):
        return 0


class AcosOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "acos"
        self.unary = True

    def eval_unary(self, a):
        return m.acos(a)

    def eval_binary(self, a, b):
        return 0


class AtanOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "atan"
        self.unary = True

    def eval_unary(self, a):
        return m.atan(a)

    def eval_binary(self, a, b):
        return 0


class ExponentOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "exp"
        self.unary = True

    def eval_unary(self, a):
        return m.exp(a)

    def eval_binary(self, a, b):
        return 0