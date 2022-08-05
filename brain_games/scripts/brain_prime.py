#!/usr/bin/env python3

from brain_games.general_logic import logic
from brain_games.ind_game.prime import manual, q_a


def main():
    """script for brain-prime"""
    logic(manual, q_a)


if __name__ == '__main__':
    main()
