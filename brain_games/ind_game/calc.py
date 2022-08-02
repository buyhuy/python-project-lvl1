#!/usr/bin/env python3

from operator import add, sub, mul
from random import choice, randint

manual = ('What is the result of the expression?')

def q_a():
    '''quastion for brain-calc'''
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    do = choice(['+', '-', '*'])
    quastion = (f'{num1} {do} {num2}')
    if do == '+':
        answer = add(num1, num2)
    elif do == '-':
        answer = sub(num1, num2)
    elif do == '*':
        answer = mul(num1, num2)
    return quastion, answer


def main():
    q_a()


if __name__  == '__main__':
    main()