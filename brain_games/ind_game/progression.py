#!/usr/bin/env python3

from random import choice, randint

manual = ('What number is missing in the progression?')


def q_a():
    '''quastion for brain-progression'''
    start = randint(1, 20)
    progress = randint(1, 10)
    numbers = [start]
    while len(numbers) <= 10:
        start += progress
        numbers.append(start)
    index = randint(1, 9)
    numbers.pop(index)
    #quastion = numbers.insert(index, '..')
    numbers[index:index] = ['..']
    quastion = numbers
    answer = numbers[index - 1] + progress
    return quastion, answer


def main():
    q_a()


if __name__ == '__main__':
    main()
