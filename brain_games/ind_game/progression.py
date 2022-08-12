#!/usr/bin/env python3

from random import randint


manual = ('What number is missing in the progression?')


def q_a():
    """task for brain-progression"""
    start = randint(1, 20)
    progress = randint(1, 10)
    numbers = [str(start)]
    while len(numbers) <= 10:
        start += progress
        numbers.append(str(start))
    index = randint(1, 9)
    numbers.pop(index)
    numbers[index:index] = ['..']
    quastion = (f'{" ".join(numbers)}')
    answer = int(numbers[index - 1]) + progress
    return quastion, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
