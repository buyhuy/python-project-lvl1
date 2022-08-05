#!/usr/bin/env python3

from brain_games.general_logic import logic
from brain_games.ind_game.calc import q_a, manual


def main():
    """script for brain-calc"""
    logic(manual, q_a)


if __name__ == '__main__':
    main()
