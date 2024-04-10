#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. Write a
program that solves the N queens problem."""
import sys


solutions = []
n = 0
pos = None


def get_input():
    """This is input function"""
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def strike(mnt, po):
    """This is strike function"""
    if (mnt[0] == po[0]) or (mnt[1] == po[1]):
        return True
    return abs(mnt[0] - po[0]) == abs(mnt[1] - po[1])


def leave(group):
    """This is leave function"""
    global solutions
    for leav in solutions:
        i = 0
        for leav_pos in leav:
            for dp in group:
                if leav_pos[0] == dp[0] and leav_pos[1] == dp[1]:
                    i += 1
        if i == n:
            return True
    return False


def get_solu(row, group):
    """This is get solution function"""
    global solutions
    global n
    if row == n:
        val = group.copy()
        if not leave(val):
            solutions.append(val)
    else:
        for h in range(n):
            a = (row * n) + h
            resu = zip(list([pos[a]]) * len(group), group)
            formal_pos = map(lambda x: strike(x[0], x[1]), resu)
            group.append(pos[a].copy())
            if not any(formal_pos):
                get_solu(row + 1, group)
            group.pop(len(group) - 1)


def solved():
    """This is solved solution function"""
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n**2)))
    a = 0
    group = []
    get_solu(a, group)


n = get_input()
solved()
for i in solutions:
    print(i)
