#!/usr/bin/env python3

from random import randint


manual = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def q_a():
    """task for brain-prime"""
    quastion = randint(1, 100)
    for v in range(2, quastion // 2):
        if quastion % v == 0:
            answer = 'no' 
            return quastion, answer
    answer = 'yes' if quastion != 1 else 'no'
    return quastion, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
