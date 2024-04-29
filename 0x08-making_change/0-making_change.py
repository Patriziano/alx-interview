#!/usr/bin/python3
""" Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total """


def makeChange(coins, total):
    """ This is makechange function"""
    if total <= 0:
        return 0
    check = 0
    tem = 0
    coins.sort(reverse=True)
    for k in coins:
        while check < total:
            check += k
            tem += 1
        if check == total:
            return tem
        check -= k
        tem -= 1
    return -1
