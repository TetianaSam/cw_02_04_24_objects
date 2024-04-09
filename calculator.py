class Calculator:
    ans = 0
    answ = 0
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def divide(a,b):
        return a / b

    @staticmethod
    def largest (*args):
        return max()

    @classmethod
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod
    def clean_ans(cls):
        cls.ans = 0

    @classmethod
    def ans_divide(cls,a,b):
        cls.answ += a/b
        return cls.answ



