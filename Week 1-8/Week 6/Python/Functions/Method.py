def mat_op(num1,num2):
    """Heyyou"""
    print(num1)
    print(id(num1))
    print(num2)
    print(id(num2))
    Multiply = num1 * num2
    print(Multiply)
    print(id(Multiply))
    divide = num1//num2
    print(divide)
    print(id(divide))
mat_op(2,8)
mat_op(16,8)
print(mat_op.__doc__)
help(mat_op)