#!/usr/bin/env python3

from brain_games.cli import welcome_user, greeting


def hello_user():
    greeting()
    welcome_user()


def main():
    hello_user()

if __name__ == '__main__':
    main()

