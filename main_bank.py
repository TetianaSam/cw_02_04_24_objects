from calculator import Calculator

"""from bankove_ucty import *
b = BankAccount(100)
b2 = BankAccount(200)
s = SavingsAccount(b, 50)

print(b)
print(s)

b.deposit(100)
s.deposit(200)

print(b.counter)
print(b2.counter)

b2.add_counter(66)
print(b.get_counter())
print(b2.get_counter())
"""
a = Calculator.add(3,6)
print(a)
b = Calculator.ans_add(8)

c = Calculator.ans_add(4)
print(c)

d = Calculator.divide(18,6)
print(d)
e = Calculator.ans_divide(a,2)
print(e)

print(Calculator.largest(1,22,3,4,52))