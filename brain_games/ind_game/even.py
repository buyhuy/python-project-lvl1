#!/usr/bin/env python3

from random import randint


manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def q_a():
    """task for brain-even"""
    quastion = randint(1, 100)
    answer = 'yes' if quastion % 2 == 0 else 'no'
    return quastion, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
