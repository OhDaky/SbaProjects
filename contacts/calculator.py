class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2
    
    def multi(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    calc = Calculator(6, 2) # num1=6, num2=2
    sumResult = calc.sum()
    print('덧셈 결과 {}'.format(sumResult))

    subResult = calc.subtract()
    print('뺄셈 결과 {}'.format(subResult))

    multiResult = calc.multi()
    print('곱셈 결과 {}'.format(multiResult))

    divResult = calc.sum()
    print('나눗셈 결과 {}'.format(divResult))

    # 덧셈 결과 : 8
    # 뺄셈 결과 : 4
    # 곱셈 결과 : 12
    # 나눗셈 결과 : 3
    