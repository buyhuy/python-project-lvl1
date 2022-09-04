#!/usr/bin/env python3

from random import randint


manual = ('Find the greatest common divisor of given numbers.')


def q_a():
    """task for brain-gcd"""
    divisors = []
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    quastion = (f'{num1} {num2}')
    for i in range(1, 101):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    answer = divisors[-1]
    return quastion, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
