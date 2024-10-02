class NotInt(Exception):
    def __init__(self, mes):
        self.mes = mes


def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        if prime(summ):
            print('Простое')
        else:
            print('Составое')
        return summ

    return wrapper


@is_prime
def sum_three(*args):
    result_ = 0
    for arg in args:
        if isinstance(arg, int):
            result_ += arg
        else:
            raise NotInt('Введены не корретные данные для сложения')
    return result_


def prime(num):
    res = 0
    if num == 2:
        return res == 0
    for i in range(2, num):
        if num % i == 0:
            res += 1
            break

    return res == 0


result = sum_three(2, 3, 6)
print(result)
