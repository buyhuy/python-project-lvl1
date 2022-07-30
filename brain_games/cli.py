#!/usr/bin/env python3

import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
name = ''


def main():
    welcome_user()


if __name__ == '__main__':
    main()

