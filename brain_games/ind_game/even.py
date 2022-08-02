#!/usr/bin/env python3

from random import randint

manual = 'Answer "yes" if the number is even, otherwise answer "no".'

def n_a():
    '''quastion for brain-even'''
    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
